#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 08:06:38 2020

@author: nia
"""

s=''
while not s.isalpha(): #s.isalpha() повертає True, якщо там лише букви
    s=input('введите букви: ')
#s=int(s)
print('дальше будет работать с  x=' s)


s = ''
while not s.isdigit(): #s.isdigit() повертає True, якщо лише цифри
    s = input('Введите положительное целое число:')
x = int(s)
print('Дальше будет работать с x='+s)


print('Вычиcление соседних чисел Фибоначчи для числа', x)
fib1 = 1
fib2 = 1
while fib2 < x:
    # Следующее число Фибоначчи определяется как сумма двух предыдщуих
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
print(fib1, '<', x, '<=', fib2)


i = 0
while i < 10:
    # .....
    i += 1
print(i)



# Примерно так выглядит for "под-капотом"
i = 0
while i in (0,1,2,3,4,5,6,7,8,9):
    # .....
    i += 1
print(i)



# Вычисление факториала числа "по-старинке" с помощью цикла while
x = int(input("Введите целое положительное число: "))
i = 1
fact = 1
while i <= x:
    fact *= i
#     print(str(i) + '! =', fact)
    i += 1
print('----------------------------------')
print(str(x) + '! =', fact)



# Вычисление факториала числа "по-новому" с помощью цикла for и итератора range()
x = int(input("Введите целое положительное число: "))
fact = 1
for i in range(1, x+1):
# for i in range(x): # Wrong! - range x починається з 0
    fact *= i
#     print(str(i) + '! =', fact)
print('----------------------------------')
print(str(x) + '! =', fact)




# Использование строк в качества объекта-итератора.
for char in 'Spam':
    print(char)


x = 123.556657
for ch in str(x):
    if ch.isdigit():
        print(ch)


x = int(input('Введите максимальное значение счётчика: '))
for i in range(x+1):
    #print(i)
    if i < 2:
        continue
    elif i > 5:
        break
    else:
        print(i)
# else:
if i == x:
    print('Достигли конца цикла нормальным путём (Else)')


def fun():
    print('Hello!')

f = fun
print(type(f), type(fun))
print(id(f), id(fun))
f()
fun()
print(f is fun)



def f():
    print('Simple function.')
f()
a = f()
print('Функция f() вернула', a)



# Пример функции с одним параметром
def f1(val):
    # тут Python выполняет va = переданное значение
    print('val =', val)

f1(35)



# Пример функции с несколькими параметрами параметром

def vector(x0, y0, x1, y1):
    x = x1 - x0
    y = y1 - y0
    
    print(
        '(' + str(x) + ',' + str(y) + ')', (x ** 2 + y ** 2) ** (1/2)
    )
        
        
vector(0, 0, 1, 1)
vector(1, 1, -1, -1)


# Пример функции с параметрами по-умолчанию

# def vector(x0 = 0, y0 = 0, x1, y1):
def vector(x1, y1, x0=0, y0=0):
    print()
    print('x1 =', x1,'x0 =', x0,'y1 =', y1,'y0 =', y0)
    x = x1 - x0
    y = y1 - y0
    
    print(
        '(' + str(x) + ',' + str(y) + ')', (x ** 2 + y ** 2) ** (1/2)
    )
        
vector(-1, -1)
vector(-1, -1, 0, 0)
vector(-1, -1, 1)
vector(-1, -1, y0=10)
vector(-1, -1, y0=10, x0=10)



# В этом примере в зависимости от того какой код раскомментарить
# мы получим разный результат или разные исключения. 
# Попробуйте это сделать самостоятельно.
#
#a = 5
#del a

def f(x, y):
    global a
    a = None
#     print('f:', a, x, y)
    a = x * y
        
a = 5
x = 10
y = 20
print('main', a, x, y)
f(5,6)
print('main', a, x, y)



# Пример функции с вычислением значения по-умолчанию

a = True



def f(val = a):
    print(val)

# Конкретное значение фактического параметра val
f(1)
# Фактический параметр отсутствует
f()
# Изменяем перемуннцю, которая используется для вычисления значения по-умолчанию для формального параметра val
a = False
# Фактический параметр отсутствует
f()




def multiply(x, y):
    return x * y

a = multiply(2, 8)
print(a)
print(multiply(2, 8.0))



def divide(x, y):
    if y == 0:
        return None
    else:
        return x / y
print(divide(5, 2))
print(divide(1, 0))


def divide(x, y):
    if y == 0:
        return
    elif isinstance(x, int) and isinstance(y, int):
        return x // y
    else:
        return x / y

    
print(divide(5, 2))
print(divide(5.0, 2))
print(divide(1, 0))



def divmod_(x, y):
    return x // y, x % y

print(divmod(3,2))
print(divmod_(3,2))
a, b = divmod_(3,2)
print(a, b)



def divide(x, y, printing=False):
    
    def print_result(val):
        if val is None:
            print('Деление на 0 запрещено!')
        else:
            print('Результат деления =', val)
    
    val = 'sdfsdfgsdfgsdgdf'
    if y == 0:
        result = None
    elif isinstance(x, int) and isinstance(y, int):
        result = x // y
    else:
        result = x / y
    if printing:
        print_result(result)
    return result


print(divide(5, 2))
divide(5, 2, True)
divide(5, 2, printing=True)
print(divide(1, 0))
divide(1, 0, True)



def divide(x, y, printing=False):
    
    def print_result(val):
        if printing:
            if val is None:
                print('Деление на 0 запрещено!')
            else:
                print('Результат деления =', val)

    if y == 0:
        result = None
    elif isinstance(x, int) and isinstance(y, int):
        result = x // y
        print_result(result)
    else:
        result = x / y
        print_result(result)
    return result

printing = True

print(divide(5, 2))
divide(5, 2, True)
divide(5, 2, printing=True)
print(divide(1, 0))
divide(1, 0, True)







