#Sergio Andrade Nieves
def intostr(a):
 a = str(a)
 a = a1[::-1]
 a = int(a)
 return a

def palin(a):
 if a == intostr(a):
  return (1)
 else:
  return (0)

def nopalin(a):
 c = 0
 while c < 30:
  a1 = a
  a2 = intostr(a)
  a3 = a1+a2
  a4 = intostr(a3)
  if a3 == a4:
   return (1)
   break
  elif a3 != a4:
   a = a3
   c += 1
  if c >= 30:
   return 0
print ("search for palindromes")
x = int(input("from: "))
y = int(input("to: "))+1
n = x
c = 0
np = 0
p = 0
l = 0
print ("------")
for t in range (x,y):
 e = palin(n)
 w = nopalin(n)
 c += 1
 if e == 1:
  p += 1
 elif w == 1:
  np += 1
 elif w != 1:
  l += 1
  print ("lychrel number detected: ",n)
 n += 1
print ("------")
print ("numbers revised:",c)
print ("natural palindromes found:",p)
print ("non-lychrels:",np)
print ("lychrel candidates:",l)