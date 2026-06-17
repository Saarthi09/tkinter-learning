import tkinter as tk

root = tk.Tk()
root.title("Note")
# button = tk.Button(root, text="End", width=25, command=root.destroy)
# button.pack()
tk.Label(root, text="First name").grid(row = 0, column=0)
tk.Label(root, text="Second name").grid(row = 1, column=0)
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry1.grid(row=0, column=2)
entry2.grid(row=1, column=2)
root.mainloop()