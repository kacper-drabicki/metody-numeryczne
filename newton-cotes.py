# funkcja całkowania metodą Newtona-Cotesa
def newton_cotes(f, a, b, n):
    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]

    return h*(y[0]/2 + y[-1]/2 + sum(y[1:-1]))

# przykładowe użycie

import math

# funkcja do całkowania
def f(x):
    return x**2

a = 0  # początek przedziału
b = 1  # koniec przedziału
n = 100  # liczba podprzedziałów

result = newton_cotes(f, a, b, n)
print(f"Wynik całkowania: {result}")