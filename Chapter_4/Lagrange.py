def lagrange_interpolation(x, y, z):
    n = len(x)
    p = 0.0
    for j in range(n):
        L = 1.0
        for i in range(n):
            if i != j:
                L *= (z - x[i]) / (x[j] - x[i])
        p += y[j] * L
    return p

n = int(input("Nhập số lượng điểm: "))

x = [0.0] * n
y = [0.0] * n

for i in range(n):
    l = list(map(float, input(f"Nhập điểm thứ {i}: ").split()))
    x[i] = l[0]
    y[i] = l[1]

xfind = float(input("Tính f(x) với x = "))
print(f"f({xfind}) = {lagrange_interpolation(x, y, xfind)}")