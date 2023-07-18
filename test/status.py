from colour import Color

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

print(gradient)
