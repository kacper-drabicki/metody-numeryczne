import numpy as np

# funkcja znajdująca wartości własne i wektory własne macierzy A za pomocą odwrotnej iteracji
def odwrotna_iteracja(A, ai_0, Pi_0, tol=1e-3, max_iter=1000):
    n = len(A)
    ai = ai_0
    Pi = Pi_0 #/ np.linalg.norm(Pi_0)  # normalizujemy wektor Pi_0

    for _ in range(max_iter):
        # rozwiązujemy równanie (A - ai*I)xi = Pi
        xi = np.linalg.solve(A - ai * np.eye(n), Pi)

        # normalizujemy xi
        xi_norm = np.linalg.norm(xi)
        if xi_norm == 0:
            raise ValueError("Wektor xi jest zerowy, wybierz inne ai_0 lub Pi_0.")
        Pi = xi / xi_norm

        # aktualizujemy wartość własną
        ai_new = ai + 1 / (Pi @ xi)

        # sprawdzamy kryterium zbieżności
        if abs(1 / (Pi @ xi)) < tol:
            break

        ai = ai_new

    return ai, Pi

# przykład użycia
A = np.array([[1, 2], [3, 4]], dtype=float)
ai_0 = -0.4  # początkowe przybliżenie wartości własnej
Pi_0 = np.array([1.0, 1.0])  # losowy wektor początkowy
ai, Pi = odwrotna_iteracja(A, ai_0, Pi_0)
print("Wartość własna:", ai)
print("Wektor własny:", Pi)