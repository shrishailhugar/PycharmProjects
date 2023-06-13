n=int(input("enter a number"))
s=n%2
if(s==0):
    print("even")
    if n>5:
        print("greater")
    else:
        print("small")
else:
    print("odd")