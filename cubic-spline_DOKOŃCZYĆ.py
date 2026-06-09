
# funkcja obliczająca wartość interpolacji cubic spline
def cubic_spline(x, y, x_interp):
    n = len(x)
    a = y.copy()
    h = [x[i+1] - x[i] for i in range(n-1)]
    
    # obliczanie macierzy A i wektora B
    A = [[0] * n for _ in range(n)]
    B = [0] * n
    
    for i in range(1, n-1):
        A[i][i-1] = h[i-1]
        A[i][i] = 2 * (h[i-1] + h[i])
        A[i][i+1] = h[i]
        B[i] = 3 * ((a[i+1] - a[i]) / h[i] - (a[i] - a[i-1]) / h[i-1])
    
    # warunki brzegowe naturalne
    A[0][0] = 1
    A[n-1][n-1] = 1
    
    # rozwiązywanie układu równań A * c = B
    c = [0] * n
    for i in range(1, n):
        factor = A[i][i-1] / A[i-1][i-1]
        for j in range(i, n):
            A[i][j] -= factor * A[i-1][j]
        B[i] -= factor * B[i-1]
    
    c[n-1] = B[n-1] / A[n-1][n-1]
    for i in range(n-2, -1, -1):
        c[i] = (B[i] - A[i][i+1] * c[i+1]) / A[i][i]
    
    # obliczanie współczynników b i d
    b = [0] * (n-1)
    d = [0] * (n-1)
    
    for i in range(n-1):
        b[i] = (a[i+1] - a[i]) / h[i] - h[i] * (2*c[i] + c[i+1]) / 3
        d[i] = (c[i+1] - c[i]) / (3*h[i])
    
    # interpolacja dla x_interp
    if x_interp < x[0]:
        return None  # poza
    if x_interp > x[-1]:
        return None  # poza

    # znajdowanie przedziału, w którym znajduje się x_interp
    for i in range(n-1):
        if x[i] <= x_interp <= x[i+1]:
            # obliczanie wartości interpolacyjnej
            dx = x_interp - x[i]
            return a[i] + b[i] * dx + c[i] * dx**2 + d[i] * dx**3

# przykładowe dane
x = [0,1,2,3,4,5,6,7,8,9]
y = [0,0,0,0,0,10,10,10,10,10]


# obliczenie wartości wielomianu interpolacyjnego w punkcie dla 100 punktów pomiędzy 0 a 9
t = [i * 0.1 for i in range(101)]
interpolated_value = [cubic_spline(x, y, t) for t in t]
# wykres wielomianu interpolacyjnego
import matplotlib.pyplot as plt

plt.plot(t, interpolated_value, label='Wielomian interpolacyjny cubic spline')
plt.scatter(x, y, color='red', label='Węzły interpolacyjne')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolacja cubic spline')
plt.legend()
plt.show()