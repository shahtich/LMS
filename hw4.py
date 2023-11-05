'''
input_string = input("Введите строку: ")
words = input_string.split()
words.reverse()
print(words)
''''''
print(input()[::2])
''''''
numbers = input("Введите список чисел через пробел: ")
number_list = numbers.split()
number_list = [int(x) for x in number_list]
n = int(input("Введите степень: "))
result = [x ** n for x in number_list]
print(result)
''''''
text = input("Введите текст: ") 
symbol = input("Введите символ: ")  
new_text = text.replace(symbol, symbol * 2)
print("Новый текст:", new_text)
''''''
string = "[xaxaxaxaxaxaxyxyxyxyyxyayxayxyaxyaxy]"
count_x = string.count('x')
count_y = string.count('y')
print(f'x: {count_x}, y: {count_y}')
'''
text = input("Введите текст со скобками: ")  
result = ""  
start = text.find("(") 
while start != -1: 
    end = text.find(")", start) 
    if end != -1: 
        result += text[start + 1: end] + "n"  
    else:  
        break  
    start = text.find("(", end)
print(result)  