import numpy as np

def analytical_solution(t, x0=1.0, v0=0.0, omega=1.0):
    x = x0 * np.cos(omega * t) + (v0 / omega) * np.sin(omega * t)
    v = -x0 * omega * np.sin(omega * t) + v0 * np.cos(omega * t)
    return x, v

def euler_step(x, v, h, omega=1.0):
    x_next = x + h * v
    v_next = v - h * (omega**2) * x
    return x_next, v_next

def modified_euler_step(x, v, h, omega=1.0):
    x_pred = x + h * v
    v_pred = v - h * (omega**2) * x
    
    x_next = x + (h / 2.0) * (v + v_pred)
    v_next = v - (h / 2.0) * (omega**2) * (x + x_pred)
    return x_next, v_next

def rk4_step(x, v, h, omega=1.0):
    kx1 = v
    kv1 = -(omega**2) * x
    
    kx2 = v + (h / 2.0) * kv1
    kv2 = -(omega**2) * (x + (h / 2.0) * kx1)
    
    kx3 = v + (h / 2.0) * kv2
    kv3 = -(omega**2) * (x + (h / 2.0) * kx2)
    
    kx4 = v + h * kv3
    kv4 = -(omega**2) * (x + h * kx3)
    
    x_next = x + (h / 6.0) * (kx1 + 2*kx2 + 2*kx3 + kx4)
    v_next = v + (h / 6.0) * (kv1 + 2*kv2 + 2*kv3 + kv4)
    return x_next, v_next

# Parametry globalne symulacji
omega = 1.0
t_max = 2 * (2 * np.pi / omega)  # Dokładnie dwa okresy drgań
x_exact, v_exact = analytical_solution(t_max)

steps_sizes = [0.1, 0.01, 0.001]

print(f"Rozwiązanie dokładne przy t = {t_max:.4f}: x = {x_exact:.6f}, v = {v_exact:.6f}\n")

for h_target in steps_sizes:
    steps = int(round(t_max / h_target))
    h = t_max / steps  # Korekta kroku, aby idealnie trafić w czas t_max
    
    # Warunki początkowe dla każdej z metod
    x_e, v_e = 1.0, 0.0
    x_m, v_m = 1.0, 0.0
    x_r, v_r = 1.0, 0.0
    
    # Pętla główna integracji
    for _ in range(steps):
        x_e, v_e = euler_step(x_e, v_e, h, omega)
        x_m, v_m = modified_euler_step(x_m, v_m, h, omega)
        x_r, v_r = rk4_step(x_r, v_r, h, omega)
        
    print(f"--- Wyniki dla kroku h = {h:.4f} ({steps} kroków) ---")
    print(f"Euler:     x = {x_e:9.6f} (błąd: {abs(x_e - x_exact):.2e}), v = {v_e:9.6f} (błąd: {abs(v_e - v_exact):.2e})")
    print(f"Mod.Euler: x = {x_m:9.6f} (błąd: {abs(x_m - x_exact):.2e}), v = {v_m:9.6f} (błąd: {abs(v_m - v_exact):.2e})")
    print(f"RK4:       x = {x_r:9.6f} (błąd: {abs(x_r - x_exact):.2e}), v = {v_r:9.6f} (błąd: {abs(v_r - v_exact):.2e})\n")