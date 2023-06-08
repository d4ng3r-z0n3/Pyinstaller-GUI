# PyInstaller GUI

This is a graphical user interface (GUI) program built with Tkinter for converting Python scripts into standalone executables using PyInstaller. The program provides a user-friendly interface for selecting a script, configuring conversion options, and running the conversion process.

## Prerequisites

- Python 3.x installed
- Required packages: `tkinter`, `subprocess`, `os`, `threading`, `shutil`

## Usage

1. Run the program by executing the script `PyInstallerGUI.py`.
2. The PyInstaller GUI window will appear.
3. Select the Python script you want to convert by clicking the "Browse" button or manually entering the path in the "Script Path" field.
4. Optionally, check the "Show Command Window" checkbox if you want to see the command window during the conversion process.
5. Click the "Convert" button to start the conversion.
6. The output of the conversion process will be displayed in a separate window titled "Command Output". You can track the progress and see any error messages in this window.
7. Once the conversion is complete, a message will be shown indicating the success or failure of the conversion.
8. If the conversion was successful, a message box will display the path of the generated executable. You can choose to open the file by clicking the "Open File" button.

## Important Notes

- Make sure you have installed all the required packages before running the program.
- PyInstaller must be installed and accessible in your system's environment variables.
- The program assumes that the `pyinstaller` command is available globally.
- The converted executable will be saved with the same name as the input script but with the `.exe` extension.
- By default, the program creates a single-file executable without a console window. You can change this behavior by checking the "Show Command Window" checkbox.

## Contributing

Contributions are welcome! If you find any issues or want to enhance the program, feel free to create a pull request.

## License

This program is licensed under the [MIT License](LICENSE).
