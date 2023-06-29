import math

x = int(input("x? "))
y = int(input("y? "))
z = int(input("z? "))

eq1 = math.pow(x*x+y*y+z*z,1/3)
eq2 = math.pow(x,y) + math.pow(y,x)
eq3 = math.sin(math.pow(x,2) + math.pow(y,2)) + math.cos(math.pow(y,2) + math.pow(z,2))
eq4 = math.pow(math.log(x) + math.log(y)+math.log(z),x+y+z)

print('({0}^2 + {1}^2 + {2}^2)^1/3 = {3}'.format(x,y,z,eq1))
print('{0}^{1} + {2}^{3} = {4}'.format(x,y,y,z,eq2))
print('cos({0}^2 + {1}^2) + sin({2}^2 + {3}^2) = {4}'.format(y,z,x,y,eq3))
print('(log {0} + log {1} + log {2}) ^ ({0} + {1} + {2}) = {3}'.format(x,y,z,eq4))
