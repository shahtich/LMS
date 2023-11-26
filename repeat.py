"""def c(a, b):
   c.mul = c.mul + b
   if ((c.mul % a == 0) and (c.mul % b == 0)):
       return c.mul
   else:
       c(a, b)
   return c.mul
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c.mul = 0
if (a > b):
   k1 = c(b, a)
else:
   k1 = c(a, b)
print("Наименьшее общее кратное:")
print(k1)

"""
"""def mass(A):
    A=[]
    n=int(input('Ввeдите число: '))
    for i in range(1, n+1):
        A.append(i)
    return A
A=[]
A=mass(A)
print(A)
for a in A:
    if a >= 1:
        for i in range(2, int(a**0.5) + 1):
            if a%i==0:
                break
        else:
            print(a)
"""
"""n=int(input('Введите число: '))
for i in range(1, n+1):
    if n%i==0:
        print('Делители этого числа: ', i)"""