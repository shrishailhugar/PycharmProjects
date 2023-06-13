#swap two strings print in title form
print("enter two strings\n")
str1=input()
str2=input()
str1,str2=str2,str1
print(str1.title())
print(str2.title())