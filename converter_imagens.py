from PIL import Image
import os
from tkinter import Tk, filedialog, simpledialog

# Function to get a directory from the user using a dialog
def get_directory(prompt):
    root = Tk()
    root.withdraw()  # Hide the main window
    path = filedialog.askdirectory(title=prompt)
    return path

# Prompt the user for the input and output directories
input_dir = get_directory('Select the input folder:')
output_dir = get_directory('Select the output folder:')

# List of supported input formats
supported_formats = ('.jpg', '.jpeg', '.png', '.webp', '.bmp', '.svg')

# Prompt the user for the desired output format
output_format = simpledialog.askstring("Output Format", "Choose the output format (PNG, JPEG, WEBP, BMP):").upper()
output_formats_supported = ['PNG', 'JPEG', 'WEBP', 'BMP']

# Check if the chosen format is valid
if output_format not in output_formats_supported:
    print(f"Invalid output format. Choose from: {', '.join(output_formats_supported)}")
    exit()

# Check if the output directory exists; if not, create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Iterate over all files in the input folder
for filename in os.listdir(input_dir):
    if filename.lower().endswith(supported_formats):  # Filter supported files
        img_path = os.path.join(input_dir, filename)

        try:
            # Handle SVG separately if necessary
            if filename.lower().endswith('.svg'):
                print(f'Skipping {filename}: SVG is not natively supported by Pillow.')
                continue  # Skip SVG files unless you want to convert them with another library

            # Open the image using Pillow
            with Image.open(img_path) as img:
                # Extract the base name of the file without the extension
                file_base_name = os.path.splitext(filename)[0]

                # Build the output path with the chosen format extension
                output_file = f'{file_base_name}.{output_format.lower()}'
                output_path = os.path.join(output_dir, output_file)

                # Convert and save the image in the specified format
                img.save(output_path, output_format)

                print(f'Converted {filename} to {output_file}')

        except Exception as e:
            print(f'Error processing {filename}: {e}')

print("Batch conversion complete!")