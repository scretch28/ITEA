# площа трикутника за формулою Герона
# s=sqrt(p*(p-a)*(p-b)*(p-c))
# де p=(a+b+c)/2
from math import sqrt
a=int(input("Enter side a:"))
b=int(input("Enter side b:"))
c=int(input('Enter side c:'))
p=(a+b+c)/2
print("p= ",p)
s=sqrt(p*(p-a)*(p-b)*(p-c))
print("Площа трикутника за формулою Герона s= ", s)


