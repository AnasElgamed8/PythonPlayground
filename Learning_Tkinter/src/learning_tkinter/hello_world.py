"""Hello world with Tkinter (what a weird name)"""

import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="I kind of regret picking this book")

label.pack()

label2 = tk.Label(
    root, text="Whatever, enter something, maybe you will see something cool"
)
label2.pack()
box = tk.Entry()
box.pack()
submit = tk.Button(root, text="Submit")
submit.pack()
insult = tk.Label(root, text="I don't know how to make this work yet")
insult1 = tk.Label(root, text="nvm I'm dropping tkinter")

if submit:
    insult.pack()
    insult1.pack()
root.mainloop()
