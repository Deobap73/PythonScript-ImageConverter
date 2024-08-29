import os
from tkinter import Tk, Label, Button, filedialog, messagebox, Checkbutton, IntVar, ttk
from PIL import Image
import cv2
import numpy as np

# Function to remove the background using OpenCV's GrabCut
def remove_background_opencv(image_path):
    img = cv2.imread(image_path)
    mask = np.zeros(img.shape[:2], np.uint8)

    bgd_model = np.zeros((1, 65), np.float64)
    fgd_model = np.zeros((1, 65), np.float64)

    rect = (50, 50, img.shape[1] - 50, img.shape[0] - 50)
    cv2.grabCut(img, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    img = img * mask2[:, :, np.newaxis]

    img_rgba = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    img_rgba[:, :, 3] = mask2 * 255

    return img_rgba

# Function to adjust DPI
def adjust_dpi(image, dpi):
    width_inch, height_inch = image.size[0] / image.info['dpi'][0], image.size[1] / image.info['dpi'][1]
    new_size = (int(width_inch * dpi), int(height_inch * dpi))
    return image.resize(new_size, Image.ANTIALIAS), dpi

# GUI Application
class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Converter")

        # Set the minimum size of the window
        self.root.geometry("300x400")  # Set default size
        self.root.minsize(500, 400)  # Minimum width and height
        
        # Set the background color of the window
        self.root.configure(bg="#f0f0f0")  # Light gray background

        # Title label with background and foreground color
        self.label_title = Label(root, text="Image Converter", font=("Arial", 16), bg="#f0f0f0", fg="#333333")
        self.label_title.pack(pady=10)

        # Buttons with custom colors
        self.btn_input_folder = Button(root, text="Select Input Folder", command=self.select_input_folder, bg="#007BFF", fg="white")
        self.btn_input_folder.pack(pady=5)

        self.btn_output_folder = Button(root, text="Select Output Folder", command=self.select_output_folder, bg="#007BFF", fg="white")
        self.btn_output_folder.pack(pady=5)

        # Labels and combo boxes with background and foreground color
        self.label_format = Label(root, text="Choose Output Format:", bg="#f0f0f0", fg="#333333")
        self.label_format.pack(pady=5)

        self.combo_format = ttk.Combobox(root, values=["PNG", "JPEG", "WEBP", "BMP"], state="readonly")
        self.combo_format.current(0)
        self.combo_format.pack(pady=5)

        self.label_dpi = Label(root, text="Set Output DPI (Pixels/Inch):", bg="#f0f0f0", fg="#333333")
        self.label_dpi.pack(pady=5)

        self.combo_dpi = ttk.Combobox(root, values=["72", "96", "150", "200", "300"], state="readonly")
        self.combo_dpi.current(4)
        self.combo_dpi.pack(pady=5)

        # Initialize the IntVar for Checkbutton
        self.remove_bg_var = IntVar(value=0)  # Set to 0 (not checked) by default
        self.check_remove_bg = Checkbutton(root, text="Remove Background", variable=self.remove_bg_var, bg="#f0f0f0", fg="#333333")
        self.check_remove_bg.pack(pady=5)

        self.btn_convert = Button(root, text="Convert Images", command=self.convert_images, bg="#28a745", fg="white")
        self.btn_convert.pack(pady=10)

        self.label_status = Label(root, text="", fg="green", bg="#f0f0f0")
        self.label_status.pack(pady=5)

        self.input_dir = ""
        self.output_dir = ""

    def select_input_folder(self):
        self.input_dir = filedialog.askdirectory(title="Select the input folder")
        if self.input_dir:
            self.label_status.config(text=f"Input folder selected: {self.input_dir}")

    def select_output_folder(self):
        self.output_dir = filedialog.askdirectory(title="Select the output folder")
        if self.output_dir:
            self.label_status.config(text=f"Output folder selected: {self.output_dir}")

    def convert_images(self):
        if not self.input_dir or not self.output_dir:
            messagebox.showerror("Error", "Please select both input and output folders.")
            return

        output_format = self.combo_format.get().lower()
        output_dpi = int(self.combo_dpi.get())
        remove_bg = self.remove_bg_var.get() == 1
        supported_formats = ('.jpg', '.jpeg', '.png', '.webp', '.bmp')

        for filename in os.listdir(self.input_dir):
            if filename.lower().endswith(supported_formats):
                img_path = os.path.join(self.input_dir, filename)

                try:
                    if filename.lower().endswith('.svg'):
                        messagebox.showwarning("Warning", f"Skipping {filename}: SVG is not supported by Pillow.")
                        continue

                    if remove_bg and output_format == "png":
                        img_rgba = remove_background_opencv(img_path)
                        output_file = f'{os.path.splitext(filename)[0]}.png'
                        output_path = os.path.join(self.output_dir, output_file)
                        cv2.imwrite(output_path, img_rgba)
                        self.label_status.config(text=f"Removed background and saved {filename} as {output_file}")

                    else:
                        with Image.open(img_path) as img:
                            file_base_name = os.path.splitext(filename)[0]
                            img, dpi = adjust_dpi(img, output_dpi)
                            output_file = f'{file_base_name}.{output_format}'
                            output_path = os.path.join(self.output_dir, output_file)
                            img.save(output_path, output_format.upper(), dpi=(dpi, dpi))
                            self.label_status.config(text=f"Converted {filename} to {output_file}")

                except Exception as e:
                    messagebox.showerror("Error", f"Error processing {filename}: {e}")

        messagebox.showinfo("Done", "Batch conversion complete!")

# Run the app
if __name__ == "__main__":
    root = Tk()
    app = ImageConverterApp(root)
    root.mainloop()