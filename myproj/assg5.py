#python program to find the simple and compound interest
p=int(input("enter principle amount\n"))
t=int(input("enter time\n"))
r=float(input("enter the rate of interest\n"))
si=float((p*t*r)/100)
ci=float(p*((1+r/100))**t)
print("simple interest is: {} and compound intrest is:{}".format(si,ci))