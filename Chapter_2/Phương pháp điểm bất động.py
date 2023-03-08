import array
from HamSo import Func

def fixed_point(g, x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        x_next = g.get(x)
        if abs(x_next - x) < tol:
            return x_next
        x = x_next
    return None

n = int(input("Nhập bậc cao nhất của hàm số: "))
print("Nhập hệ số: ")

a = array.array('f')

for i in range(0, n + 1, 1):
    c = float(input(f"Hệ số bậc {i}: "))
    if i != 1:
        a.append(-c)
    else:
        a.append(1 - c)

g = Func(n, a)

x0 = float(input("Điểm bắt đầu: "))
loop = int(input("Số lần lặp tối đa: "))
efs = float(input("Sai số: "))

print(f"Nghiệm tìm được {fixed_point(g, x0, efs, loop)}")