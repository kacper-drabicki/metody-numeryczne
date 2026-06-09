

# funkcja rozwiązująca równanie f(x) = 0 metodą Newtona-Raphsona, która przybliża pochodną funkcji f w punkcie x0 i iteracyjnie poprawia przybliżenie, aż do osiągnięcia zadanego tolerancji lub maksymalnej liczby iteracji
def newton_raphson(f, x0, tol=1e-7, max_iter=1000):
    def derivative(f, x, h=1e-5):
        return (f(x + h) - f(x - h)) / (2 * h)

    x = x0
    for i in range(max_iter):
        f_x = f(x)
        if abs(f_x) < tol:
            return x
        f_prime_x = derivative(f, x)
        if f_prime_x == 0:
            raise ValueError("Pochodna jest równa zero. Wybierz inne przybliżenie początkowe.")
        x = x - f_x / f_prime_x

    raise ValueError("Nie osiągnięto zbieżności w zadanej liczbie iteracji.")

# Prosty przykład użycia

# Przykładowa funkcja: f(x) = x^2 - 2, której pierwiastkiem jest sqrt(2)
def example_function(x):
    return x**2 - 2

initial_guess = 1.0
root = newton_raphson(example_function, initial_guess)
print(f"Pierwiastek z 2 to około: {root}")