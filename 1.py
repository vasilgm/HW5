# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input('Введите число а -> '))
b = int(input('Введите степень b -> '))

def funktion(A,B):
    if B == 1:
        return A
    else:
        return funktion(A, B-1)*A

print (funktion(a, b))