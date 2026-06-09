
# funkcja obliczająca transformatę Fouriera dla sygnału dyskretnego
def fourier_transform(signal):
    N = len(signal)
    transform = []
    
    for k in range(N):
        sum_real = 0
        sum_imag = 0
        
        for n in range(N):
            angle = (2 * 3.141592653589793 * k * n) / N
            sum_real += signal[n] * cos(angle)
            sum_imag += signal[n] * sin(angle)
        
        transform.append(complex(sum_real, sum_imag))
    
    return transform