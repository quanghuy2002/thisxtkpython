ten = input("Nhập tên của bạn:  ")
print(ten)
n = len(ten)

d = dict()
for i in range(1, n + 1):
    d[i] = i * i

print(d)
