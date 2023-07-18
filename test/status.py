from colour import Color
import matplotlib.pyplot as plt

def rainbow_gradient(distances):
    num_colors = len(distances)
    colors = []
    base_color = Color("green")
    target_color = Color("red")
    
    luminance_start = base_color.get_luminance()
    luminance_end = target_color.get_luminance()
    
    for i in range(num_colors):
        moydist = distances[i]
        t = i / (num_colors - 1)  # Interpolation paramètre t
        
        adjusted_luminance = luminance_start + (luminance_end - luminance_start) * (1 - t) * (moydist - 1) / 18
        color = Color(rgb=(base_color.rgb[0] * (1 - t) + target_color.rgb[0] * t,
                           base_color.rgb[1] * (1 - t) + target_color.rgb[1] * t,
                           base_color.rgb[2] * (1 - t) + target_color.rgb[2] * t))
        color.set_luminance(adjusted_luminance)
        
        hex_code = color.hex_l
        colors.append(hex_code)
    
    return colors

distances = [0.05263158, 0.05263158, 0.05263158, 0.05263158, 0.05263158,
             0.05263158, 0.05263158, 0.05263158, 0.05263158, 0.05263158,
             0.05263158, 0.05263158, 0.05263158, 0.05263158, 0.05263158,
             0.05263158, 0.05263158, 0.05263158, 19.0]

gradient = rainbow_gradient(distances)

# Create a figure and axis
fig, ax = plt.subplots()

# Set the background color of the plot
fig.set_facecolor('white')

# Hide the axis labels
ax.set_axis_off()

# Calculate the width and height of each color patch
width = 1.0 / len(gradient)
height = 1.0

# Iterate through the colors and plot a rectangle for each
for i, color in enumerate(gradient):
    # Calculate the x-coordinate of the color patch
    x = i * width
    
    # Plot the color patch
    rect = plt.Rectangle((x, 0), width, height, facecolor=color)
    ax.add_patch(rect)

# Set the aspect ratio to 'auto' to ensure the patches are square
ax.set_aspect('auto')

# Set the limits of the x-axis
ax.set_xlim(0, 1)

# Display the plot
plt.show()

