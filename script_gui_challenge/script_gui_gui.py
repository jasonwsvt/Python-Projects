#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.5.1
#
# Author:       Daniel A. Christie
#
# Purpose:      Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 10.


from tkinter import *
import tkinter as tk

# Be sure to import our other modules 
# so we can have access to them
#import script_gui_main
import script_gui_func



def load_gui(self):
    """
        Define the default tkinter widgets and their initial
        configuration and place them using the grid geometry.
        I prefer to use grid as it offers the best control
        for pacing the widgets, but is a little confusing at
        first, but that is what this demo is here for...
    """

    self.btn_browse1 = tk.Button(self.master,width=12,height=1,text='Browse...',command=lambda: script_gui_func.select_folder(self.txt_browse1))
    self.btn_browse1.grid(row=1,column=0,padx=(15,15),pady=(40,5),sticky=W)
    self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Browse...',command=lambda: script_gui_func.select_folder(self.txt_browse2))
    self.btn_browse2.grid(row=2,column=0,padx=(15,15),pady=(5,5),sticky=W)

    self.txt_browse1 = tk.Entry(self.master,width=56,text='')
    self.txt_browse1.grid(row=1,column=1,columnspan=2,padx=(15,0),pady=(40,5),sticky=N+E+W)
    self.txt_browse2 = tk.Entry(self.master,width=56,text='')
    self.txt_browse2.grid(row=2,column=1,columnspan=2,padx=(15,0),pady=(5,5),sticky=N+E+W)

    self.btn_check = tk.Button(self.master,width=12,height=2,text='Check for files...',command=lambda: script_gui_func.addToList(self))
    self.btn_check.grid(row=3,column=0,padx=(15,15),pady=(5,5),sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program',command=lambda: script_gui_func.ask_quit(self))
    self.btn_close.grid(row=3,column=2,padx=(15,0),pady=(5,5),sticky=E)

#    script_gui_func.create_db(self)
#    script_gui_func.onRefresh(self)

if __name__ == "__main__":
    pass
