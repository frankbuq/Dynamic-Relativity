import numpy as np
import matplotlib.pyplot as plt

#Script A: verify_flyby_anomaly.py
#Output: flyby_trajectory.png
#
#Physics: Integrates the conformal gradient along a hyperbolic trajectory (Earth Flyby).


def verify_flyby():
    # Constants
    G = 6.674e-11
    M_Earth = 5.972e24
    R_Earth = 6371e3
    c = 3e8
    
    # Trajectory Simulation (Hyperbolic Flyby)
    t = np.linspace(-3000, 3000, 1000) # seconds from perigee
    v_inf = 8900 # m/s (approx Galileo velocity)
    b = R_Earth + 950e3 # Impact parameter (altitude 950km)
    
    # Simplified 2D Trajectory (x, y)
    r = np.sqrt(b**2 + (v_inf * t)**2)
    v = v_inf # approx constant for gradient calc
    
    # Gradient Norms
    # Spatial: GM/r^2
    grad_phi = (G * M_Earth) / r**2
    # Temporal: v * grad_phi (Convection)
    dphi_dt = v * grad_phi
    
    # Calculate Conformal Factor mu
    # mu = 1 + a0 / S_total
    a0 = 1.2e-10
    S_total = np.sqrt(grad_phi**2 + (dphi_dt/c)**2)
    mu = 1 + a0 / S_total
    
    # Calculate Asymmetry Force (Wake - Bow)
    # The anomaly comes from the dot product of Velocity and Gradient Asymmetry
    # We simulate this as a scaling factor difference along the track
    
    # Asymmetry factor (approximate geometric drag)
    asymmetry = (dphi_dt / c) / S_total 
    
    # Anomaly Acceleration: a_anom ~ g * (mu - 1) * asymmetry
    a_anom = grad_phi * (mu - 1) * asymmetry
    
    # Integrate Delta V
    # FIXED FOR NUMPY 2.0+: Changed np.trapz to np.trapezoid
    delta_v_accum = np.trapezoid(a_anom, t) * 1000 # Convert to mm/s
    
    print(f"Predicted Delta V: {delta_v_accum:.2f} mm/s")
    
    # Plot
    plt.figure(figsize=(10,5))
    plt.subplot(1,2,1)
    plt.plot(t/60, a_anom * 1e6)
    plt.xlabel('Time from Perigee (min)')
    plt.ylabel('Anomalous Accel (microns/s^2)')
    plt.title('Anomaly Profile')
    plt.grid(True)
    
    plt.subplot(1,2,2)
    plt.plot(t/60, np.cumsum(a_anom)*(t[1]-t[0])*1000)
    plt.xlabel('Time from Perigee (min)')
    plt.ylabel('Accumulated Delta V (mm/s)')
    plt.title(f'Total Prediction: {delta_v_accum:.2f} mm/s')
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('flyby_trajectory.png')
    print("Plot saved as flyby_trajectory.png")

if __name__ == "__main__":
    verify_flyby()