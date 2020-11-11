x = float(input("Input value x: "))
n = 1


def p(x, n):
    return (((-1) ** (n - 1)) * ((x - 1) ** n)) / n


sum = p(x, n)
if 0 < x < 2:
    while abs(p(x, n + 1) - p(x, n)) > 10 ** (-6):
        n += 1
        sum += p(x, n)
    print("Your function value:", round(sum + p(x, n + 1), 6))
else:
    print("Error! Print numbr х є (0;2)")
