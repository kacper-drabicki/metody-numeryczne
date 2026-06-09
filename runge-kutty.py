# funkcja obliczająca rozwiązanie równania różniczkowego metodą Rungego-Kutty
def runge_kutta(f, x0, y0, h, n):
    x = x0
    y = y0

    for _ in range(n):
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)

        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        x += h

    return x, y

