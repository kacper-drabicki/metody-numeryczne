import numpy as np
import matplotlib.pyplot as plt
from math import factorial

# współczynnik dwumianowy dla wykładnika rzeczywistego
def binomial_real(alpha, n):
    if n == 0:
        return 1.0

    result = 1.0
    for k in range(n):
        result *= (alpha - k)
    return result / factorial(n)

# rozwinięcie Taylora sqrt(x) wokół x0 = 1
def taylor_sqrt(x, order):
    alpha = 0.5
    y = np.zeros_like(x, dtype=float)

    for n in range(order + 1):
        coeff = binomial_real(alpha, n)
        y += coeff * (x - 1) ** n

    return y

# zakres argumentów
x = np.linspace(0.1, 2.0, 1000)

# funkcja dokładna
y_exact = np.sqrt(x)

# rzędy rozwinięcia
orders = [2, 3, 5, 10]

plt.figure(figsize=(10, 6))

# wykres funkcji dokładnej
plt.plot(x, y_exact, 'k', linewidth=2,
         label=r'$\sqrt{x}$')

# wykresy przybliżeń
for n in orders:
    y_taylor = taylor_sqrt(x, n)
    plt.plot(x, y_taylor,
             label=f'Rząd {n}')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Rozwinięcie Taylora funkcji sqrt(x) wokół x=1')
plt.grid(True)
plt.legend()
plt.show()