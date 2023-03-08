from MaTrix import Matrix

def abs(x):
    if x > 0:
        return x
    else:
        return -x

def gauss_elimination(A, b):
    n = A.rows

    for i in range(n):
        max_el = abs(A.data[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(A.data[k][i]) > max_el:
                max_el = abs(A.data[k][i])
                max_row = k

        for k in range(i, n):
            temp = A.data[max_row][k]
            A.data[max_row][k] = A.data[i][k]
            A.data[i][k] = temp
        temp = b[max_row]
        b[max_row] = b[i]
        b[i] = temp

        for k in range(i + 1, n):
            c = -A.data[k][i] / A.data[i][i]
            for j in range(i, n):
                if i == j:
                    A.data[k][j] = 0
                else:
                    A.data[k][j] += c * A.data[i][j]
            b[k] += c * b[i]

    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / A.data[i][i]
        for k in range(i - 1, -1, -1):
            b[k] -= A.data[k][i] * x[i]

    return x

n = int(input("Nhập kích thước ma trận: "))
a = [[] for i in range(n)]

for i in range(n):
    a[i] = list(map(float, input(f"Nhập hàng {i}: ").split()))


b = list(map(float, input(f"Nhập ma trận kết quả : ").split()))

A = Matrix(n, n, a)

print("Nghiệm của hệ phương trình: ")
print(gauss_elimination(A, b))