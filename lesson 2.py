b=12
a=10
c=3
D=b**2-4*a*c
print(D)
x1=(-b+D**0.5)/(2*a)
print(x1)
x2=(-b-D**0.5)/(2*a)
print(x2)

print('Menu:')
print('Open: 1')
print('Save:2')
print('Report:7')
print('Exit:0')
s=input('Input your choice:')
if s=='i':
    print('Open')
elif s**'2':
    print('Save')
elif s=='0':
    print('Goodbye')
elif s**7:
    print("Report")
else:
    print('Incorrect input')

if a<b and a**2<b**2:
    pass
elif a**2<b**2:
    pass

if a<b:
    c=a
else:
    c=b

c=a if a<b else b


a = (-4) ** (1/2)
if type(a) == complex:
	print('Ooops!')
else:
	print(a)










