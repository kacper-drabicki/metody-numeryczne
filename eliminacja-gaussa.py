import numpy as np

# funkcja wykonująca eliminacje Gaussa dla macierzy A i wektora b bez pivotowania
def eliminacja_gaussa(A, b):
    n = len(A)
    # tworzymy macierz rozszerzoną [A|b]
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    # eliminacja w dół
    for i in range(n):
        # dla każdego wiersza poniżej i-tego
        for j in range(i + 1, n):
            # obliczamy współczynnik eliminacji
            factor = Ab[j][i] / Ab[i][i]
            # odejmujemy odpowiednią wielokrotność wiersza i od wiersza j
            Ab[j] = Ab[j] - factor * Ab[i]
    
    # teraz macierz jest górnotrójkątna, możemy rozwiązać układ równań
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i][-1] - np.dot(Ab[i][i + 1:n], x[i + 1:n])) / Ab[i][i]
    
    return x

# przykład użycia
A = np.array([[3, 2, -4], [2, 3, 3], [5, -3, 1]], dtype=float)
b = np.array([3, 15, 14], dtype=float)
x = eliminacja_gaussa(A, b)
print("Rozwiązanie układu równań Ax = b:", x)