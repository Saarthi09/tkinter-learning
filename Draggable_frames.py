import tkinter as tk

root = tk.Tk()
root.title("Draggable Sticky Note")
root.geometry("600x400")

note = tk.Frame(root, bg = "khaki", bd =1, relief="solid")
note.place(x=50, y=50, width=200, height=200)

title = tk.Label(note,
                 text = "note 1",
                 bg = "gold",
                 font =("Arial", 12, "bold")
)
title.pack(fill="x")

def start_drag(event):
    note.drag_x = event.x_root - note.winfo_x()
    note.drag_y = event.y_root - note.winfo_y()

def drag(event):
    x = event.x_root - note.drag_x
    y = event.y_root - note.drag_y
    note.place(x=x, y=y)

note.bind("<Button-1>", start_drag)
note.bind("<B1-Motion>", drag)

title.bind("<Button-1>", start_drag)
title.bind("<B1-Motion>", drag)


root.mainloop()