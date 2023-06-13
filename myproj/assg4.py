#python program days can be converted into yeras months remaining days
import math
day=int(input("enter number of days\n"))
year=divmod(day,365)
month=divmod(year[1],30)
days=month[1]
print("{} days can converted into {} year(s) {} month(s) and {} days".format(day,year[0],month[0],days))
