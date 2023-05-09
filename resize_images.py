import os
from PIL import Image, UnidentifiedImageError

def resize_image(image_path, max_size):
    try:
        img = Image.open(image_path)
    except UnidentifiedImageError:
        print(f"Skipping non-image file: {image_path}")
        return

    img_size = os.path.getsize(image_path)

    if img_size > max_size:
        ratio = (max_size / img_size) ** 0.5
        new_width = int(img.width * ratio)
        new_height = int(img.height * ratio)

        img_resized = img.resize((new_width, new_height), Image.ANTIALIAS)
        img_resized.save(image_path, format=img.format, quality=95)

def resize_images_in_folder(folder_path, max_size):
    for root, _, files in os.walk(folder_path):
        for file in files:
            image_path = os.path.join(root, file)
            resize_image(image_path, max_size)

if __name__ == "__main__":
    folder_path = input("Enter the folder path containing the images: ").strip()
    max_size = 0.25 * 1024 * 1024  # 0.25 MB in bytes

    resize_images_in_folder(folder_path, max_size)
    print("Images resized successfully.")
