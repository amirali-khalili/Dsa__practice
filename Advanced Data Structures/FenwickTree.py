class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)  # اندیس از 1 شروع می‌شه

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i   # میره سراغ بخش بعدی

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i   # میره سراغ بخش قبلی
        return s

    def range_sum(self, l, r):
        return self.query(r) - self.query(l - 1)


# تست
arr = [2, 1, 1, 3, 2, 3, 4, 5, 6]
ft = FenwickTree(len(arr))

# ساخت درخت با آپدیت‌ها
for i, val in enumerate(arr, 1):
    ft.update(i, val)

print(ft.query(5))        # جمع از اول تا 5 → 2+1+1+3+2 = 9
print(ft.range_sum(3, 7)) # جمع بین 3 تا 7 → 1+3+2+3+4 = 13
