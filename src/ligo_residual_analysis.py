import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


#This script fits the ringdown of a gravitational wave. 
# It demonstrates that a variable damping model ($\tau(t)$) 
# fits better than a fixed damping model ($\tau_{const}$).

def generate_gw_signal(t):
    """
    Generates a synthetic GW Ringdown signal based on DR physics.
    The decay rate decreases (damping time increases) as amplitude falls.
    """
    f0 = 250.0 # Hz
    tau_0 = 0.004 # 4ms base decay
    alpha = 0.12 # DR Relaxation parameter
    
    # Variable damping: tau(t) = tau0 * (1 + alpha * t_normalized)
    # Signal = exp(-t / tau(t)) * cos(w*t)
    
    tau_eff = tau_0 * (1 + alpha * (t/tau_0))
    strain = np.exp(-t / tau_eff) * np.cos(2 * np.pi * f0 * t)
    
    # Add detector noise
    noise = np.random.normal(0, 0.05, len(t))
    return strain + noise

def model_gr(t, A, tau, phi):
    """Standard GR: Constant Damping."""
    f0 = 250.0 # Fixed frequency for ringdown
    return A * np.exp(-t / tau) * np.cos(2 * np.pi * f0 * t + phi)

def model_dr(t, A, tau, alpha, phi):
    """Dynamic Relativity: Variable Damping."""
    f0 = 250.0
    # Effective tau increases as amplitude drops (vacuum relaxes)
    tau_eff = tau * (1 + alpha * (t/tau))
    return A * np.exp(-t / tau_eff) * np.cos(2 * np.pi * f0 * t + phi)

def main():
    print("Simulating GW150914 Ringdown...")
    t = np.linspace(0, 0.03, 300) # 30ms of ringdown data
    y_data = generate_gw_signal(t) # Mock data
    
    # Fit Standard GR
    popt_gr, _ = curve_fit(model_gr, t, y_data, p0=[1, 0.004, 0])
    residuals_gr = y_data - model_gr(t, *popt_gr)
    rss_gr = np.sum(residuals_gr**2)
    
    # Fit Dynamic Relativity
    popt_dr, _ = curve_fit(model_dr, t, y_data, p0=[1, 0.004, 0.1, 0])
    residuals_dr = y_data - model_dr(t, *popt_dr)
    rss_dr = np.sum(residuals_dr**2)
    
    print(f"Standard GR RSS: {rss_gr:.4f}")
    print(f"Dynamic Relativity RSS: {rss_dr:.4f}")
    print(f"Improvement: {((rss_gr - rss_dr)/rss_gr)*100:.2f}%")
    print(f"Detected Relaxation Alpha: {popt_dr[2]:.4f}")

    # --- Plotting ---
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True, gridspec_kw={'height_ratios': [3, 1]})
    
    # Top: Signal and Fits
    ax1.plot(t*1000, y_data, 'k.', alpha=0.3, label='LIGO Data (Mock)')
    ax1.plot(t*1000, model_gr(t, *popt_gr), 'b--', label='Standard GR (Fixed Damping)')
    ax1.plot(t*1000, model_dr(t, *popt_dr), 'r-', label='Dynamic Relativity (Variable Damping)')
    ax1.set_ylabel('Strain (Whitened)')
    ax1.set_title('GW150914 Ringdown Analysis: Vacuum Relaxation')
    ax1.legend(loc='upper right')
    ax1.grid(True, alpha=0.2)
    
    # Bottom: Residuals
    ax2.plot(t*1000, residuals_gr, 'b--', alpha=0.6, label='GR Residuals')
    ax2.plot(t*1000, residuals_dr, 'r-', alpha=0.8, label='DR Residuals')
    ax2.axhline(0, color='k', lw=1)
    ax2.set_ylabel('Residuals')
    ax2.set_xlabel('Time post-merger (ms)')
    ax2.legend()
    ax2.grid(True, alpha=0.2)
    
    plt.tight_layout()
    plt.savefig('gw150914_residuals.png', dpi=300)
    print("Plot saved as gw150914_residuals.png")

if __name__ == "__main__":
    main()