import numpy as np
import matplotlib.pyplot as plt

# Parametry
t_max = 1000 * np.pi
num_points = 10000
t = np.linspace(0, t_max, num_points)

# Funkcja sin(t)
signal = np.sin(t)

# Dodaj szum o amplitudzie +- 0.2
noise = np.random.uniform(-0.2, 0.2, num_points)
signal_noisy = signal + noise

# Transformata Fouriera
fft = np.fft.fft(signal_noisy)
frequencies = np.fft.fftfreq(num_points, t[1] - t[0])

# Usuń częstości poza podstawową 
fft_filtered = fft.copy()
fft_filtered[2:] = 0

# Transformata odwrotna
signal_reconstructed = np.fft.ifft(fft_filtered).real

# Wizualizacja
fig, axes = plt.subplots(1, 1, figsize=(12, 10))
axes.plot(t, signal_reconstructed, 'g-', linewidth=1, label='Sygnał odbudowany')
axes.set_xlabel('t')
axes.set_ylabel('amplituda')

plt.tight_layout()
plt.show()
