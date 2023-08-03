import csv
import matplotlib.pyplot as plt

# plusoumoins = 6

def opencsv(file):
    with open(file, newline='') as csvfile:
        return [row for row in csv.DictReader(csvfile, delimiter=';')]
    
data = opencsv('traitementV2/pt13.txt')

def tester(plusoumoins):
    for i in range (len(data)-plusoumoins):
    # print(data[i+1]['temps'])
    # print(data[i-1]['temps'])
    # print(data[i+1]['distance'])
    # print(data[i-1]['distance'])
        vitesse = (float(data[i+plusoumoins]['distance']) - float(data[i-plusoumoins]['distance'])) / (float(data[i+plusoumoins]['temps']) - float(data[i-plusoumoins]['temps']))
        print(f'vitesse {i}:', -vitesse)

        plt.figure(plusoumoins,figsize=[16,9])
        plt.xlim([-1,476])
        plt.ylim([-1, 1])

        plt.plot([i],[-vitesse], marker='o', linestyle='-')
        # plt.show
        # plt.pause(0.00001)
        if i == 474-plusoumoins:
            plt.savefig(f'traitementV2/vitesse±{plusoumoins}.png')
            plt.clf

# for i in range(1, 20):
#     tester(i)

tester(100)