from MaTrix import Matrix

def abs(x):
    if x > 0:
        return x
    else:
        return -x

def doolittle(A, b):
    n = A.rows
    L = Matrix(n, n, [[0.0] * n for i in range(n)])
    U = Matrix(n, n, [[0.0] * n for i in range(n)])
    for i in range(n):
        # Tính phần tử trên đường chéo của ma trận U
        U.data[i][i] = 1.0
        for j in range(i, n):
            s1 = sum(U.data[k][j] * L.data[i][k] for k in range(i))
            U.data[i][j] = A.data[i][j] - s1
        # Tính phần tử dưới đường chéo của ma trận L
        for j in range(i, n):
            if i == j:
                L.data[i][i] = 1.0
            else:
                s2 = sum(U.data[k][i] * L.data[j][k] for k in range(i))
                L.data[j][i] = (A.data[j][i] - s2) / U.data[i][i]
    # Giải hệ phương trình tuyến tính LY = b
    y = [0.0] * n
    for i in range(n):
        s3 = sum(L.data[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - s3) / L.data[i][i]
    # Giải hệ phương trình tuyến tính UX = Y
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        s4 = sum(U.data[i][j] * x[j] for j in range(i+1, n))
        x[i] = (y[i] - s4) / U.data[i][i]
    return x

n = int(input("Nhập kích thước ma trận: "))
a = [[] for i in range(n)]

for i in range(n):
    a[i] = list(map(float, input(f"Nhập hàng {i}: ").split()))

b = list(map(float, input(f"Nhập ma trận kết quả : ").split()))

A = Matrix(n, n, a)

print("Nghiệm của hệ phương trình: ")
print(doolittle(A, b))