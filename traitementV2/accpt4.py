import csv
import matplotlib.pyplot as plt

plusoumoins = 20

def opencsv(file):
    with open(file, newline='') as csvfile:
        return [row for row in csv.DictReader(csvfile, delimiter=';')]
    
data = opencsv('vt-pt4only.txt')


for i in range (len(data)-plusoumoins):
    accel = (float(data[i+plusoumoins]['vitesse']) - float(data[i-plusoumoins]['vitesse'])) / (float(data[i+plusoumoins]['temps']) - float(data[i-plusoumoins]['temps']))*1000
    print(f'accel {i}:', accel)

    with open("accélaration pt4.csv", 'a', encoding='utf-8') as file:
        file.write('\n' + str(i) + ';' + str(accel))

    # plt.figure(plusoumoins,figsize=[16,9])
    # plt.xlim([-1,476])
    # plt.ylim([-3, 10])

    # plt.xlabel("Numéro de l'image", fontsize = 16)
    # plt.ylabel("Accélération (sans unité)", fontsize = 16)
    # plt.xticks([0,50,100,150,200,250,300,350,400,450],fontsize = 14)
    # plt.yticks([-3,0,10], fontsize = 14)
    
    # plt.plot([i],[accel], marker='o', linestyle='-', color='blue')

    # if i == 457-plusoumoins-4:
    #     print('saving')
    #     plt.savefig(f'acceleration/accel±{plusoumoins}.png')
    #     plt.clf