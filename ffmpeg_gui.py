import tkinter as tk
from tkinter import filedialog
import subprocess


def browse_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("WebM files", "*.webm")])
    input_file_var.set(file_path)


def browse_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".gif", filetypes=[("GIF files", "*.gif")])
    output_file_var.set(file_path)


def execute_ffmpeg():
    input_file = input_file_var.get()
    output_file = output_file_var.get()
    crf = crf_var.get()
    scale = scale_var.get()

    command = f"ffmpeg -i {input_file} -crf {crf} -vf scale={scale} {output_file}"
    subprocess.run(command, shell=True)


root = tk.Tk()
root.title("FFmpeg GUI")

input_file_var = tk.StringVar()
output_file_var = tk.StringVar()
crf_var = tk.StringVar()
scale_var = tk.StringVar()

input_file_label = tk.Label(root, text="Input file:")
input_file_label.grid(row=0, column=0)
input_file_entry = tk.Entry(root, textvariable=input_file_var)
input_file_entry.grid(row=0, column=1)
input_file_button = tk.Button(root, text="Browse", command=browse_input_file)
input_file_button.grid(row=0, column=2)

output_file_label = tk.Label(root, text="Output file:")
output_file_label.grid(row=1, column=0)
output_file_entry = tk.Entry(root, textvariable=output_file_var)
output_file_entry.grid(row=1, column=1)
output_file_button = tk.Button(root, text="Browse", command=browse_output_file)
output_file_button.grid(row=1, column=2)

crf_label = tk.Label(root, text="CRF value:")
crf_label.grid(row=2, column=0)
crf_entry = tk.Entry(root, textvariable=crf_var)
crf_entry.grid(row=2, column=1)
crf_var.set("35")

scale_label = tk.Label(root, text="Scale:")
scale_label.grid(row=3, column=0)
scale_entry = tk.Entry(root, textvariable=scale_var)
scale_entry.grid(row=3, column=1)
scale_var.set("800:-1")

run_button = tk.Button(root, text="Run FFmpeg", command=execute_ffmpeg)
run_button.grid(row=4, column=1)

root.mainloop()
