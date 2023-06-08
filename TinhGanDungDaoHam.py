import numpy as np

def f(x):
    return np.sin(x)

def forward_difference_5point(f, x, h):
    return (f(x - 2 * h) - 8 * f(x - h) + 8 * f(x + h) - f(x + 2 * h)) / (12 * h)

if __name__ == "__main__":
    a = 0.0  # Điểm bắt đầu của khoảng
    b = 1.0  # Điểm kết thúc của khoảng
    n = 5    # Số điểm mốc

    h = (b - a) / (n - 1)  # Khoảng cách giữa các điểm mốc

    x = np.linspace(a, b, n)  # Điểm bắt đầu
    dy_dx_approx = forward_difference_5point(f, x, h)

    print("f'(x) =", dy_dx_approx)
