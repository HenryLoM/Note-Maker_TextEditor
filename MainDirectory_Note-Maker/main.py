import Templates as tm
import tkinter as tk
from tkinter import filedialog

# - - - - - - - functions - - - - - - -

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")],
                                             initialfile="untitled.txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))

def exit_editor():
    root.destroy()

def fill_template(event):
    # Check if the event was triggered by user selection
    if event.widget == template_menu and template_var.get() != "Select Template":
        # if alright
        selected_template = template_var.get()
        tm.call_template(text, selected_template)

# - - - - - - - window - - - - - - -

# primary
root = tk.Tk()
root.title("Note-Maker")
root.geometry("500x350")

# input place
text = tk.Text(root, wrap="word")
text.pack(expand=True, fill="both")
text.configure(bg="#242424", fg="#ffffff", highlightbackground="#242424", insertbackground="#ffffff")  # change cursor color

# menubar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_editor)

# buttons

open_button = tk.Button(root, text="Open", command=open_file)
open_button.pack(side=tk.LEFT, padx=5, anchor=tk.S)

save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack(side=tk.LEFT, padx=5, anchor=tk.S)

exit_button = tk.Button(root, text="Exit", command=exit_editor)
exit_button.pack(side=tk.LEFT, padx=5, anchor=tk.S)

# template dropdown
template_var = tk.StringVar(root)
template_var.set("Select Template")
template_menu = tk.OptionMenu(root, template_var, "Select Template", "Todo list", "Email", "README file")
template_menu.pack(side=tk.LEFT, padx=5, anchor=tk.S)

template_menu.bind("<ButtonRelease-1>", fill_template)  # bind the event to automatically fill the template

# make the window
root.mainloop()
