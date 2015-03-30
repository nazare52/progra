#Sergio Andrade Nieves
def rem(a,b):
 return a%b
def gcd(a,b):
 if a < b:
  a,b = b,a
 a1 = 0
 while True:
  a1 = rem(a,b)
  if a1 == 0:
   return b
   break
  else:
   a = b
   b = a1
x = int(input())
y = int(input())
z = gcd(x,y)
print (z)