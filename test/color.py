from colour import Color

def rainbow_gradient(num_colors):
    colors = []
    base_color = Color("red")
    gradient = list(base_color.range_to(Color("violet"), num_colors))
    for color in gradient:
        hex_code = color.hex_l
        colors.append(hex_code)
    return colors

num_colors = 10
gradient = rainbow_gradient(num_colors)

print(gradient)