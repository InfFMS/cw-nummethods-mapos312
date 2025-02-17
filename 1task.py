import numpy as np
import matplotlib.pyplot as plt

a = 0.1382
b = 3.19 * 10**-5
R = 8.314
tc = [-140, -130, -120, -110, -100]
tk = [T + 273.15 for T in tc]
V = np.linspace(b + 1*10**-5, 1*10**-3, 1000)
def findp(V, T, a, b, R):
    return (R*T/(V-b)) - (a/V**2)

plt.figure()
plt.xlabel('Объем, м^3/моль')
plt.ylabel('Давление, Па')

for T_kelvin in tk:
    P = findp(V, T_kelvin, a, b, R)
    if T_kelvin == max(tk):
        plt.plot(V, P, color='r', label=f'T = {T_kelvin - 273.15} °C')
    else:
        plt.plot(V, P, color='b', label=f'T = {T_kelvin - 273.15} °C')

plt.xscale('log')
plt.yscale('log')
plt.xlim(b + 1*10**-5, 1*10**-3)
plt.legend()
plt.grid(True)
plt.show()
#видим что при -100 по цельсию рафик без холмиков, закрашиваем его красным