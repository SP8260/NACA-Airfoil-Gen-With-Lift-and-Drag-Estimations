import math
import matplotlib.pyplot as plt

naca = input("Enter 4 digit NACA:")
init_m = int(naca[0])
init_p = int(naca[1])
init_t = int(naca[2:])

m = init_m * 0.01
p = init_p * 0.1
t = init_t * 0.01

baseline_points = 100

upper_x = []
lower_x = []
upper_y = []
lower_y = []
camber_x = []
camber_y = []
drag_y = []
lift_y = []
ld_ratio_y = []

sum_I0 = 0
sum_A1 = 0

for i in range(baseline_points):
    beta = (i/ (baseline_points-1))*math.pi
    x = 0.5*(1-math.cos(beta))
    yt = t/0.2*(0.2969*math.sqrt(x) - 0.1260*x - 0.3516*x**2 + 0.2843*x**3 - 0.1036*x**4)
    
    if m == 0:
        yc = 0
        theta = 0
    elif x <= p:
        yc = m/p**2*(2*p*x - x**2)
        theta = math.atan((2*m/p**2)*(p-x))
    else:
        yc = (m/(1-p)**2)*((1-2*p)+2*p*x - x**2)
        theta = math.atan(((2*m)/(1-p)**2)*(p-x))
    
    camber_x.append(x)
    camber_y.append(yc)
    
    xu = x - yt*math.sin(theta)
    yu = yc + yt*math.cos(theta)
    
    xl = x+yt*math.sin(theta)
    yl = yc - yt*math.cos(theta)
    
    upper_x.append(xu)
    lower_x.append(xl)
    upper_y.append(yu)
    lower_y.append(yl)

for i in range(0, baseline_points-1):
    x = camber_x[i]
    beta = (i/(baseline_points-1))*math.pi
    d_theta = math.pi/(baseline_points-1)
    
    if m == 0:
        dyc_dx = 0.0
    elif x<=p:
        dyc_dx = ((2*m)/(p**2))*(p-x)
    if x>p:
        dyc_dx = (((2*m)/((1-p)**2))*(p-x))
    
    sum_I0 += dyc_dx * d_theta
    sum_A1 += (dyc_dx * math.cos(beta)) * d_theta

    
I0 = sum_I0 / math.pi
A1 = (2 * sum_A1) / math.pi

Cd0 = 0.006 + (0.05 * t)
k = 0.01


alpha_deg_list = [-5, 0, 5, 10]
for alpha_deg in alpha_deg_list:
    alpha_rad = math.radians(alpha_deg)
    Cl = 2 * math.pi * (alpha_rad - I0) + math.pi * A1
    lift_y.append(Cl)
    
    Cd = Cd0 + k * (Cl ** 2)
    drag_y.append(Cd)
    
    ld_ratio_y.append(Cl/Cd if Cd != 0 else 0)

fig, ax = plt.subplots(2, 2, figsize=(8,7.2))


ax[0, 0].set_title("NACA Airfoil")
ax[0, 0].plot(upper_x, upper_y, label="Upper surface", color="blue")
ax[0, 0].plot(lower_x, lower_y, label="Lower surface", color="orange")
ax[0, 0].plot(camber_x, camber_y, label="Mean Camber", color="black", linestyle="--", alpha=0.7)
ax[0, 0].set_aspect('equal', adjustable='box')
ax[0, 0].grid(True)

ax[0, 1].set_title("Lift Coefficient (Cl)")
ax[0, 1].plot(alpha_deg_list, lift_y, label="Lift", color="red")
ax[0, 1].set_xlabel("Alpha (degrees)")
ax[0, 1].grid(True)

ax[1, 0].set_title("Drag Estimation (Cd)")
ax[1, 0].plot(alpha_deg_list, drag_y, label="Drag", color="green")
ax[1, 0].set_xlabel("Alpha (degrees)")
ax[1, 0].grid(True)

ax[1, 1].set_title("Lift-Drag Ratio (Cl/Cd)")
ax[1, 1].plot(alpha_deg_list, ld_ratio_y, label="L/D Ratio", color="purple")
ax[1, 1].set_xlabel("Alpha (degrees)")
ax[1, 1].grid(True)

plt.tight_layout()
plt.show()



