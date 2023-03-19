from MaTrix import Matrix
def gauss_seidel(A, b, x0, tol=1e-6, max_iter=1000):
    n = A.rows
    x = x0.copy()
    for k in range(max_iter):
        for i in range(n):
            s = sum(A.data[i][j] * x[j] for j in range(i))
            t = sum(A.data[i][j] * x[j] for j in range(i+1, n))
            x[i] = (b[i] - s - t) / A.data[i][i]
        if all(abs(x[i]-x0[i]) < tol for i in range(n)):
            return x
        x0 = x.copy()
    return x


n = int(input("Nhập kích thước ma trận: "))
a = [[] for i in range(n)]

for i in range(n):
    a[i] = list(map(float, input(f"Nhập hàng {i}: ").split()))


b = list(map(float, input(f"Nhập ma trận kết quả : ").split()))

A = Matrix(n, n, a)

x = [0 for i in range(n)]

print("Nghiệm của hệ phương trình: ")
print(gauss_seidel(A, b, x))