import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import subprocess
import os
import threading
import shutil  # Add the import statement for shutil

class OutputWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Command Output")

        self.output_text = tk.Text(self, height=20, width=80)
        self.output_text.pack()
        self.output_text.configure(state="disabled")

    def append_text(self, text):
        self.output_text.configure(state="normal")
        self.output_text.insert(tk.END, text)
        self.output_text.see(tk.END)
        self.output_text.update_idletasks()
        self.output_text.configure(state="disabled")


class PyInstallerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyInstaller GUI")

        # Script Path
        self.script_path = tk.StringVar()
        self.show_command_window = tk.BooleanVar()
        self.show_command_window.set(False)

        self.create_widgets()

    def create_widgets(self):
        # Script Path
        script_label = tk.Label(self, text="Script Path:")
        script_label.grid(row=0, column=0, sticky="w")
        script_entry = tk.Entry(self, textvariable=self.script_path)
        script_entry.grid(row=0, column=1, padx=5, pady=5)
        script_browse_button = tk.Button(self, text="Browse", command=self.browse_script)
        script_browse_button.grid(row=0, column=2, padx=5, pady=5)

        # Show Command Window
        show_command_window_check = tk.Checkbutton(self, text="Show Command Window", variable=self.show_command_window)
        show_command_window_check.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=2)

        convert_button = tk.Button(self, text="Convert", command=self.convert_script)
        convert_button.grid(row=2, column=0, columnspan=3, padx=5, pady=10)

    def browse_script(self):
        script_path = filedialog.askopenfilename(title="Select Script File")
        self.script_path.set(script_path)

    def convert_script(self):
        script_path = self.script_path.get()

        if not script_path:
            messagebox.showerror("Error", "Please select a script file.")
            return

        script_dir = os.path.dirname(script_path)

        default_output_path = filedialog.asksaveasfilename(
            title="Save Executable",
            initialdir=script_dir,
            initialfile=os.path.splitext(os.path.basename(script_path))[0] + ".exe",
            defaultextension=".exe",
            filetypes=[("Executable Files", "*.exe")]
        )

        if not default_output_path:
            return

        self.output_window = OutputWindow(self)
        self.output_window.update()

        thread = threading.Thread(target=self.run_pyinstaller, args=(script_path, default_output_path))
        thread.start()

    def run_pyinstaller(self, script_path, output_path):
        command = f"pyinstaller --onefile {script_path} --name {os.path.splitext(os.path.basename(output_path))[0]}"
        if not self.show_command_window.get():
            command += " --noconsole"

        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

        while True:
            line = process.stdout.readline()
            if not line:
                break
            line = line.decode("utf-8")
            self.output_window.append_text(line)

        process.wait()
        self.output_window.append_text("Conversion complete.\n")

        self.copy_executable(script_path, output_path)

    def copy_executable(self, script_path, output_path):
        script_name = os.path.splitext(os.path.basename(script_path))[0]
        exe_path = os.path.join(os.path.dirname(script_path), "dist", f"{script_name}.exe")

        try:
            shutil.copy(exe_path, output_path)
            messagebox.showinfo("Success", "Script successfully converted to executable!")
            self.show_exe_path(output_path)
        except FileNotFoundError:
            messagebox.showerror("Error", "Executable file not found.")

    def show_exe_path(self, output_path):
        messagebox.showinfo("Executable Path", f"Executable path: {output_path}")

        answer = messagebox.askyesno("Open File", "Do you want to open the executable file?")
        if answer:
            self.open_file(output_path)

    def open_file(self, path):
        if os.path.exists(path):
            subprocess.Popen(f'explorer /select,"{os.path.abspath(path)}"')


if __name__ == "__main__":
    app = PyInstallerGUI()
    app.mainloop()
