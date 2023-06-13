import cmath as c
a=complex(input("enter a first complex number\n"))
b=complex(input("enter a second complex number\n"))
d=complex(a*b)
print("multiplication of {} and {} in polar form is {}".format(a,b,c.polar(d)))