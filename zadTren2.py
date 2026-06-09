import numpy as np
import matplotlib.pyplot as plt
from datetime import date

# -------------------------
# Parametry orbity Ziemi
# -------------------------
e = 0.0167          # mimośród
a = 1.0             # pół oś wielka [AU]
T = 365.25          # okres obiegu [dni]

# Data peryhelium
perihelion = date(2020, 1, 5)

# Dzisiejsza data
today = date.today()

# -------------------------
# Rozwiązanie równania Keplera
# -------------------------
def kepler(M, e, tol=1e-12, max_iter=100):
    E = M

    for _ in range(max_iter):
        f = E - e * np.sin(E) - M
        df = 1 - e * np.cos(E)

        E_new = E - f / df

        if abs(E_new - E) < tol:
            return E_new

        E = E_new

    return E

# -------------------------
# Położenie planety
# -------------------------
def position(days_from_perihelion):
    M = 2 * np.pi * (days_from_perihelion % T) / T
    E = kepler(M, e)

    x = a * (np.cos(E) - e)
    y = a * np.sqrt(1 - e**2) * np.sin(E)

    return x, y

# -------------------------
# Orbita - cały bieżący rok
# -------------------------
year = today.year
start_year = date(year, 1, 1)

days = np.arange(0, 366)

x_orbit = []
y_orbit = []

for d in days:
    current_date = start_year.fromordinal(start_year.toordinal() + d)

    dt = (current_date - perihelion).days
    x, y = position(dt)

    x_orbit.append(x)
    y_orbit.append(y)

# -------------------------
# Położenie dzisiejsze
# -------------------------
dt_today = (today - perihelion).days
x_today, y_today = position(dt_today)

# -------------------------
# Wykres
# -------------------------
plt.figure(figsize=(8, 8))

plt.plot(x_orbit, y_orbit,
         label=f'Orbita Ziemi w roku {year}')

# Słońce znajduje się w ognisku elipsy
plt.scatter(0, 0, s=120, marker='*',
            label='Słońce')

plt.scatter(x_today, y_today,
            s=80,
            label=f'Ziemia ({today})')

plt.xlabel('x [AU]')
plt.ylabel('y [AU]')
plt.title('Położenie Ziemi względem Słońca')
plt.axis('equal')
plt.grid(True)
plt.legend()

plt.show()