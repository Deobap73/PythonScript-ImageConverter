# Image Converter

<br>

## Overview

The Image Converter is a graphical application designed to convert image files from one format to another using a user-friendly interface. It supports various image formats and provides a convenient way to batch process images in a specified directory. This application utilizes Python and is designed to run on Windows.

<br> <br>

## Features

- **Batch Image Conversion:** Convert multiple images in a specified directory.
- **Format Support:** Supports conversion to common formats such as PNG, JPEG, WEBP, and BMP.
- **Flexible Input and Output:** Allows users to specify input and output directories and select the desired output format.
- **Background Removal:** Optional feature to remove backgrounds from images using OpenCV's GrabCut algorithm.
- **DPI Adjustment:** Adjusts the DPI (dots per inch) of the output images.
- **Error Handling:** Provides informative messages in case of errors during processing.

<br> <br>

## Requirements

- **Windows OS:** This application is designed for Windows.
- **Python 3.x:** Required to run the application.
- **Required Python Packages:** `Pillow`, `opencv-python`, `numpy`, `tkinter`

<br> <br>

## Installation

To set up the Image Converter, follow these steps:

1. **Clone the Repository:**

   - Clone the repository using the following command:
     ```bash
     git clone git@github.com:Deobap73/PythonScript-ImageConverter.git
     ```
   - Navigate to the cloned repository:
     ```bash
     cd PythonScript-ImageConverter
     ```

