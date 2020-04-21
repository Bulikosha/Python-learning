# FINISHED

""" Напишите программу, которая считывает с клавиатуры два числа a и b, считает и выводит на консоль среднее
арифметическое всех чисел из отрезка [a; b], которые делятся на 3.
В приведенном ниже примере среднее арифметическое считается для чисел на отрезке [-5; 12].
Всего чисел, делящихся на 3, на этом отрезке 6: -3, 0, 3, 6, 9, 12. Их среднее арифметическое равно 4.5
На вход программе подаются интервалы, внутри которых всегда есть хотя бы одно число, которое делится на 3. """

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
s = []
counter = 0
for number in range(a,b+1):
    if number % 3 == 0 and a < b:
        s.append(number)
        counter += 1
    elif number % 3 == 0 and a > b:
        a,b = b,a
        s.append(number)
        counter += 1
    elif number % 3 != 0:
        continue
print(sum(s)/counter)

# Optimal solution
"""
a,b = int(input()), int(input())
a += -a%3
b -= b%3
print((a+b)/2)
"""