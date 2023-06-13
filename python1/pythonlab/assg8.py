#distance between two co-ordinates
import math as m
print("enter x co-ordinates\n")
x0=float(input())
x1=float(input())
print("enter y co-ordinates\n")
y0=float(input())
y1=float(input())
d=m.sqrt((x0-x1)**2+(y0-y1)**2);
print("the distance between ({},{}) and({},{}) is {}".format(x0,y0,x1,y1,d))