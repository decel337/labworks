# Given number x, y. (x, y) ?c G, G - initial set
x = float(input("Input x: "))
y = float(input("Input y: "))
if ((y >= (1 - x)) and x <= 0) or ((y >= (1 - x)) and y <= 0):
    print("Belong to G")
else:
    print("Not belong to G")
