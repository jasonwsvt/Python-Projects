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
import web_generator_func



def load_gui(self):
    """
        Define the default tkinter widgets and their initial
        configuration and place them using the grid geometry.
        I prefer to use grid as it offers the best control
        for pacing the widgets, but is a little confusing at
        first, but that is what this demo is here for...
    """

    #Define the listbox with a scrollbar and grid them
    self.scrollbar = Scrollbar(self.master,orient=VERTICAL)
    self.txt_code = tk.Text(self.master, height=12, width=55, exportselection=0,yscrollcommand=self.scrollbar.set)
    self.txt_code.bind('<<ListboxSelect>>',lambda event: web_generator_func.onSelect(self,event))
    self.scrollbar.config(command=self.txt_code.yview)
    self.scrollbar.grid(row=0,column=3,rowspan=14,columnspan=1,padx=(5,0),pady=(5,0),sticky=N+E+S)
    self.txt_code.grid(row=0,column=0,rowspan=14,columnspan=3,padx=(5,0),pady=(5,0),sticky=N+E+S+W)

    self.btn_commit = tk.Button(self.master,width=12,height=2,text='Commit',command=lambda: web_generator_func.onCommit(self.txt_code))
    self.btn_commit.grid(row=14,column=0,padx=(5,0),pady=(5,5),sticky=W)

    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program',command=lambda: web_generator_func.ask_quit(self))
    self.btn_close.grid(row=14,column=2,columnspan=2,padx=(5,0),pady=(5,5),sticky=E)

    web_generator_func.onLoad(self.txt_code)

if __name__ == "__main__":
    pass