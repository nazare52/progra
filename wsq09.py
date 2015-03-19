# Sergio Andrade Nieves
while True:
 n = int(input("enter a non-negative integer: "))
 while n < 0:
  n = int(input("please enter a positive number: "))
 f = 0
 c = 1
 while f < n:
  f += 1
  c = c*f
 print (n,"!=",c)
 yes = set(['yes','y', 'ye', ''])
 no = set(['no','n'])
 print ("want to enter another number?{y,n}")
 q = input()
 while True:
  if q in yes:
   break
  elif q in no:
   break
  else:
   print ("please enter yes or no")
   q = input()
 if q in yes:
  print ("fine")
 elif q in no:
  print ("have a nice day.")
  break