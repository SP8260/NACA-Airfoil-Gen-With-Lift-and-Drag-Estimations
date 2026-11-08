# NACA-Airfoil-Gen-With-Lift-and-Drag-Equations

A Python script that generates 2D profiles of NACA 4-digit airfoils and estimates their aerodynamic lift and drag characteristics using Thin Airfoil Theory and a standard Drag Polar model.

## Features
* **Airfoil Generation**: Computes upper, lower, and mean camber line coordinates from any standard NACA 4-digit code.
* **Lift Coefficient ($C_l$)**: Evaluates lift curves across various angles of attack using Thin Airfoil Theory Fourier constants ($I_0$ and $A_1$).
* **Drag Estimation ($C_d$)**: Calculates parasitic and induced drag coefficients using an empirical drag polar configuration.
* **Aerodynamic Efficiency**: Plots the Lift-to-Drag ($L/D$) ratio across standard operation profiles.

## Prerequisites
Ensure you have Python 3 and matplotlib installed:

```bash
pip install matplotlib
```

## Usage
Run the script from your terminal:

```bash
python naca_generator.py
```

Enter a standard 4-digit NACA code when prompted (e.g., `2412` or `0012`).

## Accuracy Constraints
The numerical lift and drag approximations rely heavily on standard thin airfoil assumptions. Estimations are most reliable under these parameters:
* **Thickness (last two digits)**: Between 06 and 12
* **Maximum Camber (first digit)**: Between 0 and 4
* **Camber Position (second digit)**: Between 4 and 5
