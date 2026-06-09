from scipy.stats import norm
from scipy.integrate import quad

def dystrybuanta(x):
    return (1 - norm.cdf(x))

print(dystrybuanta(0))