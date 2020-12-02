def Combinations(Weight):
    NumberOfVariants = 0
    for x in range(1, 2**len(VariantsOfWeight)):
        TempWeight = 0
        for i in range(0, 10):
            TempWeight += VariantsOfWeight[i] * (x % 2)
            x = x // 2
        if TempWeight == Weight:
            NumberOfVariants += 1
    return NumberOfVariants
Weight = int(input("Weight: "))
VariantsOfWeight = [100, 200, 300, 500, 1000, 1200, 1400, 1500, 2000, 3000]
print("NumberOfVariants:", Combinations(Weight))
