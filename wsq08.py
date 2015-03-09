# Sergio Andrade Nieves
def suma(a,b):
 return (a+b)
def resta(a,b):
 return (a-b)
def mult(a,b):
 return (a*b)
def division(a,b):
 return (a//b)
def rem(a,b):
 return (a%b)
a = int(input("first number: "))
b = int(input("second number: "))
print (a,"+",b,"=",suma(a,b))
print (a,"-",b,"=",resta(a,b))
print (a,"*",b,"=",mult(a,b))
print (a,"//",b,"=",division(a,b))
print (a,"%",b,"=",rem(a,b))