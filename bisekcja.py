# funkcja rozwiązuje równanie f(x) = 0 metodą bisekcji
def bisekcja(f, a, b, tol=1e-7, max_iter=1000):
    if f(a) * f(b) >= 0:
        raise ValueError("Funkcja musi mieć różne znaki na końcach przedziału [a, b].")
    
    for i in range(max_iter):
        c = (a + b) / 2  # punkt środkowy
        if f(c) == 0 or (b - a) / 2 < tol:
            return c  # znaleziono rozwiązanie lub osiągnięto tolerancję
        
        if f(c) * f(a) < 0:
            b = c  # rozwiązanie jest w lewej połowie
        else:
            a = c  # rozwiązanie jest w prawej połowie
    
    return (a + b) / 2  # zwraca najlepsze przybliżenie po max_iter iteracjach

# Prosty przykład użycia funkcji bisekcja

import math
    
# Przykładowa funkcja: f(x) = x^2 - 2 (szukamy pierwiastka z 2)
def f(x):
    return x**2 - 2

a = 0
b = 2
root = bisekcja(f, a, b)
print(f"Przybliżony pierwiastek z 2: {root}")
print(f"Sprawdzenie: f({root}) = {f(root)}")