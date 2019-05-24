# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mlp
import cmath 
import math
import random

#definindo as duas possíveis séries de acordo com o módulo de 5
def absLower(n, z):
    value = (((-1)**n)*(z**n))/((5)**(n+1))
    return value

def absUpper(n, z):
    if n > 0:
        value = (-1*(((-1)**n)*((5)**(n-1))))/(z**n)
        return value


#inicializando o variável que irá guardar f(z)
sum_laurent = 0
#número de zs para testar
z_test = 2000
#número de interações
epochs = 200
#array para guardar a parte img
z_img = []
#array para guardar a parte real
z_real = []
fz_img = []
fz_real = []
ep = []#for para escolher um z e calcular o fz respectivo
for j in range(0, z_test):
    
    img = random.randrange(-10, 10, 1)
    real = random.randrange(-2, 2, 1)
    
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
    print('|z|: ', abs(z))
    print('f(z) = ', sum_laurent)
    print('=======================')
    if abs(z) != 5 :
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
ax = fig.add_subplot(111, projection='3d')
ax.scatter(ep, fz_real, fz_img)
ax.set_xlabel('Interações')
ax.set_ylabel('Real')
ax.set_zlabel('Img')
plt.show()

