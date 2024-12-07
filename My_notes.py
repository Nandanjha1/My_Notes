# Create My Notes(like Notepad)

from tkinter import *
from tkinter import ttk
from tkinter import filedialog,messagebox
import os
import tempfile
import win32print
import win32api
root = Tk()
root.title("My Notes")
root.minsize(width=400, height=300)
root.iconbitmap("C:/Users/navin/OneDrive/Desktop/Logo/icon.ico")

def get_current_text_widget():
    """Get the Text widget in the currently selected tab."""
    current_tab = notebook.select()
    frame = root.nametowidget(current_tab)
    text_widget = frame.winfo_children()[0]
    return text_widget
         
def new_tab():  # Not working properly need to change.
    new_tab = Frame(notebook)
    text_area = Text(new_tab)
    text_area.pack(fill="both", expand=True)
    tab_name = f"Tab {len(notebook.tabs()) + 1}"
    notebook.add(new_tab, text=tab_name)
    notebook.select(new_tab)

# def new_tab():
#         """Create a new tab with a text editor."""
#         frame = ttk.Frame(notebook)
#         text_area = Text(frame, wrap="word")
#         text_area.pack(fill="both", expand=True, padx=2, pady=2)
#         notebook.add(frame, text=f"Untitled {len(notebook.tabs()) + 1}")
#         notebook.select(frame)

def new_window():
    new_window = Toplevel(root)
    new_window.title("New Window")
    new_window.minsize(width=400, height=300)
    
    new_text_area = Text(new_window, wrap='word')
    new_text_area.pack(fill="both", expand=1)

def save_all():
    for tab in file_path:
        if file_path[tab] is None:
            notebook.select(tab)
            save_as_file()
        else:
            with open(file_path[tab], "w") as file:
                file.write(tab.get("1.0", "end").strip())
    messagebox.showinfo("Save All", "All files saved successfully.")

def open_file():
    """Open a file and display its contents in the current tab."""
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "r") as file:
            content2 = file.read()
        content = get_current_text_widget()
        content.delete("1.0", "end")
        content.insert("1.0", content2)
        notebook.tab(notebook.select(), text=file_path.split("/")[-1])

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

def save_as_file():
    pass

def page_setup():
    pass

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

def close_current_tab():
    """Closes the currently selected tab."""
    if len(notebook.tabs()) >= 1:
        current_tab = notebook.select()
        notebook.forget(current_tab)
    else:
        messagebox.showwarning("Warning", "Cannot close the last tab!")

def close_window():
    if messagebox.askyesno("Quit", "Are you sure you want to close the window?"):
        new_window.destroy()
 
def exit():
    root.destroy()

def undo():
    try:
        text.edit_undo()
    except TclError:
        messagebox.showinfo("Undo", "Nothing to undo")

def cut():
    text.event_generate("<<Cut>>")

def copy():
    text.event_generate("<<Copy>>")

def paste():
    text.event_generate("<<Paste>>")

def delete_text():
    text.delete("1.0", "end")

def function():
    print("All functions doing the same thing...")

                  
menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New tab              Ctrl+N", command=new_tab)
file_menu.add_command(label="New window      Ctrl+Shift+N", command=new_window)
file_menu.add_command(label="Save all                Ctrl+Alt+S", command=save_all)
file_menu.add_command(label="Open                   Ctrl+O", command=open_file)
file_menu.add_command(label="Save                     Ctrl+S", command=save_file)
file_menu.add_command(label="Save as                Ctrl+Shift+S", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Page setup", command=page_setup)
file_menu.add_command(label="Print                     Ctrl+P", command=print_file)
file_menu.add_separator()
file_menu.add_command(label="Close tab             Ctrl+W", command=close_current_tab)
file_menu.add_command(label="Close Window   Ctrl+Shift+W", command=close_window)
file_menu.add_command(label="Exit", command=exit)

edit_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo                              Ctrl+Z", command=undo)
edit_menu.add_separator()
edit_menu.add_command(label="Copy                              Ctrl+C", command=copy)
edit_menu.add_command(label="Past                                Ctrl+V", command=paste)
edit_menu.add_command(label="Cut                                 Ctrl+X", command=cut)
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
