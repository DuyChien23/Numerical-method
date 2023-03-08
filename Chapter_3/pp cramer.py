from MaTrix import Matrix

def abs(x):
    if x > 0:
        return x
    else:
        return -x

def cramer(A, b):
    n = A.rows
    det_A = A.det()
    if det_A == 0:
        print("Ma trận hệ số không khả nghịch")
        return None
    x = [0 for i in range(n)]

    for i in range(n):
        Ai = A.copy()
        for j in range(n):
            Ai.data[j][i] = b[j]
        det_Ai = Ai.det()
        x[i] = det_Ai / det_A
    return x

n = int(input("Nhập kích thước ma trận: "))
a = [[] for i in range(n)]

for i in range(n):
    a[i] = list(map(float, input(f"Nhập hàng {i}: ").split()))

b = list(map(float, input(f"Nhập ma trận kết quả : ").split()))

A = Matrix(n, n, a)

print("Nghiệm của hệ phương trình: ")
print(cramer(A, b))