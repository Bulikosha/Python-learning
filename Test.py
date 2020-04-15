"""Вычислить сумму целых чисел на отрезке от а до b
Например: от 3 до 7"""

value_1 = int(input())
value_2 = int(input())
summ = 0
i = value_1

while i <= value_2:
    summ += i
    i += 1

print(summ)