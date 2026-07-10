import tkinter as tk

root = tk.Tk()
root.title("Sticky notes")
root.geometry("600x600")
root.configure(bg="khaki")

label = tk.Label(text="Sticky notes",
                 font = ("Times New Roman", 20),
                 bg= "Yellow")
label.pack()



def create_note():
    new_window = tk.Tk()
    new_window.title("Note")
    new_window.geometry("400x400")
    new_window.configure(bg= "skyblue")


create_btn = tk.Button(root,
                       text = "Create Note",
                       font=("Times New Roman", 14),
                       bg= "khaki",
                       command= create_note
                       )


create_btn.pack()

exit_btn = tk.Button(root,
                     text="Exit",
                     font=("Times New Roman", 14),
                     command= root.destroy)
exit_btn.pack()


create_btn.place(x=100, y = 150)
label.place(x=250 ,y=50)
exit_btn.place(x=100, y=200)

root.mainloop()