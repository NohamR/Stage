import csv
import matplotlib.pyplot as plt

# plusoumoins = 6

def opencsv(file):
    with open(file, newline='') as csvfile:
        return [row for row in csv.DictReader(csvfile, delimiter=';')]
    
data = opencsv('pt4only.txt')

def tester(plusoumoins):
    for i in range (len(data)-plusoumoins):

        ##corection des points manquants
        if i <plusoumoins:
            vitesse = -(float(data[i+1]['distance']) - float(data[i-1]['distance'])) / (float(data[i+1]['temps']) - float(data[i-1]['temps']))
            if vitesse>0.05 or vitesse<-0.05:
                vitesse=0
        else :
            vitesse = -(float(data[i+plusoumoins]['distance']) - float(data[i-plusoumoins]['distance'])) / (float(data[i+plusoumoins]['temps']) - float(data[i-plusoumoins]['temps']))
        print(f'vitesse {i}:', vitesse)

        plt.figure(plusoumoins,figsize=[16,9])
        plt.xlim([-1,476])
        plt.ylim([-0.3, 1])
        plt.xlabel("Numéro de l'image", fontsize = 16)
        plt.ylabel("Vitesse (sans unité)", fontsize = 16)
        plt.xticks([0,50,100,150,200,250,300,350,400,450,500],fontsize = 14)
        # plt.yticks([-0.3,0,1], fontsize = 14)
        plt.yticks([i/100 for i in range(-30, 100, 5)], fontsize = 14)

        plt.plot([i],[vitesse], marker='o', linestyle='-', color='blue')

        if i == 474-plusoumoins:
            plt.savefig(f'vitesse/vitesse±{plusoumoins}.png')
            plt.clf
        
        # with open("vt-pt4only.txt", 'a', encoding='utf-8') as file:
        #     file.write('\n' + str(i) + ';' + str(vitesse))

tester(21)