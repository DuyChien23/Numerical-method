import numpy as np

def f(x):
    return np.sin(x)

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    sum = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x_i = a + i * h
        sum += f(x_i)
    return h * sum

def midpoint_rule(f, a, b, n):
    h = (b - a) / n
    sum = 0.0
    for i in range(n):
        x_i = a + (i + 0.5) * h
        sum += f(x_i)
    return h * sum

def simpson_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Number of intervals must be even for Simpson's rule")
    h = (b - a) / n
    sum = f(a) + f(b)
    for i in range(1, n, 2):
        x_i = a + i * h
        sum += 4 * f(x_i)
    for i in range(2, n-1, 2):
        x_i = a + i * h
        sum += 2 * f(x_i)
    return h * sum / 3

if __name__ == "__main__":
    a = 0.0  # Điểm bắt đầu của khoảng
    b = 1.0  # Điểm kết thúc của khoảng
    n = 50  # Số đoạn chia

    trapezoidal_result = trapezoidal_rule(f, a, b, n)
    midpoint_result = midpoint_rule(f, a, b, n)
    simpson_result = simpson_rule(f, a, b, n)

    print("Trapezoidal Rule result:", trapezoidal_result)
    print("Midpoint Rule result:", midpoint_result)
    print("Simpson Rule result:", simpson_result)
