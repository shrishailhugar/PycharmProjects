n=int(input("enter value of n\n"))
m=int(input("enter value of m\n"))
for i in range(n,m+1):
    k=2
    while k<=i/2:
        if i%k==0:
            break
        k=k+1
    else:
         print(" the {} value is prime".format(i))