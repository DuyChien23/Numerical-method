def newton_interpolation(x, y, z):
    n = len(x)
    f = [[0.0] * n for i in range(n)]

    for i in range(n):
        f[i][0] = y[i]

    for j in range(1, n):
        for i in range(n-j):
            f[i][j] = (f[i+1][j-1] - f[i][j-1]) / (x[i+j] - x[i])

    # Tính giá trị nội suy
    f_interp = f[0][0]
    for i in range(1, n):
        prod = 1
        for j in range(i):
            prod *= (z - x[j])
        f_interp += f[0][i] * prod

    return f_interp


n = int(input("Nhập số lượng điểm: "))

x = [0.0] * n
y = [0.0] * n

for i in range(n):
    l = list(map(float, input(f"Nhập điểm thứ {i}: ").split()))
    x[i] = l[0]
    y[i] = l[1]

xfind = float(input("Tính f(x) với x = "))
print(f"f({xfind}) = {newton_interpolation(x, y, xfind)}")