'''
A=[1,2,3] 
B=[1,1,1] #заданные массивы
result=(list(map(lambda x,y:x+y,A,B))) #вводим функцию которая поочерёдно складывает элементы массива(с помощью функции map изменяем по каждому эл)
print(result)
'''
'''
S=[13,12,1,22,3232,12,12,144,296,0]
result=list((filter(lambda x: (x%12==0 or x%13==0),S)))
print (result)'''
"from functools import reduce"
A=[12,1,2,2,1,2,3232,0.1]
'''result=reduce(max,A)
print(result)'''
A=sorted(A)
print(A[0])
