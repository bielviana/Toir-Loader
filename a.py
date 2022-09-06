# import tkinter as tk
# from tkinter import filedialog

# root = tk.Tk()
# root.withdraw()

# file_path = filedialog.askopenfilename()



import easygui

file_path = easygui.fileopenbox(default="*.exe")




print(file_path)