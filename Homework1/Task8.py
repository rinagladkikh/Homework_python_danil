# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите размер шоколадки, длина: "))
m = int(input("Введите размер шоколадки, вторая ширина: "))
k = int(input("Cколько долек хотите отломить: "))
if (k % m == 0 or k % n == 0) and k < m * n:
    print("yes")
else:
    print("no")