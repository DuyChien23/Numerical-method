import array
from HamSo import Func

def bisection(f, a, b, tol):
    if f.get(a) * f.get(b) >= 0:
        raise ValueError("Khoảng cách ban đầu không chứa nghiệm!")

    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if f.get(c) == 0:
            return c
        elif f.get(c) * f.get(a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

n = int(input("Nhập bậc cao nhất của hàm số: "))
print("Nhập hệ số: ")

a = array.array('f')

for i in range(0, n + 1, 1):
    c = float(input(f"Hệ số bậc {i}: "))
    a.append(c)

f = Func(n, a)

l = float(input("Giới hạn dưới: "))
r = float(input("Giới hạn trên: "))
efs = float(input("Sai số: "))

print(f"Nghiệm tìm được {bisection(f, l, r, efs)}")