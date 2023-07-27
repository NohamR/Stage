import os
import cv2

def create_video_from_images(image_folder, output_video_path, fps=15):
    image_files = sorted([f for f in os.listdir(image_folder) if f.endswith('.png')])

    if not image_files:
        print("Aucune image .png")
        return

    image_path = os.path.join(image_folder, image_files[0])
    img = cv2.imread(image_path)
    height, width, _ = img.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        img = cv2.imread(image_path)
        video_writer.write(img)

    video_writer.release()
    print(f"Vidéo créée avec succès : {output_video_path}")

if __name__ == "__main__":
    input_image_folder = "traitement/vidresult"
    output_video_path = "traitement/video_sortie.mp4"

    create_video_from_images(input_image_folder, output_video_path)
