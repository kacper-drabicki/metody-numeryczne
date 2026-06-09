import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# 1. Definiowanie parametrów modelu
alpha = 2.0
beta = 0.2
delta = 0.01
gamma = 0.2

# 2. Definiowanie układu równań różniczkowych (funkcja pochodnych)
def lotka_volterra(t, y):
    k, l = y
    dk_dt = (alpha - beta * l) * k
    dl_dt = (delta * k - gamma) * l
    return [dk_dt, dl_dt]

# 3. Definiowanie warunków początkowych i przedziału czasu
# Wybieramy stan początkowy (k=30, l=4) różny od punktu równowagi (20, 10)
y0 = [30, 4]
t_span = (0, 30)  # czas symulacji od 0 do 30 jednostek
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # punkty, dla których chcemy zapisać wynik

# 4. Rozwiązanie układu równań za pomocą metody RK45
sol = solve_ivp(lotka_volterra, t_span, y0, t_eval=t_eval, method='RK45')

# 5. Wizualizacja wyników
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Wykres 1: Zmiana populacji w czasie
ax1.plot(sol.t, sol.y[0], 'b-', linewidth=2, label='Króliki (ofiary, k)')
ax1.plot(sol.t, sol.y[1], 'r-', linewidth=2, label='Lisy (drapieżniki, l)')
ax1.set_xlabel('Czas t')
ax1.set_ylabel('Liczebność populacji')
ax1.set_title('Zmiana populacji w czasie')
ax1.grid(True)
ax1.legend()

# Wykres 2: Portret fazowy (zależność l od k)
ax2.plot(sol.y[0], sol.y[1], 'g-', linewidth=2)
ax2.plot(y0[0], y0[1], 'ro', label='Stan początkowy (30, 4)')
ax2.plot(gamma/delta, alpha/beta, 'kx', label='Punkt stacjonarny (20, 10)')
ax2.set_xlabel('Populacja ofiar (k)')
ax2.set_ylabel('Populacja drapieżników (l)')
ax2.set_title('Portret fazowy układu')
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.savefig('lotka_volterra.png')
print("Symulacja zakończona pomyślnie. Wykres zapisano jako lotka_volterra.png")