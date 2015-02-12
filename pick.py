# sergio andrade nieves 
import random
x = random.randrange(1,101)
count = 0
print ("i am thinking in a number between 1 and 100.")
y = int(input("guess the number: "))
while y != x: 
 count += 1
 if y < x:
  low = "sorry but {} is too low, try again: ".format(y)
  y = int(input(low))
 elif y > x:
  high = "sorry but {} is too high, try again: ".format(y)
  y = int(input(high))
c = "correct! it is {}.".format(y)
print (c)
print ("you tried",count,"times")