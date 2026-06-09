
# funkcja znajduje pierwiastek równania f(x) = 0 metodą Riddersa
# Jest to metoda oparta na metodzie falsi, wymagająca mniejszej liczby iteracji.
# Po znalezieniu punktu xc = 1
# 2(xa + xb). = jak w metodzie bisekcji szukamy
# funkcji wykładniczej eu takiej, żeby pasowała do analizowanej funkcji f w
# xa, xc i xb, czyli
# f (xa) −2f (xc)eu + f (xb)e2u = 0. (3.4)
# Ten warunek jest spełniony jeżeli
# eu = 1
# f (xb)
# (
# f (xc) + sign(f (xa))√f (xc)2 −f (xa)f (xb)
# )
# . (3.5)
# Po zastosowaniu metody falsi do punktów (xa, f (xa)eu) i (xb, f (xb)e2u) (za-
# miast (xa, f (xa)) i (xb, f (xb))) dostaje się kolejne przybliżenie szukanego pier-
# wiastka:
# xd = xc + (xc −xa)sign(f (xa) −f (xc))f (xc)√f (xc)2 −f (xa)f (xb) . (3.6)
# Następnie należy rozważyć trzy przedziały (a - d, d - c, c - b) i sprawdzić w
# którym z nich jest zero funkcji:
# f (xa)f (xd) < 0 ⇒ xb ←xd
# f (xd)f (xb) < 0 ⇒ xa ←xd
# 14
# f (xd)f (xc) < 0 ⇒ xa ←xc, xb ←xd
# Dla właściwego przedziału należy obliczyć
# xc = 1
# 2(xa + xb), (3.7)
# a następnie przejść do następnej iteracji, czyli wyznaczyć punkt xd z równa-
# nia 3.6.

import math
def ridders(f, a, b, tol=1e-7, max_iter=1000):
    if f(a) * f(b) >= 0:
        raise ValueError("Funkcja musi mieć różne znaki na końcach przedziału [a, b].")

    for i in range(max_iter):
        c = 0.5 * (a + b)  # Punkt środkowy
        f_c = f(c)

        if abs(f_c) < tol:
            return c  # Znaleziono pierwiastek

        # Oblicz eu
        eu = 1
        if f_c**2 - f(a) * f(b) > 0:
            eu = math.sqrt(f_c**2 - f(a) * f(b))

        # Oblicz xd
        xd = c + (c - a) * math.copysign(1, f(a) - f_c) * f_c / eu

        if abs(f(xd)) < tol:
            return xd  # Znaleziono pierwiastek

        # Sprawdź, w którym przedziale jest zero funkcji
        if f(a) * f(xd) < 0:
            b = xd
        elif f(xd) * f(b) < 0:
            a = xd
        else:
            a = c
            b = xd

    raise ValueError("Nie osiągnięto zbieżności w zadanej liczbie iteracji.")


# Przykład użycia

# Definicja funkcji, której pierwiastek chcemy znaleźć
def example_function(x):
    return x**2 - 2

a = 0  # Początek przedziału
b = 2  # Koniec przedziału

try:
    root = ridders(example_function, a, b)
    print(f"Pierwiastek równania x^2 - 2 = 0 to: {root}")
except ValueError as e:
    print(e)
