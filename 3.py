import numpy as np
from scipy.interpolate import CubicSpline

def lagrange_interpolation(x, y, x_interp):
    n = len(x)
    m = len(x_interp)
    y_interp = np.zeros(m)

    for j in range(m):
        for i in range(n):
            L = 1.0
            for k in range(n):
                if k != i:
                    L *= (x_interp[j] - x[k]) / (x[i] - x[k])
            y_interp[j] += y[i] * L

    return y_interp

def divided_differences(x, y):
    n = len(x)
    f = np.zeros((n, n))
    f[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            f[i, j] = (f[i+1, j-1] - f[i, j-1]) / (x[i+j] - x[i])

    return f

def newton_interpolation(x, y, x_interp):
    n = len(x)
    m = len(x_interp)
    f = divided_differences(x, y)
    y_interp = np.zeros(m)

    for j in range(m):
        p = 1.0
        for i in range(n):
            y_interp[j] += f[0, i] * p
            p *= (x_interp[j] - x[i])

    return y_interp

def cubic_spline_interpolation(x, y, x_interp):
    cs = CubicSpline(x, y)
    y_interp = cs(x_interp)
    return y_interp

if __name__ == "__main__":
    # Dữ liệu mẫu
    x = np.array([0, 1, 2, 3, 4])
    y = np.array([0, 1, 2, 3, 4])

    # Các điểm nội suy
    x_interp = np.array([0.5, 1.5, 2.5, 3.5])

    # Phương pháp Lagrange
    y_interp_lagrange = lagrange_interpolation(x, y, x_interp)
    print("Lagrange interpolation:", y_interp_lagrange)

    # Phương pháp Newton
    y_interp_newton = newton_interpolation(x, y, x_interp)
    print("Newton interpolation:", y_interp_newton)

    # Phương pháp Cubic Spline
    y_interp_cubic_spline = cubic_spline_interpolation(x, y, x_interp)
    print("Cubic Spline interpolation:", y_interp_cubic_spline)
