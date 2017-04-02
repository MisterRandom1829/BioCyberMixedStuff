# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/mateusz/.spyder2/.temp.py
"""

import numpy as np
import matplotlib.pyplot as plt

### proposal of model with grass
alfa = 2
beta = 0.1
gamma = 0.005
delta = 0.1
epsilon = 0.005
dzeta = 0.2
eta = 0.003


def simulation(_alfa, _beta, _gamma, _delta, _epsilon, _dzeta, _eta):
    G = []
    Z = []
    W = []
    
    G.append(100)
    Z.append(100)
    #W.append(100)
    W.append(0)
    time = 10000

    for i in range(time):
        G.append(G[i] * _alfa / (1 + _eta * G[i]) - _beta * Z[i])
        Z.append((_gamma * G[i]) * Z[i] - _delta * W[i])
    #W.append(W[i]*(epsilon*Z[i]-dzeta))
        W.append(0)
        if Z[i+1]<=0:# or W[i+1]<=0:
            break
    
    Ret = [G, Z]
 #   print Ret    
    
    return Ret
step = np.arange(0., 5., .01)
step = np.round(step, 2)
#print step
alfa = .0
T = []
for i in range (500):
    T.append(simulation(step[i], beta, gamma, delta, epsilon, dzeta, eta))
   
S = []   
Bif = []
#print len(T[200][0])
#print T[200][0][0]
#print len(T)
for x in range(len(T)):
       
    for g in range (len(T[x][0])):
        if (not(g == 0 or g == len(T[x][0]) or g == len(T[x][0]) - 1)):
            if (T[x][0][g] >= 0 and T[x][0][g] <= T[x][0][g-1] and T[x][0][g] <= T[x][0][g+1]):
                
               # P.append(T[x][0][g])
                Bif.append(T[x][0][g])
                S.append(step[x])
        #break



#print Bif[100][1]
#aaa = Bif[0:-1][0]
#print aaa
plt.plot(S, Bif)



'''
ranMax = 1000
ranMin = 0
grass, = plt.plot(G[ranMin:ranMax], label='Grass')
prey, = plt.plot(Z[ranMin:ranMax], label='Rabbits')
#predator, = plt.plot(W[ranMin:ranMax], label='Predator')
plt.legend(handles=[grass, prey])
plt.show()
'''








