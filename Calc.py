# FINISHED

def calc (res):
    res = 0
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    c = str(input("Введите операцию (plus, minus, multiply, divide): "))
    if c.lower() == "plus" or c == "+":
        res = a + b
    elif c.lower() == "minus" or c == "-":
        res = a - b
    elif c.lower() == "multiply" or c == "*":
        res = a * b
    elif c.lower() == "divide" or c == "/":
        res = a / b
    else:
        print("Введите верное значение")
    return res

print(calc(1))

