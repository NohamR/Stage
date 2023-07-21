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
plt.xlabel('distance w  en m')
plt.ylabel('vitesse en m.s-¹')
plt.plot(ww, phi(ww))
plt.savefig('test/phi(www).png')
plt.draw()  
plt.pause(10)