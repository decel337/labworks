a = list(map(float, input().split()))
print(len(a))
sum = 0
sum1 = 0
list = []
list1 = []
for i in a:
    sum += i
k = round(sum / 100, 4)
print(sum, k)
for p in a:
    list.append(round(p - k, 3))
print(*list)
for u in list:
    list1.append(round(u**2, 6))
print(*list1)
for m in list1:
    sum1 += m
t = round(sum1/100, 6)
print(sum1, t)
