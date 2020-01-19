a=12<3
b=12>3
c=bool(8)
print(a,b,c)

a=11 input('enter the number: ')
b=int(a)/5
d=int(a)//5

print('result=', b,d)
print(type(a), type(b), type(d))

a=1 #float(input('a= '))
b=1 #float(input('b= '))
if a>b:
    print('Ab')
else:
    print('aB')

a=[1,2,3]
i=0 #counter
while i<3:
    print(a[i])
    i+=1
i+=2
print('Finish',i)

a=[1,2,3]
for x in a:
    print(x)

x+=5
print('Finish', x)

a=7.0
print(isinstance(a,float)) #проверка, есть ли а типом fload или другим указанньім
print(type(a)==int)

a=1
b=1
print(a is b, a==b)
a=4327
b=432
print(id(a),id(b))
print(a is b, a==b)




