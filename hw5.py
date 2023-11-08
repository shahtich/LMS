'''n=int(input())
A=[input()for i in range(n)]
B=[]
print(A)
for i in A:
    if A.count(i)>1:
        B.append(i)
print(len(B))'''

'''text=input()
chars = list(text)
if chars[0].isalpha():
    chars[0]=chars[0].upper()
    print(chars)
for i in range(len(text)):
    if (chars[i-1] in ['. ','! ','? ']) and chars[i].isalpha():
        chars[i]=chars[i].upper()
print(chars)

'''
def capitalize_text(text):
    capitalized_text = ""
    capitalize_next = True
    for i in range(len(text)):
            if text[i].isalpha():
                if capitalize_next:
                    capitalized_text += text[i].upper()
                    capitalize_next = False
                else:
                    capitalized_text += text[i].lower()
            else:
                capitalized_text += text[i]
                if text[i] in [".", "!", "?"]:
                    capitalize_next = True
    return capitalized_text
text = input()
capitalized_text = capitalize_text(text)
print(capitalized_text)