2. **Install Required Packages:**

   - Ensure you have Python 3.x installed. You can download it from the [official Python website](https://www.python.org/downloads/).
   - Install the required Python packages by running the following command:
     ```bash
     pip install pillow opencv-python numpy
     ```

3. **Prepare the Environment:**

   - **Run Command Prompt as Administrator:** This is necessary to ensure proper installation of packages and access rights. To do this:

     - Search for `cmd` or `Command Prompt` in the Start menu.
     - Right-click on `Command Prompt` and select `Run as administrator`.

   - **Ensure Python Scripts Directory is in PATH:**
     - Right-click on `This PC` or `Computer` on the desktop or in File Explorer.
     - Select `Properties`, then click on `Advanced system settings`.
     - In the `System Properties` window, click on the `Environment Variables` button.
     - In the `Environment Variables` window, find the `Path` variable under `System variables`, and click `Edit`.
     - Ensure that the path to the Python `Scripts` directory (e.g., `C:\Python39\Scripts`) is included. If not, click `New` and add the path.

HEAD
=======
   - **Ensure Python Scripts Directory is in PATH:**<br>
   - Right-click on `This PC` or `Computer` on the desktop or in File Explorer.
   - Select `Properties`, then click on `Advanced system settings`. <br> - In the `System Properties` window, click on the `Environment Variables` button.
   - In the `Environment Variables` window, find the `Path` variable under `System variables`, and click `Edit`.
   - Ensure that the path to the Python `Scripts` directory (e.g., `C:\Python39\Scripts`) is included. If not, click `New` and add the path.
     <br><br>

4. **Compile the Executable:**

   - Use PyInstaller to compile the script into an executable. Open Command Prompt as Administrator and run the following command:
     ```bash
     pyinstaller --onefile --hidden-import=tkinter --icon=icon.ico converter_imagens.py
     ```
   - The executable will be created in the `dist` folder within the project directory.

5. **Run the Executable:**
   - Navigate to the `dist` directory:
     ```bash
     cd dist
     ```
   - Double-click the `converter_imagens.exe` file or run it from the command prompt.

<br> <br>

## Usage

1. **Run the Executable:**

   - Double-click the `converter_imagens.exe` file or run it from the command prompt.

2. **Select Input Directory:**

   - Click on "Select Input Folder" to choose the folder containing the images you want to convert.

3. **Select Output Directory:**

   - Click on "Select Output Folder" to choose the folder where you want to save the converted images.

4. **Choose Output Format:**

   - Select the desired output format from the options provided: PNG, JPEG, WEBP, or BMP.

5. **Set Output DPI:**

   - Choose the DPI (Pixels/Inch) for the output images.

6. **Optional Background Removal:**

   - Check the "Remove Background" option if you want to remove the background from the images (available only for PNG format).

7. **Start Conversion:**

   - Click on "Convert Images" to process all images in the input directory, convert them to the specified format, and save them in the output directory.

8. **Completion:**

   - Once the conversion is complete, a message will be displayed indicating that the batch conversion is finished.

<br> <br>

## Example

To run the application, follow these steps:

1. Open a command prompt or double-click the executable.
2. Select the input folder, e.g., `C:\Users\YourUsername\Pictures\Input`.
3. Select the output folder, e.g., `C:\Users\YourUsername\Pictures\Output`.
4. Choose the output format, e.g., `PNG`.
5. (Optional) Enable background removal if desired.

The application will convert all supported image files in the input folder to the selected format and save them in the output folder.

<br> <br>

## Supported Formats

- **Input Formats:** JPG, JPEG, PNG, WEBP, BMP
- **Output Formats:** PNG, JPEG, WEBP, BMP

<br> <br>

## Error Handling

If an error occurs during processing, such as unsupported file formats or issues with reading/writing files, the application will display an error message detailing the problem.

<br> <br>

## Limitations

- **SVG Files:** SVG files are not supported and will be skipped during conversion.
- **Large Files:** Processing very large files may be limited by system resources.

<br> <br>

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

<br> <br>

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. Contributions are welcome!

<<<<<<< HEAD
<br> <br>

- **Back-End Technologies**:

<p align="left">
<a href="https://nodejs.org/en" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/Deobap73/Deobap73Pictures/main/Assets/nodejs.svg" alt="nodejs" width="70" height="70"/> </a> &nbsp;&nbsp;&nbsp;&nbsp;   
<a href="https://www.mongodb.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/Deobap73/Deobap73Pictures/main/Assets/mongodb.svg" alt="mongoDB" width="70" height="70"/> </a>
=======
- **Technologies used**:
<br> <br>
  <p align="left">
  <a href="https://www.python.org/n" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/Deobap73/Deobap73Pictures/main/Assets/python.svg" alt="python" width="70" height="70"/> </a> &nbsp;&nbsp;&nbsp;&nbsp;  
>>>>>>> 62b1db04895c9a82b41ebccf9b7643ed22a7b1e5
</p>

<br> <br>

- ## 📫 Be in contact with me:
<<<<<<< HEAD

<br> <br>

**For any questions or support, please contact [your email] or open an issue on the repository.**

<p align="left">
    <a href="https://www.linkedin.com/in/deolindobaptista" target="blank"><img src="https://raw.githubusercontent.com/Deobap73/Deobap73Pictures/main/Assets/linked-in-alt.svg" alt="deolindobaptista" height="50" width="60" style="margin-right: 20px;" /></a>&nbsp;&nbsp;&nbsp;&nbsp;   
    <a href="https://github.com/Deobap73" target="blank"><img src="https://raw.githubusercontent.com/Deobap73/Deobap73Pictures/main/Assets/github.svg" alt="deolindobaptista" height="50" width="60" style="margin-right: 20px;" /></a>&nbsp;&nbsp;&nbsp;&nbsp;   
    <a href="https://wa.me/+4917634644129" target="blank"><img src="https://raw.githubusercontent.com/Deobap73/Deobap73Pictures/main/Assets/whatsapp.svg" alt="deolindobaptista" height="50" width="50" style="margin-right: 20px;" /></a>&nbsp;&nbsp;&nbsp;&nbsp;   
    <a href="mailto:contact@deolindobaptista.com" target="_blank">
        <img src="https://github.com/Deobap73/Deobap73Pictures/blob/c3ebd3b8d7ef3169a38eaa12dc0db698d4a4c255/Assets/email.webp" alt="deolindobaptista" height="50" width="50" style="margin-left: 20px;" />
    </a>
</p>

<br> <br>
=======
  <br> <br>
  **For any questions or support, please contact or open an issue on the repository.**
    <p align="left">
        <a href="https://www.linkedin.com/in/deolindobaptista" target="blank"><img src="https://raw.githubusercontent.com/Deobap73/Deobap73Pictures/main/Assets/linked-in-alt.svg" alt="deolindobaptista" height="50" width="60" style="margin-right: 20px;" /></a>&nbsp;&nbsp;&nbsp;&nbsp;   
        <a href="https://github.com/Deobap73" target="blank"><img src="https://raw.githubusercontent.com/Deobap73/Deobap73Pictures/main/Assets/github.svg" alt="deolindobaptista" height="50" width="60" style="margin-right: 20px;" /></a>&nbsp;&nbsp;&nbsp;&nbsp;   
        <a href="https://wa.me/+4917634644129" target="blank"><img src="https://raw.githubusercontent.com/Deobap73/Deobap73Pictures/main/Assets/whatsapp.svg" alt="deolindobaptista" height="50" width="50" style="margin-right: 20px;" /></a>&nbsp;&nbsp;&nbsp;&nbsp;   
        <a href="mailto:contact@deolindobaptista.com" target="_blank">
            <img src="https://github.com/Deobap73/Deobap73Pictures/blob/main/Assets/email.png" alt="deolindobaptista" height="50" width="50" style="margin-left: 20px;" />
        </a>
    </p>
    <br> <br>
>>>>>>> 62b1db04895c9a82b41ebccf9b7643ed22a7b1e5

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=Deobap73)](https://github.com/anuraghazra/github-readme-stats)

![GitHub streak stats](https://streak-stats.demolab.com/?user=Deobap73) &nbsp;&nbsp;&nbsp;&nbsp; ![GitHub stats](https://github-readme-stats.vercel.app/api?username=Deobap73&show_icons=true&count_private=true)

[![trophy](https://github-profile-trophy.vercel.app/?username=Deobap73)](https://github.com/ryo-ma/github-profile-trophy)
