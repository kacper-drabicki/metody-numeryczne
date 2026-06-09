import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# 1. Definicja układu równań wahadła
def pendulum_system(t, y, g_over_l=1.0):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = -g_over_l * np.sin(theta)
    return [dtheta_dt, domega_dt]

# 2. Definicja przedziału czasu symulacji
t_span = (0, 20)
t_eval = np.linspace(t_span[0], t_span[1], 1000)

# 3. Lista różnych warunków początkowych [theta_0, omega_0]
# Dobieramy je tak, by pokazać drgania, ruch graniczny oraz pełne obroty
initial_conditions = [
    [0.5, 0.0],   # Małe drgania
    [1.5, 0.0],   # Średnie drgania
    [2.8, 0.0],   # Duże drgania (blisko punktu krytycznego)
    [0.0, 1.8],   # Szybki ruch oscylacyjny
    [0.0, 2.5],   # Pełne obroty w prawo (cyrkulacja)
    [0.0, -2.5]   # Pełne obroty w lewo
]

# 4. Tworzenie wykresu
plt.figure(figsize=(10, 6))

for i, y0 in enumerate(initial_conditions):
    # Rozwiązanie układu dla danego warunku początkowego
    sol = solve_ivp(pendulum_system, t_span, y0, t_eval=t_eval)
    
    # Wyciągamy położenie (theta) i prędkość/pęd (omega)
    theta_res = sol.y[0]
    omega_res = sol.y[1]
    
    # Rysowanie trajektorii fazowej
    plt.plot(theta_res, omega_res, label=f"Stan pocz.: $\\theta_0$={y0[0]}, $\\omega_0$={y0[1]}")

# 5. Formatowanie i estetyka wykresu
plt.title("Portret fazowy wahadła matematycznego (bez przybliżeń)", fontsize=14)
plt.xlabel("Położenie kątowe $\\theta$ [rad]", fontsize=12)
plt.ylabel("Prędkość kątowa / Pęd $\\omega$ [rad/s]", fontsize=12)
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right')

# Ograniczenie osi dla lepszej czytelności (zakres wokół głównych trajektorii)
plt.xlim(-4, 4)
plt.ylim(-3.5, 3.5)

# Wyświetlenie wykresu
plt.tight_layout()
plt.show()