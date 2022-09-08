import math

n = 10
x = [130, 650, 99, 150, 128, 302, 95, 945, 368, 961]
y = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]

xTotal = 0
yTotal = 0
xvy = 0


for i in range(n):
    xTotal = xTotal + x[i]
    yTotal = yTotal + y[i]
    xvy = xvy + x[i]*y[i]

a = xvy - (n * (xTotal/n) * (yTotal/n))

################################################################

xQuad = 0
yQuad = 0
for i in range(n):
    xQuad = xQuad + x[i]**2
    yQuad = yQuad + y[i]**2

b = xQuad - (n*((xTotal/n)**2))



# b1 = n * (xQuad-(xTotal*xTotal))
# b2 = n * (yQuad-(yTotal*yTotal))
# b = b1*b2
# b = math.sqrt(b) 


################################################################
print(yTotal)
print(yTotal*yTotal)
print(a)
print(b)
print(a/b)
