import tkinter as tk

root = tk.Tk()
root.title("Draggable Sticky Note")
root.geometry("600x400")

note = tk.Frame(root, bg = "khaki", bd =1, relief="solid")
note.place(x=50, y=50, width=100, height=100)

title = tk.Lable(note,
                 text = "note 1",
                 bg = "gold",
                 font =("Arial", 12, "bold")
)
title.pack(fill="x")


root.mainloop()