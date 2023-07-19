import numpy as np
import matplotlib.pyplot as plt

vt = 1.25  # 4,5 km/h
Umin = 1  # vitesse m/s
Umax = 36  # environ 130 km/h
Wm = 4.23  # longueur du véhicule en m (moyenne française)
t = np.linspace(0, 15, 400)

def vitesse(t):
    a = np.where(t <= 10, (Umax - Umin) / 10, - (Umax - Umin) / 10)
    vt = np.where(t <= 10, Umin + a * t, Umax + 2 * a * (t - 10))
    return vt


def security(t):
    vt = vitesse(t)
    dist = Wm * (1 + (vt/(16.1/3.6)))
    # print(dist)
    return dist

plt.figure(figsize=[16, 9])
plt.xlim([-1,16])
plt.xlabel('temps (s)')
plt.ylabel('distance de sécurité (m)')
plt.plot(t, security(t))
plt.savefig('pipes/dist sécurités.png')
plt.draw()
plt.pause(5)