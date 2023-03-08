import array

class Func:
    def __init__(self, n, a):
        self.n = n
        self.a = a
    def get(self, x):
        X = 1
        ans = 0
        for c in self.a:
            ans += X * c
            X *= x
        return ans
    def derivative(self):
        arr = array.array('f')
        for i in range(1, self.n + 1, 1):
            arr.append(i * self.a[i])
        return Func(self.n - 1, arr)