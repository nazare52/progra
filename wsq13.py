#Sergio Andrade Nieves
def babylonia(n):
 r = n/2
 s = 0
 n2 = 0
 for t in range(10):
  s = (r+(n/r))/2
  r = s
 return (s)

f = babylonia(7)
print (f)
print (f*f)