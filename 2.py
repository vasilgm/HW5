# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4

a = int(input('Введите число а -> '))
b = int(input('Введите число b -> '))

def funktion_A (A,B):
    if A == 1:
        return 1
    else:
        return funktion_A (A-1, B) + 1

def funktion_B (A,B):
    if B == 1:
        return 1
    else:
        return funktion_B (A, B-1) + 1

print (funktion_A(a, b) + funktion_B(a, b))