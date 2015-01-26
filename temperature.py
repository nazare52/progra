print ("what is the temperature in Fahrenheit?")
t = int(input())
c = int(5*((t-32)/9))
sentence = "a temperature of {} degrees Fahrenheit is {} degrees in Celsius.".format(t,c)
print (sentence)
if (c>=100):
 print ("water boils at this temperature at sea level.")
elif (c<0):
 print ("at this temperature water is ice.")
else:
 print ("water does not boil at this temperature at sea level.")