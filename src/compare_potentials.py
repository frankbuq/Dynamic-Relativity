import numpy as np
import matplotlib.pyplot as plt


# This script solves the saturation physics to visualize 
# the core theoretical claim: that the "Newtonian-to-Galactic" 
# transition horizon moves depending on the mass of the star.


# --- Constants ---
G = 6.67430e-11
M_SOL = 1.989e30
AU_TO_M = 1.496e11
A0 = 1.2e-10

def calculate_g_obs(r_au, mass_sol):
    """
    Numerically solves the DR relation: g * tanh(g/a0) = g_newton
    """
    r = r_au * AU_TO_M
    mass = mass_sol * M_SOL
    g_newt = G * mass / r**2
    
    # Iterative solver for g_obs
    g_guess = np.sqrt(g_newt * A0) # Initial guess (deep limit)
    for _ in range(10):
        # Simple fixed point iteration usually converges fast for this function
        g_guess = g_newt / np.tanh(g_guess / A0)
    
    return g_guess

def main():
    r_au = np.logspace(2, 5, 500) # 100 AU to 100,000 AU
    
    # 1. Solar Mass System
    g_newt_sol = (G * M_SOL) / (r_au * AU_TO_M)**2
    g_dr_sol = np.array([calculate_g_obs(r, 1.0) for r in r_au])
    
    # 2. Red Dwarf System (0.8 Solar Mass)
    g_newt_rd = (G * 0.8 * M_SOL) / (r_au * AU_TO_M)**2
    g_dr_rd = np.array([calculate_g_obs(r, 0.8) for r in r_au])
    
    # Calculate Horizon Locations (where g_newt = 3*a0)
    # Theory: r_sat = sqrt(GM / 3a0)
    r_sat_sol = np.sqrt((G * M_SOL) / (3 * A0)) / AU_TO_M
    r_sat_rd = np.sqrt((G * 0.8 * M_SOL) / (3 * A0)) / AU_TO_M
    
    print(f"Horizon (Solar): {r_sat_sol:.0f} AU")
    print(f"Horizon (Red Dwarf): {r_sat_rd:.0f} AU")

    # --- Plotting ---
    plt.figure(figsize=(10, 6))
    
    # Plot curves (Ratio of DR / Newton to show the "Boost")
    plt.semilogx(r_au, g_dr_sol / g_newt_sol, 'k-', label='Sun (1.0 M_sun)')
    plt.semilogx(r_au, g_dr_rd / g_newt_rd, 'r--', label='Red Dwarf Binary (0.8 M_sun)')
    
    # Mark Horizons
    plt.axvline(r_sat_sol, color='k', linestyle=':', alpha=0.5)
    plt.text(r_sat_sol * 1.1, 1.5, f'{r_sat_sol:.0f} AU', rotation=90)
    
    plt.axvline(r_sat_rd, color='r', linestyle=':', alpha=0.5)
    plt.text(r_sat_rd * 0.8, 2.5, f'{r_sat_rd:.0f} AU', color='red', rotation=90)

    plt.xlabel('Distance from Source (AU)')
    plt.ylabel('Gravity Boost Factor ($g_{obs} / g_{newton}$)')
    plt.title('The Mass-Dependent Saturation Horizon')
    plt.legend()
    plt.grid(True, which="both", alpha=0.3)
    
    plt.ylim(1, 10)
    plt.xlim(500, 20000)
    plt.savefig('saturation_horizon_theory.png', dpi=300)
    print("Plot saved as saturation_horizon_theory.png")

if __name__ == "__main__":
    main()