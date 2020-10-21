# Для заданої довжини ребра куба знайти обєм куба і площу його бічної поверхні
a = float(input("Enter the edge of the cube: "))  # ребро куба
if a > 0: #существует ли куб
    V = a ** 3  # обєм куба
    S = 4 * a * a  # площа бічної поверхні
    print("Cube volume:", round(V, 5)) #вывод
    print("Side surface area:", round(S, 5)) #вывод
else:
    print("Unreal")


