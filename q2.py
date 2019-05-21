# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import cmath 
import math
import random

#definindo as duas possíveis séries de acordo com o módulo de z>2>1 ou 1<z<2
def absBetween(n, z):
    value = ((-1*(1/((2**(n+1)))))*(z**n)) - (1/(z**(n+1)))
    return value

def absUpper(n, z):
    value = (1/(z**(n+1)))*((2**n)-1)
    return value


#inicializando o variável que irá guardar f(z)
sum_laurent = 0
#número de zs para testar
z_test = 10
#número de interações
epochs  = input('Entre com o 1º valor: ')
#array para guardar a parte img
z_img = []
#array para guardar a parte real
z_real = []
fz = []
#for para escolher um z e calcular o fz respectivo
for j in range(0, z_test):
    
    img = random.randrange(-20, 20, 1)
    real = random.randrange(-10, 10, 1)
    
    z_img.append(img)
    z_real.append(real)
    
    z = complex(real, img)
    
    for interator in range(0,epochs):
        if abs(z) > 1 and abs(z) < 2:
            sum_laurent = absBetween(interator, z)            
        if abs(z) >2 and abs(z) > 1:
            sum_laurent = absUpper(interator, z)
    print('=======================')        
    print('Resultado:')        
    print('z = ', z)
    print('f(z) = ', sum_laurent)
    print('=======================')
    fz.append(sum_laurent)
    sum_laurent = 0
        
        
        
        
        
        
#gráfico para localizar cada ponto  

plt.scatter(z_real,z_img)
plt.xlabel('REAL')
plt.ylabel('IMG')
plt.show()

#gráfico para cada f(z)

plt.plot(fz, scalex = True)
plt.ylabel('F(Z)')
plt.xlabel('z_test')
plt.show()

