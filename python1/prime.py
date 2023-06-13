n=int(input("enter the number\n"))
if n==1:
    print("nither prime nor composite\n")
else:
    k=2
    for k in range(2,n):
        if n%k==0:
            print("not prime\n")
            break
    else:
        print("its prime\n")