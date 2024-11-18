# Create My Notes(like Notepad)

from tkinter import *
from tkinter import ttk,filedialog,messagebox
import os
import tempfile
import win32print
import win32api
root = Tk()
root.title("My Notes")
root.minsize(width=400, height=300)
root.iconbitmap("C:/Users/navin/OneDrive/Desktop/Logo/icon.ico")

def function():
    print("All functions doing the same thing...")
    
def open_file():
    global name
    name = filedialog.askopenfilename(parent=root, initialdir=os.getcwd())

def delete_text():
    text.delete("1.0", "end")
 
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        try:
            content = text.get("1.0", "end-1c")
            with open(file_path, "w") as file:
                file.write(content)
            messagebox.showinfo("Success", "File saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {e}")

def print_file():
    content1 = text.get("1.0", "end-1c")
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
    temp_file.write(content1.encode("utf-8"))
    temp_file.close()
    try:
        printer_name = win32print.GetDefaultPrinter()
        win32api.ShellExecute(0, "print", temp_file.name, None, ".", 0)
        print(f"Content sent to printer: {printer_name}")
    except Exception as e:
        print(f"Error while printing: {e}")
        
def new_tab():  # Not working properly need to change.
    new_tab = Frame(notebook)
    text_area = Text(new_tab)
    text_area.pack(fill="both", expand=True)
    tab_name = f"Tab {len(notebook.tabs()) + 1}"
    notebook.add(new_tab, text=tab_name)
    notebook.select(new_tab)

def close_current_tab():
    """Closes the currently selected tab."""
    if len(notebook.tabs()) >= 1:
        current_tab = notebook.select()
        notebook.forget(current_tab)
    else:
        messagebox.showwarning("Warning", "Cannot close the last tab!")
                     
menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New tab              Ctrl+N", command=new_tab)
file_menu.add_command(label="New window      Ctrl+Shift+N", command=function)
file_menu.add_command(label="Save all                Ctrl+Alt+S", command=function)
file_menu.add_command(label="Open                   Ctrl+O", command=open_file)
file_menu.add_command(label="Save                     Ctrl+S", command=save_file)
file_menu.add_command(label="Save as                Ctrl+Shift+S", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Page setup", command=function)
file_menu.add_command(label="Print                     Ctrl+P", command=print_file)
file_menu.add_separator()
file_menu.add_command(label="Close tab             Ctrl+W", command=close_current_tab)
file_menu.add_command(label="Close Window   Ctrl+Shift+W", command=function)
file_menu.add_command(label="Exit", command=function)

edit_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo                              Ctrl+Z", command=function)
edit_menu.add_separator()
edit_menu.add_command(label="Copy                              Ctrl+C", command=function)
edit_menu.add_command(label="Past                                Ctrl+V", command=function)
edit_menu.add_command(label="Cut                                 Ctrl+X", command=function)
edit_menu.add_command(label="Delete                            Del", command=delete_text)
edit_menu.add_separator()
edit_menu.add_command(label="Search with Bing         Ctrl+E", command=function)
edit_menu.add_separator()
edit_menu.add_command(label="Find                               Ctrl+F", command=function)
edit_menu.add_command(label="Find next                      F3", command=function)
edit_menu.add_command(label="Find previous              Shift+F3", command=function)
edit_menu.add_command(label="Replace                        Ctrl+H", command=function)
edit_menu.add_command(label="Go to                            Ctrl+G", command=function)
edit_menu.add_separator()
edit_menu.add_command(label="Font", command=function)

view_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Status bar    ", command=function)
view_menu.add_command(label="Word wrap    ", command=function)
view_menu.add_command(label="Zoom in          ctrl+plus", command=function)
view_menu.add_command(label="Zoom out        ctrl+minus", command=function)

text = Text(root)
text.pack(fill="both", expand=True)
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

root.mainloop()
