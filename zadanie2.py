import numpy as np
from scipy.linalg import eigvals

macierz = np.array([[1,2,3],[4,6,8],[7,1,9]])

wartosci_wlasne = eigvals(macierz)

print(f'Jedna z wartości własnych: {wartosci_wlasne[:1].item()}')