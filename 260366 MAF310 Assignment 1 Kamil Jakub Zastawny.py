# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 12:34:26 2024

@author: kamza
"""

import numpy as np
#OPPGAVE 1

#konstruerer matrisen
A1 = np.array([[-8, 4, 0, 0, 0],
             [8, -10, 2, 0, 0],
             [0, 6, -11, 5, 0],
             [0, 0, 3, -7, 4],
             [0, 0, 0, 2, -4]], float)

#konstruerer output
B1 = np.array([-80, 0, 0, 0, -30], float)

# solving for A and B
C1 = np.linalg.solve(A1, B1)

#printing results
for index, value in enumerate(C1):
    print(f"Konsentrasjonen i tank {index} er {value:.2f}")

#OPPGAVE 2

#konstruerer matrisen
A2 = np.array([[-6, 4, 0, 0],
               [0, -7, 3, -4],
               [4, 0, -4, 0],
               [2, 0, 1, -4]])

#OPPGAVE 3
from matplotlib import pyplot as plt

#konstruerer datasett
h = [0, 1.525, 3.050, 4.575, 6.10, 7.625, 9.150]
p = [1, 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741]

plt.plot(h,p,'x')
coefficients = np.polyfit(h,p,2)
print(f"Coefficients: {coefficients}")

xfit = np.linspace(0,10,100)
yfit = np.polyval(coefficients, xfit)
plt.plot(h, p, 'x')
plt.plot(xfit, yfit)