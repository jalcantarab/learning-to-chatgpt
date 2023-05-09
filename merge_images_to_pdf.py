import os
import sys
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def is_image_file(filename):
    try:
        Image.open(filename)
        return True
    except IOError:
        return False

def merge_images_to_pdf(input_folder, output_filename):
    # Get a list of all files in the input folder
    file_list = os.listdir(input_folder)

    # Filter the list to include only image files
    image_files = [os.path.join(input_folder, f) for f in file_list if is_image_file(os.path.join(input_folder, f))]

    # Create a PDF canvas to draw the images on
    c = canvas.Canvas(output_filename, pagesize=letter)

    for image_file in image_files:
        # Open the image file
        img = Image.open(image_file)

        # Set the dimensions for the image to be placed on the PDF
        img_width, img_height = img.size
        page_width, page_height = letter

        # Calculate the scale factor to fit the image within the page
        scale_factor = min(page_width / img_width, page_height / img_height)

        # Calculate the new image dimensions
        new_width = img_width * scale_factor
        new_height = img_height * scale_factor

        # Calculate the position for the image to be centered on the page
        x_pos = (page_width - new_width) / 2
        y_pos = (page_height - new_height) / 2

        # Draw the image on the PDF canvas
        c.drawImage(image_file, x_pos, y_pos, new_width, new_height)

        # Move to the next page
        c.showPage()

    # Save the PDF
    c.save()

if __name__ == "__main__":
    input_folder = sys.argv[1]  # Path to the folder containing the images
    output_filename = sys.argv[2]  # Output PDF filename

    merge_images_to_pdf(input_folder, output_filename)
