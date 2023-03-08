import array
from HamSo import Func

def newton(f, df, x0, tol, max_iter):
    i = 0
    x = x0
    while i < max_iter:
        fx = f.get(x)
        if abs(fx) < tol:
            return x
        dfx = df.get(x)

        if dfx == 0:
            raise ValueError("Không thể tìm nghiệm vì f'(x) = 0")
        x = x - fx / dfx
        i += 1
    raise ValueError("Số lần lặp tối đa đã đạt được mà không tìm được nghiệm")

n = int(input("Nhập bậc cao nhất của hàm số: "))
print("Nhập hệ số: ")

a = array.array('f')

for i in range(0, n + 1, 1):
    c = float(input(f"Hệ số bậc {i}: "))
    a.append(c)

f = Func(n, a)

x0 = float(input("Điểm bắt đầu: "))
loop = int(input("Số lần lặp tối đa: "))
tol = float(input("Sai số: "))

print(f"Nghiệm tìm được {newton(f, f.derivative(), x0, tol, loop)}")