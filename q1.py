# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import cmath 
import math
import random

#definindo as duas possíveis séries de acordo com o módulo de 5
def absLower(n, z):
    value = (((-1)**n)*(z**n))/((5)**(n+1))
    return value

def absUpper(n, z):
    if n > 0:
        value = -1*(((-1)**n)*((5)**(n-1)))/(z**n)
        return value


#inicializando o variável que irá guardar f(z)
sum_laurent = 0
#número de zs para testar
z_test = 10
#número de interações
epochs = 3
#array para guardar a parte img
z_img = []
#array para guardar a parte real
z_real = []
fz_img = []
fz_real = []
ep = []#for para escolher um z e calcular o fz respectivo
for j in range(0, z_test):
    
    img = random.randrange(-20, 20, 1)
    real = random.randrange(-10, 10, 1)
    
    z_img.append(img)
    z_real.append(real)
    
    z = complex(real, img)
    
    for interator in range(0,epochs):
        if abs(z) > 5:
            sum_laurent = absUpper(interator, z)            
        if abs(z) < 5:
            sum_laurent = absLower(interator, z)
    print('=======================')        
    print('Resultado:')        
    print('z = ', z)
    print('f(z) = ', sum_laurent)
    print('=======================')
    fz_img.append(sum_laurent.imag)
    fz_real.append(sum_laurent.imag)
    ep.append(j)
    sum_laurent = 0
        
        
        
        
        
        
#gráfico para localizar cada ponto  

plt.scatter(z_real,z_img)
plt.xlabel('REAL')
plt.ylabel('IMG')
plt.show()

#gráfico para cada f(z)


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(ep, fz_real, fz_img, label='parametric curve')
ax.legend()
plt.show()

