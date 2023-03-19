from MaTrix import Matrix
def jacobi(A, b, x0, tol=1e-6, max_iter=1000):
    n = A.rows
    x = x0.copy()
    for k in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            s = sum(A.data[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A.data[i][i]
        if all(abs(x_new[i]-x[i]) < tol for i in range(n)):
            return x_new
        x = x_new
    return x



n = int(input("Nhập kích thước ma trận: "))
a = [[] for i in range(n)]

for i in range(n):
    a[i] = list(map(float, input(f"Nhập hàng {i}: ").split()))


b = list(map(float, input(f"Nhập ma trận kết quả : ").split()))

A = Matrix(n, n, a)

x = [0 for i in range(n)]

print("Nghiệm của hệ phương trình: ")
print(jacobi(A, b, x))