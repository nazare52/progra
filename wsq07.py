# SERGIO ANDRADE NIEVES
x = int(input("low: "))
y = int(input("high: "))
z = 0
if x > y:
 x,y = y,x
while x != y:
 z = z+x
 x += 1
 print (z)
print (z+y)