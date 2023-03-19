def spline_cubic(x, y):
    n = len(x)

    h = [0.0 for i in range(n - 1)]
    for i in range(n - 1):
        h[i] = x[i + 1] - x[i]

    alpha = [0.0 for i in range(n - 2)]

    for i in range(1, n - 1):
        alpha[i - 1] = (3 / h[i]) * (y[i + 1] - y[i]) - (3 / h[i - 1]) * (y[i] - y[i - 1])

    l, u, z = [0.0 for i in range(n)], [0.0 for i in range(n - 1)], [0.0 for i in range(n)]
    l[0] = 1.0

    for i in range(1, n - 1):
        l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * u[i - 1]
        u[i] = h[i] / l[i]
        z[i] = (alpha[i - 1] - h[i - 1] * z[i - 1]) / l[i]

    l[n - 1] = 1
    z[n - 1] = 0

    b, c, d = [0.0 for i in range(n - 1)], [0.0 for i in range(n)], [0.0 for i in range(n - 1)]

    for j in range(n - 2, -1, -1):
        c[j] = z[j] - u[j] * c[j + 1]
        b[j] = (y[j + 1] - y[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])


    return b, c, d

# Khởi tạo dữ liệu đầu vào
n = int(input("Nhập số lượng điểm: "))

x = [0.0] * n
y = [0.0] * n

for i in range(n):
    l = list(map(float, input(f"Nhập điểm thứ {i}: ").split()))
    x[i] = l[0]
    y[i] = l[1]

# Tính toán hệ số đa thức bậc ba của từng đoạn
b, c, d = spline_cubic(x, y)

# Đánh giá giá trị của hàm spline tại một điểm mới
x_new = float(input("Tính f(x) với x = "))
i = 0
while x[i] < x_new:
    i += 1
i -= 1
y_new = y[i] + b[i]*(x_new-x[i]) + c[i]*(x_new-x[i])**2 + d[i]*(x_new-x[i])**3

print("Giá trị của hàm spline tại x_new = {}: {}".format(x_new, y_new))
