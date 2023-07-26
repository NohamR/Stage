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


coordonnees_xb = []
with open('traitement/distance_delrp.txt', 'r') as f:
    lignes = f.readlines()
    for ligne in lignes:
        line = eval(ligne)

        lenline = len(line)
        colors = rainbow_gradient(lenline)
        

        plt.figure(1,figsize=[16,9])
        plt.xlim([-1,150])
        plt.ylim([-0.5, 5])

        nb = 0
        for pos in line:
            plt.plot([0,pos],[nb, nb], marker='o', linestyle='-', color=colors[nb])
            nb += 1

        plt.draw()
        plt.pause(0.0001)
        plt.clf()
