# PyInstaller GUI

A graphical user interface (GUI) for converting Python scripts into standalone executables using PyInstaller.

## Requirements

- Python 3.x
- Tkinter

## Usage

1. Clone the repository or download the `PyInstallerGUI.py` file.

2. Run the script using Python:

   ```bash
   python PyInstallerGUI.pyc
   ```

3. The PyInstaller GUI window will open.

4. Enter the path to the script you want to convert in the "Script Path" field, or click the "Browse" button to select the script file using a file dialog.

5. Check the "Show Command Window" checkbox if you want to display the command window during the conversion process.

6. Check the "Use Custom Icon" checkbox if you want to specify a custom icon for the executable. Click the "Browse Icon" button to select an icon file using a file dialog.

7. Click the "Convert" button to start the conversion process.

8. If a script file is not selected or an error occurs, an error message will be displayed.

9. During the conversion process, the command output will be shown in a separate window titled "Command Output". The output will also be appended to the GUI window.

10. Once the conversion is complete, a success message will be displayed, and the path to the generated executable will be shown. Clicking "Open File" will open the file explorer with the executable file selected.

Note: This GUI uses PyInstaller as the underlying tool for converting the script to an executable. Make sure PyInstaller is installed and available in your system's `PATH`.

## License

This project is licensed under the [MIT License](LICENSE).
