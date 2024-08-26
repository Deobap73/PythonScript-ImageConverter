# Image Converter

<br>

## Overview

The Image Converter is a command-line application designed to convert image files from one format to another. It supports a variety of image formats and provides an easy way to batch process images in a specific directory. The program is packaged as a standalone executable for easy distribution and use on Windows.
<br> <br>

## Features

- **Batch Image Conversion:** Convert multiple images in a specified directory.
- **Format Support:** Supports conversion to common formats such as PNG, JPEG, WEBP, and BMP.
- **Flexible Input and Output:** Allows users to specify input and output directories and select the desired output format.
- **Error Handling:** Provides informative messages in case of errors during processing.

<br> <br>

## Requirements

- **Windows OS:** This executable is specifically designed for Windows.
- **Python 3.x:** Required for compiling the script into an executable.
- **PyInstaller:** Used to create the standalone executable.

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
     pip install pillow pyinstaller
     ```

3. **Prepare the Environment:**
   - **Run Command Prompt as Administrator:** This is necessary to ensure proper installation of packages and access rights. To do this:

     - Search for `cmd` or `Command Prompt` in the Start menu.
     - Right-click on `Command Prompt` and select `Run as administrator`.

     <br>

   - **Ensure Python Scripts Directory is in PATH:**
   - Right-click on `This PC` or `Computer` on the desktop or in File Explorer. <br>
   - Select `Properties`, then click on `Advanced system settings`. <br> - In the `System Properties` window, click on the `Environment Variables` button.
   - In the `Environment Variables` window, find the `Path` variable under `System variables`, and click `Edit`.
   - Ensure that the path to the Python `Scripts` directory (e.g., `C:\Python39\Scripts`) is included. If not, click `New` and add the path.
     <br>
4. **Compile the Executable:**
   - Use PyInstaller to compile the script into an executable. Open Command Prompt as Administrator and run the following command:
     ```bash
     pyinstaller --onefile --hidden-import=tkinter --icon=icon.ico converter_imagens.py
     ```
   - The executable will be created in the `dist` folder within the project directory.
     <br>
5. **Run the Executable:**
   - Navigate to the `dist` directory:
     ```bash
     cd dist
     ```
   - Double-click the `converter_imagens.exe` file or run it from the command prompt.
     <br>

## Usage

1. **Run the Executable:**

   - Double-click the `converter_imagens.exe` file or run it from the command prompt.

2. **Input Directory:**

   - You will be prompted to enter the path of the folder containing the images you want to convert.

3. **Output Directory:**

   - Next, specify the path of the folder where you want to save the converted images.

4. **Output Format:**

   - Choose the desired output format from the options provided: PNG, JPEG, WEBP, or BMP.

5. **Conversion Process:**

   - The program will process all images in the input directory, convert them to the specified format, and save them in the output directory.

6. **Completion:**
   - Once the conversion is complete, a message will be displayed indicating that the batch conversion is finished.

## Example

To run the application, you might follow these steps:

1. Open a command prompt or double-click the executable.
2. Enter the path to the input folder, e.g., `C:\Users\YourUsername\Pictures\Input`.
3. Enter the path to the output folder, e.g., `C:\Users\YourUsername\Pictures\Output`.
4. Choose the output format, e.g., `PNG`.

The application will convert all supported image files in the input folder to the selected format and save them in the output folder.

## Supported Formats

- **Input Formats:** JPG, JPEG, PNG, WEBP, BMP
- **Output Formats:** PNG, JPEG, WEBP, BMP

## Error Handling

If an error occurs during processing, such as unsupported file formats or issues with reading/writing files, the application will display an error message detailing the problem.

## Limitations

- **SVG Files:** SVG files are not natively supported and will be skipped during conversion.
- **Large Files:** Processing very large files may be limited by system resources.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. Contributions are welcome!

- **Back-End Technologies**:
<br> <br>
  <p align="left">
  <a href="https://nodejs.org/en" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/Deobap73/Deobap73Pictures/main/Assets/nodejs.svg" alt="nodejs" width="70" height="70"/> </a> &nbsp;&nbsp;&nbsp;&nbsp;   
    <a href="https://www.mongodb.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/Deobap73/Deobap73Pictures/main/Assets/mongodb.svg" alt="mongoDB" width="70" height="70"/> </a>
</p>
<br> <br>

- ## 📫 Be in contact with me:
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

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=Deobap73)](https://github.com/anuraghazra/github-readme-stats)

![GitHub streak stats](https://streak-stats.demolab.com/?user=Deobap73) &nbsp;&nbsp;&nbsp;&nbsp; ![GitHub stats](https://github-readme-stats.vercel.app/api?username=Deobap73&show_icons=true&count_private=true)

[![trophy](https://github-profile-trophy.vercel.app/?username=Deobap73)](https://github.com/ryo-ma/github-profile-trophy)
