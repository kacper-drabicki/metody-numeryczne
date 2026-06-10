H = 100
M0 = 10
G = 10

mc = 0.1
K = 0.01  
C = 1.0   


def mass(t):
	m = M0 - 0.5 * K * t * t
	return m if m > mc else mc

def rhs(t, y, v):
	m = mass(t)
	a = -G - (C / m) * v * abs(v)
	return v, a

def rk4_step(t, y, v, h):
	k1y, k1v = rhs(t, y, v)
	k2y, k2v = rhs(t + 0.5 * h, y + 0.5 * h * k1y, v + 0.5 * h * k1v)
	k3y, k3v = rhs(t + 0.5 * h, y + 0.5 * h * k2y, v + 0.5 * h * k2v)
	k4y, k4v = rhs(t + h, y + h * k3y, v + h * k3v)

	y_next = y + (h / 6.0) * (k1y + 2.0 * k2y + 2.0 * k3y + k4y)
	v_next = v + (h / 6.0) * (k1v + 2.0 * k2v + 2.0 * k3v + k4v)
	return y_next, v_next


t_burn = (2.0 * (M0 - mc) / K) ** 0.5

t = 0.0
y = H
v = 0.0

h = 0.1
h_min = 1e-6
h_max = 1.0
tol = 1e-6

t_prev, y_prev = t, y
max_iter = 2_000_000

for _ in range(max_iter):
    if y <= 0.0:
        break

    y1, v1 = rk4_step(t, y, v, h)

    yh, vh = rk4_step(t, y, v, 0.5 * h)
    y2, v2 = rk4_step(t + 0.5 * h, yh, vh, 0.5 * h)

    err = max(abs(y2 - y1), abs(v2 - v1))

    if err <= tol or h <= h_min:
        t_prev, y_prev = t, y
        t += h
        y, v = y2, v2

        if err == 0.0:
            s = 2.0
        else:
            s = 0.9 * (tol / err) ** 0.2
        s = min(2.0, max(0.5, s))
        h = min(h_max, max(h_min, h * s))
    else:
        s = max(0.1, 0.9 * (tol / err) ** 0.2)
        h = max(h_min, h * s)

if y <= 0.0 and y != y_prev:
    frac = y_prev / (y_prev - y)
    t_ground = t_prev + frac * (t - t_prev)
else:
    t_ground = float("nan")

print(f"Czas wypalenia flary: {t_burn:.6f} s")
print(f"Czas upadku na powierzchnie: {t_ground:.6f} s")

if t_ground < t_burn:
    print("Flara uderza o ziemie zanim przestanie sie palic.")
else:
    print("Flara przestaje sie palic przed uderzeniem o ziemie.")


