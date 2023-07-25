import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

image_path = "cameratransform/google.png"

from scipy.ndimage import map_coordinates

def simulate_top_view(image_path, inclination=0, rotation=0):
    # Charger l'image
    img = mpimg.imread(image_path)

    # Dimensions de l'image
    height, width, _ = img.shape

    # Créer une grille d'indices pour les pixels de l'image
    y, x = np.indices((height, width))

    # Convertir les coordonnées x, y en coordonnées polaires
    r = np.sqrt((x - width / 2) ** 2 + (y - height / 2) ** 2)
    theta = np.arctan2(y - height / 2, x - width / 2)

    # Ajuster l'inclinaison et la rotation
    r_adjusted = r * np.cos(np.deg2rad(inclination))
    theta_adjusted = theta + np.deg2rad(rotation)

    # Convertir les coordonnées polaires ajustées en coordonnées cartésiennes
    x_adjusted = width / 2 + r_adjusted * np.cos(theta_adjusted)
    y_adjusted = height / 2 + r_adjusted * np.sin(theta_adjusted)

    # Interpolation bilinéaire pour obtenir les nouvelles valeurs de pixel
    coordinates = np.vstack((y_adjusted.flatten(), x_adjusted.flatten()))
    simulated_img = np.zeros_like(img)
    for c in range(3):  # Canal de couleur (R, G, B)
        simulated_img[:, :, c] = map_coordinates(img[:, :, c], coordinates, order=1).reshape(img.shape[:2])

    return simulated_img

# Chemin vers votre image

# Paramètres de simulation (inclinaison et rotation en degrés)
inclination_degrees = 30
rotation_degrees = 45

# Simulation de la vue de dessus avec les paramètres donnés
simulated_image = simulate_top_view(image_path, inclination=inclination_degrees, rotation=rotation_degrees)

# Afficher l'image originale et l'image simulée côte à côte
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(mpimg.imread(image_path))
axes[0].set_title("Image originale")
axes[0].axis("off")

axes[1].imshow(simulated_image)
axes[1].set_title("Vue de dessus simulée")
axes[1].axis("off")

plt.show()