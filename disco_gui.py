# Copyright (c) 2015 K. Gabriel Rosati
# Adapted from www.tkdocs.com/tutorial/firstexample.html 
# tkdocs Copyright (c) 2007-2015 Mark Roseman


# GUI starts

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("DiSCo!")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

cover_path = StringVar()
intro_path = StringVar()

has_cover = ttk.Checkbutton(mainframe).grid(column=0, row=1, sticky=W)
ttk.Label(mainframe, text="Cover Sheet:").grid(column=1, row=1, sticky=W)
cover_entry = ttk.Entry(mainframe, width=33, textvariable=cover_path)
cover_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Button(mainframe, text="Choose...").grid(column=3, row=1, sticky=E)

has_intro = ttk.Checkbutton(mainframe).grid(column=0, row=2, sticky=W)
ttk.Label(mainframe, text="Introduction:").grid(column=1, row=2, sticky=W)
intro_entry = ttk.Entry(mainframe, width=33, textvariable=intro_path)
intro_entry.grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Choose...").grid(column=3, row=2, sticky=E)

ttk.Label(mainframe, text="<~Question Choice Wizard Here~>").grid(column=2, row=3, sticky=W)

ttk.Button(mainframe, text="Create Latex").grid(column=2, row=4, sticky=E)
ttk.Button(mainframe, text="Create PDF").grid(column=3, row=4, sticky=W)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

cover_entry.focus()

root.mainloop()
