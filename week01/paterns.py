#Quadratic equation
a=int(input())
b=int(input())
c=int(input())

d_d = b**2-(4*a*c) #Assigning variables to make the program simpler
d = d_d**(1/2)  #Root of b square -4ac
sol1 = ((-b)+d)/(2*a)
sol2 = ((-b)-d)/(2*a)

if d_d < 0:
   print('Solution exists in complex numbers')

#Return the solution if it exists in real numbers)
else:
   print('x = {0} or x = {1}'.format(sol1,sol2))