# Calculus Plotter

"""
This program is to provide an interface to do some basic calculus functions within
It will find derivatives, integrals, the area between curves, lengths of curves, etc...
It will also plot all this so that you can see an illustrated version of what is being done

This program was made in attempt to consolidate a bunch of tools I frequently had to go looking for during uni
"""


from frameSingle import *
from frameDual import *
import tkinter as tk
import tkinter.ttk as ttk


class Window:
    def __init__(self, root, title, geometry):
        # This will set all the base information to make the main window
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
        
        # Universal variables
        pad_ext = 5

        # This will create the main notebook for the entire program
        notebook_main = ttk.Notebook(master=root)
        notebook_main.pack(expand=1, fill='both', padx=pad_ext, pady=pad_ext)

        # To create the frames for each main tab
        tab_single = tk.Frame(master=notebook_main)
        # tab_dual = tk.Frame(master=notebook_main)
        # And to add them to the main notebook
        notebook_main.add(tab_single, text='Single Function')
        # notebook_main.add(tab_dual, text='Dual Functions')
        # Making configurations to some rows and columns
        tab_single.columnconfigure([1], weight=1)
        tab_single.rowconfigure([0], weight=1)

        # Putting all the frames into the main program now
        FrameSingle(tab_single)
        # FrameDual(tab_dual)

        self.root.mainloop()  # To actually run the program loop


def main():
    window = Window(tk.Tk(), 'Math Calculator', '1500x650')  # Main window defined here
    

main()


# Future Improvements
# Need to add in the Dual function options and section
