from PIL import Image
import os
import shutil

try:os.remove('gipps/merged.png')
except:pass

def merge_images(overlay_folder, output_path):
    overlay_path = f"{overlay_folder}/1.png"
    overlay = Image.open(overlay_path)
    result_width, result_height = overlay.size
    result = Image.new('RGB', (result_width, result_height), color=(255, 255, 255))
    x, y = 0, 0
    for i in range(1,40):
        overlay_path = f"{overlay_folder}/{i}.png"
        overlay = Image.open(overlay_path)
        result.paste(overlay, (x, y), overlay)
    result.save(output_path)

def detrf(folder_path):
    try:
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            print(f"Folder '{folder_path}' successfully deleted.")
        else:
            print(f"Folder '{folder_path}' does not exist.")

        try:
            os.makedirs(folder_path)
            print(f"Folder '{folder_path}' successfully created.")
        except OSError as e:
            print(f"Error creating folder: {e}")

    except OSError as e:
        print(f"Error deleting folder: {e}")

def merge():
    overlay_folder = "gipps/result"
    output_path = "gipps/merged.png"
    merge_images(overlay_folder, output_path)
    detrf('gipps/result')
    print('merge done')