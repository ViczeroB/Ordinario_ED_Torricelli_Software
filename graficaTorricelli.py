import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

H = 0.3  # Altura del cono (metros)
R_T = 0.15  # Radio superior del cono (metros)
R_B = 0.05  # Radio inferior del cono (metros)
R_A = 0.01  # Radio del agujero de drenaje (metros)
g = 9.81  # Aceleración gravitatoria (m/s^2)

# Área del agujero
A = np.pi * R_A ** 2

# Función de la ley de Torricelli t(h)
def t_h(h):
    M = (R_T - R_B) / H
    B = np.sqrt(2 * g)
    C = fsolve(lambda c: (np.pi * M / B) * (2/5 * H ** (5/2)) + (2 * np.pi * R_B / B) * (2/3 * H ** (3/2)) - c, 0)
    return (np.pi * M / B) * (2/5 * h ** (5/2)) + (2 * np.pi * R_B / B) * (2/3 * h ** (3/2)) - C

# Generando valores de h
h_values = np.linspace(0, H, 100)

# Calculando valores de t(h)
t_values = t_h(h_values)

# Asegurándonos de que los valores de tiempo sean no negativos
t_values = np.abs(t_values)

# Graficando t(h)
plt.plot(t_values, h_values)
plt.xlabel('Tiempo (s)')
plt.ylabel('Altura del agua (m)')
plt.title('Ley de Torricelli')
plt.grid(True)
plt.show()



