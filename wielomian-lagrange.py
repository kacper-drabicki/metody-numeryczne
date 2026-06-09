
# funkcja znajdująca wielomian interpolacyjny Lagrange'a

def lagrange_interpolation(x, y, t):
    n = len(x)
    result = 0.0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (t - x[j]) / (x[i] - x[j])
        result += term
    return result

# przykładowe dane
x = [0,1,2,3,4,5,6,7,8,9]
y = [0,0,0,0,0,10,10,10,10,10]


# obliczenie wartości wielomianu interpolacyjnego w punkcie dla 100 punktów pomiędzy 0 a 9
t = [i * 0.1 for i in range(101)]
interpolated_value = [lagrange_interpolation(x, y, t) for t in t]
# wykres wielomianu interpolacyjnego
import matplotlib.pyplot as plt

plt.plot(t, interpolated_value, label='Wielomian interpolacyjny Lagrange\'a')
plt.scatter(x, y, color='red', label='Węzły interpolacyjne')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolacja Lagrange\'a')
plt.legend()
plt.show()