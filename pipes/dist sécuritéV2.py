import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# vt = 1.25  # 4,5 km/h
Umin = 1  # vitesse m/s
Umax = 36  # environ 130 km/h
Wm = 4.23  # longueur du véhicule en m (moyenne française)
t = np.linspace(0, 15, 400)

def vitesse(t):
    a = np.where(t <= 10, (Umax - Umin) / 10, - (Umax - Umin) / 10)
    vt = np.where(t <= 10, Umin + a * t, Umax + 2 * a * (t - 10))
    # print('vt: ', vt)
    return vt


def security(t):
    vt = np.linspace(1, 36, 400)
    # ici la vitesse est encore en m/s
    miles_per_meter = 0.000621371
    seconds_per_hour = 3600
    vt = vt * miles_per_meter * seconds_per_hour
    dist = Wm * (1 + (vt/(16.1/3.6)))
    # print(dist)
    return dist


fig, ax1 = plt.subplots(figsize=[16, 9])
ax1.set_xlim([-1, 16])
ax1.set_xlabel('Temps (s)', fontsize = 16)
ax1.set_ylabel('Distance de sécurité en m', color='b', fontsize = 16)
ax1.plot(t, security(t), label='Distance de sécurité', color='b')
ax1.tick_params(axis='y', labelcolor='blue', labelsize = 14)
ax1.tick_params(axis='x', labelcolor='black', labelsize = 14)

ax2 = ax1.twinx()
ax2.set_ylabel('Vitesse de la voiture leader en m/s', color='r', fontsize = 16)
vitesse_data = np.linspace(1, 36, 400)
ax2.plot(t, vitesse_data, label='Vitesse de la voiture leader', color='r')
ax2.tick_params(axis='y', labelcolor='r', labelsize = 14)


ax1.set_ylim(-1, 100)
ax2.set_ylim(-1, 100)

ax1.yaxis.set_major_locator(ticker.LinearLocator(numticks=10))
ax2.yaxis.set_major_locator(ticker.LinearLocator(numticks=10))

# plt.title(label='Variation de la distance de sécurité en fonction de la vitesse du leader selon le modèle de Pipes', fontsize= 16)
fig.legend(loc='upper center', fontsize = 16)
plt.savefig('pipes/dist sécuritésV2.png')
plt.draw()
plt.pause(1)