n = int(input("Input value n: "))
print("Reciprocal numbers with " + str(n) + ":", end=" ")
for i in list(range(1, n)):
    p = n
    k = i
    while p != 0 and k != 0:
        if p > k:
            p = p % k
        else:
            k = k % p
    if p + k == 1:
        print(i, end=" ")
