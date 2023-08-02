import numpy as np
import matplotlib.pyplot as plt

U = 1.25 # vitesse m.s-¹
Wm = 0.3 # distance minimale entre la voiture et celle qui la précède m
Ws = 0.9 # m
ww = np.linspace(0, 10, 200)

def phi(ww):
    PHI = (U*(1 - np.exp(- (ww-Wm)/Ws)))
    return (ww >= Wm)* PHI

plt.figure(figsize=[16,9])
plt.xlabel('distance w  en m', fontsize = 16)
plt.ylabel('vitesse en m.s-¹', fontsize = 16)
plt.tick_params(labelsize = 14)
plt.plot(ww, phi(ww))
plt.savefig('test/phi(ww).png')
plt.draw()  
plt.pause(0.1)