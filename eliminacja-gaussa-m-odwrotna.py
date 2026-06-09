import numpy as np

# funkcja znajdująca odwrotność macierzy A za pomocą eliminacji Gaussa
def odwrotna_macierzy(A):
    n = len(A)
    # tworzymy macierz rozszerzoną [A|I], gdzie I to macierz jednostkowa
    AI = np.hstack([A, np.eye(n)])
    
    # eliminacja w dół
    for i in range(n):
        # dla każdego wiersza poniżej i-tego
        for j in range(i + 1, n):
            # obliczamy współczynnik eliminacji
            factor = AI[j][i] / AI[i][i]
            # odejmujemy odpowiednią wielokrotność wiersza i od wiersza j
            AI[j] = AI[j] - factor * AI[i]
    
    # robimy jedynki na diagonali
    for i in range(n):
        AI[i] = AI[i] / AI[i][i]

    # eliminacja w góre
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            factor = AI[j][i] / AI[i][i]
            AI[j] = AI[j] - factor * AI[i]

    # macierz odwrotna znajduje się po prawej stronie rozszerzonej macierzy
    return AI[:, n:]

# przykład użycia (łatwy przykład, żeby łatwo zweryfikować wynik)
A = np.array([[2, 1], [5, 3]], dtype=float)
odwrotna_A = odwrotna_macierzy(A)
print("Odwrotność macierzy A:", odwrotna_A)
# wypisz wynik ze znanem rozwiązaniem, aby zweryfikować poprawność
print("Sprawdzenie: A * A^-1 =", A@odwrotna_A)