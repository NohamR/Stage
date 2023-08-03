import matplotlib.pyplot as plt
from colour import Color

def rainbow_gradient(num_colors):
    colors = []
    gradient = list(Color("violet").range_to(Color("red"), num_colors))
    for color in gradient:
        colors.append(color.hex_l)
    return colors

framenb = 1

keyvalues = []

with open('traitementV2/distance.txt', 'r') as f:
    lignes = f.readlines()
    for ligne in lignes:
        line = eval(ligne)

        allkeys = list(line.keys())
        allkeys.sort()
        linedict = {i: line[i] for i in allkeys}
        
        linedict = {cle: valeur for cle, valeur in linedict.items() if valeur >= 0}

        for key, value in linedict.items():
            if key not in keyvalues:
                keyvalues.append(key)

keypositions = {}

for key, i in zip(keyvalues, range(1, len(keyvalues)+1)):
    keypositions[key] = i
print('keypositions: ', keypositions)
colors = rainbow_gradient(len(keypositions)+1)

with open('traitementV2/distance.txt', 'r') as f:
    lignes = f.readlines()
    for ligne in lignes:
        line = eval(ligne)

        allkeys = list(line.keys())
        allkeys.sort()
        linedict = {i: line[i] for i in allkeys}
        
        linedict = {cle: valeur for cle, valeur in linedict.items() if valeur >= 0}     

        plt.figure(1,figsize=[16,9])
        plt.xlim([-1,780])
        plt.ylim([-20, 150])

        plt.grid()

        nb = 0

        for key, value in linedict.items():
            if key == 13:
                # print('value: ', value)
                # print(framenb)
                with open("traitementV2/pt13.txt", 'a', encoding='utf-8') as file:
                    file.write('\n' + str(framenb) + ';' + str(value))

                plt.plot([framenb],[value], marker='o', linestyle='-', color=colors[keypositions[key]])       # , color=colors[key]

            nb += 1

        # plt.draw()
        # plt.pause(0.0001)
        if framenb == 780:
            plt.savefig(f'traitementV2/{framenb}.png')
        framenb += 1
        # plt.clf()