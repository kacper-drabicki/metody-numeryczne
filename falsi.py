# funkcja rozwiązuje równanie f(x) = 0 metodą falsi
import math


def falsi(f, a, b, tol=1e-7, max_iter=1000):
    if f(a) * f(b) >= 0:
        raise ValueError("Funkcja musi mieć różne znaki na końcach przedziału [a, b].")

    for i in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))  # Punkt przecięcia linii łączącej (a, f(a)) i (b, f(b)) z osią x
        f_c = f(c)

        if abs(f_c) < tol:
            return c  # Znaleziono pierwiastek

        if f_c * f(a) < 0:
            b = c  # Pierwiastek jest w przedziale [a, c]
        else:
            a = c  # Pierwiastek jest w przedziale [c, b]

    raise ValueError("Nie osiągnięto zbieżności w zadanej liczbie iteracji.")

# Przykład użycia

# Definicja funkcji, której pierwiastek chcemy znaleźć
def example_function(x):
    return x**2-2

a = 0  # Początek przedziału
b = 2  # Koniec przedziału

try:
    root = falsi(example_function, a, b)
    print(f"Pierwiastek równania x^2 - 2 = 0 to: {root}")
except ValueError as e:
    print(e)