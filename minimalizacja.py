from scipy.optimize import curve_fit
import numpy as np

def f(t, a, b):
    return a*np.exp(-b*t)

popt, pcov = curve_fit(f, t, y)

print("a =", popt[0])
print("b =", popt[1])

print("błędy =", np.sqrt(np.diag(pcov)))