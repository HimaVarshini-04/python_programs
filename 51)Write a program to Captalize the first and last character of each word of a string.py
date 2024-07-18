str1=input()
str2= ""
for word in str1.split():
    str=word[0].upper() + word[1:-1] + word[-1].upper()
    str2+= str+ " "
print(str2)
