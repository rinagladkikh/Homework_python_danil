# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

num = int(input("Введите трехзначное число: "))
a = num % 10
b = (num % 100) // 10
c = num // 100
print("Сумма цифр =", a+b+c)