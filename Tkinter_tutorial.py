import tkinter as tk

root = tk.Tk()
root.title("Note")

root.geometry("300x300")
menu = tk.Menu(root)
root.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label="Options", menu=filemenu)
filemenu.add_command(label= "Add")
filemenu.add_command(label="Edit")
filemenu.add_command(label="Delete")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
frame = tk.Frame(root)
frame.pack()
root.mainloop()

# button = tk.Button(root, text="End", width=25, command=root.destroy)
# button.pack()

# tk.Label(root, text="First name").grid(row = 0, column=0)
# tk.Label(root, text="Second name").grid(row = 1, column=0)
# entry1 = tk.Entry(root)
# entry2 = tk.Entry(root)
# entry1.grid(row=0, column=2)
# entry2.grid(row=1, column=2)