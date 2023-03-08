import array
from HamSo import Func

def secant_method(f, x0, x1, eps):
    while abs(x1 - x0) > eps:
        x2 = x1 - f.get(x1) * (x1 - x0) / (f.get(x1) - f.get(x0))
        x0, x1 = x1, x2
    return x1

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

print(f"Nghiệm tìm được {secant_method(f, l, r, efs)}")