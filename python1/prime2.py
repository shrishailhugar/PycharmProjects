a=int(input("enter a number\n"))
if a==1:
    print("not prime and composite\n")
else:
     f=True
     i=2
     while i<=a/2:
         if a%i==0:
            f=False
            break
         i=i+1
     if f:
        print("{} is prime".format(a))
     else:
          print("{} not prime".format(a))
