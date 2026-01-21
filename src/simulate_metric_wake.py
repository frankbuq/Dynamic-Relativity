import numpy as np
import matplotlib.pyplot as plt

#Script C: simulate_metric_wake.pyOutput: metric_wake_simulation.png
# Physics: Solves the 1D Wave Equation to show the Potential 
# ($\mu$) lagging behind the Mass ($M$) during a collision.

def simulate_wake():
    # Space-time grid
    x = np.linspace(0, 100, 200)
    dx = x[1] - x[0]
    dt = 0.1
    c_sim = 5.0 # Simulation speed of light
    
    # Source Mass (Gaussian) moving right
    def mass_density(x, t, v=2.0):
        pos = 20 + v * t
        return np.exp(-(x - pos)**2 / 10.0)
    
    # Wave Equation: d2u/dt2 = c^2 d2u/dx2 + Source
    u = np.zeros_like(x) # Field mu
    u_prev = np.zeros_like(x)
    u_next = np.zeros_like(x)
    
    # Time stepping
    snapshots = []
    for t in np.arange(0, 30, dt):
        source = mass_density(x, t)
        
        # Finite Difference
        laplacian = (np.roll(u, -1) - 2*u + np.roll(u, 1)) / dx**2
        u_next = 2*u - u_prev + (c_sim*dt)**2 * laplacian + source * dt**2
        
        u_prev = u.copy()
        u = u_next.copy()
        
        if abs(t - 15) < dt: # Capture at t=15
            snapshots = (x, u, source)

    # Plot
    x_grid, field, source = snapshots
    
    plt.figure(figsize=(10,6))
    plt.plot(x_grid, source, 'k--', label='Baryonic Mass (Gas)')
    plt.plot(x_grid, field/np.max(field), 'b-', lw=2, label='Metric Potential (Lensing)')
    plt.fill_between(x_grid, field/np.max(field), color='blue', alpha=0.1)
    
    plt.annotate('Metric Wake\n(Dark Matter Signal)', xy=(45, 0.5), xytext=(20, 0.8),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    
    plt.xlabel('Position')
    plt.ylabel('Amplitude')
    plt.title('Simulation of Retarded Potential (Bullet Cluster)')
    plt.legend()
    plt.grid(True)
    plt.savefig('metric_wake_simulation.png')

if __name__ == "__main__":
    simulate_wake()