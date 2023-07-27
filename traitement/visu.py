import matplotlib.pyplot as plt
from colour import Color

def rainbow_gradient(num_colors):
    colors = []
    base_color = Color("violet")
    gradient = list(base_color.range_to(Color("red"), num_colors))
    for color in gradient:
        hex_code = color.hex_l
        colors.append(hex_code)
    return colors

framenb = 1
coordonnees_xb = []
with open('traitement/distance.txt', 'r') as f:
    lignes = f.readlines()
    for ligne in lignes:
        line = eval(ligne)
        line = sorted(line)

        for element in line:
                if element < 0:
                    line.remove(element)
        
        if len(line) >= 4 :

            lendeline = len(line)
            
            while lendeline > 4:
                trop = line.pop()
                lendeline = len(line)

            plt.figure(1,figsize=[16,9])
            plt.xlim([-1,150])
            plt.ylim([-0.5, 5])

            colors = rainbow_gradient(len(line))
            nb = 0
            for pos in line:
                plt.plot([0,pos],[nb, nb], marker='o', linestyle='-', color=colors[nb])
                nb += 1

            plt.draw()
            plt.pause(0.0001)
            plt.savefig(f'traitement/vidresult/{framenb}.png')
            framenb += 1
            plt.clf()