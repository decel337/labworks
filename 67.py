n = int(input("Input number of term range: "))
a0 = 1
for i in range(1, n+1):
    a = (i * a0 + 1) / i
    a0 = a
print("Value term range:", round(a, 6))
