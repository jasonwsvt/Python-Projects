#!/usr/bin/python
"""
    #!/usr/bin/python
    It's a recommended way, proposed in documentation:
    2.2.2. Executable Python Scripts.
    In a Unix-like operating system, the program loader
    takes the presence of these two characters as an
    indication that the file is a script, and tries to
    execute that script using the interpreter specified
    by the rest of the first line in the file.
"""
# -*- coding: utf-8 -*-
"""
    # -*- coding: utf-8 -*-
    This sets the charset if it is present on the first two lines of the file.
    this is Syntax to declare the encoding of a Python source file. It's discussed
    in PEP 0263 - Defining Python Source Code Encodings.
    https://www.python.org/dev/peps/pep-0263/
"""
#
# Python Ver:   3.5.1
#
# Author:       Daniel A. Christie (modified by Jason Storer)
#
# Purpose:      Web page generator. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 10.


from tkinter import *
import tkinter as tk

# Be sure to import our other modules 
# so we can have access to them
import web_generator_gui
import web_generator_func


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame): #Frame is the primary tkinter object
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.width = 480
        self.height = 252
        self.master = master #self.master is the ParentWindow Frame
        self.master.minsize(self.width, self.height) #(Height, Width)
        self.master.maxsize(self.width, self.height)
        # This CenterWindow method will center our app on the user's screen
        web_generator_func.center_window(self,self.width, self.height)
        self.master.title("Site Code Generator")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: web_generator_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module, 
        # keeping your code comparmentalized and clutter free
        web_generator_gui.load_gui(self)

"""
    It is from these few lines of code that Python will begin our gui and application
    The (if __name__ == "__main__":) part is basically telling Python that if this script
    is ran, it should start by running the code below this line....in this case we have
    instructed Python to run the following and in this order:

    root = tk.Tk()              #This Instantiates the Tk.() root frame (window) into being
    App = ParentWindow(root)    #This instantiates our own class as an App object
    root.mainloop()             #This ensures the Tkinter class object, our window, to keep looping
                                #meaning, it will stay open until we instruct it to close
"""

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()