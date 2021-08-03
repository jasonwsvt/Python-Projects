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
import fta_func



def load_gui(self):
    """
        Define the default tkinter widgets and their initial
        configuration and place them using the grid geometry.
        I prefer to use grid as it offers the best control
        for pacing the widgets, but is a little confusing at
        first, but that is what this demo is here for...
    """

    self.btn_source = tk.Button(self.master,width=12,height=1,text='Source',command=lambda: fta_func.select_folder(self.txt_source))
    self.btn_source.grid(row=0,column=0,padx=(5,5),pady=(5,5),sticky=W)
    self.btn_destination = tk.Button(self.master,width=12,height=1,text='Destination',command=lambda: fta_func.select_folder(self.txt_destination))
    self.btn_destination.grid(row=1,column=0,padx=(5,5),pady=(5,5),sticky=W)

    self.txt_source = tk.Entry(self.master,width=56,text='')
    self.txt_source.grid(row=0,column=1,columnspan=2,padx=(5,0),pady=(8,2),sticky=N+E+W)
    self.txt_destination = tk.Entry(self.master,width=56,text='')
    self.txt_destination.grid(row=1,column=1,columnspan=2,padx=(5,0),pady=(8,2),sticky=N+E+W)

    self.btn_check = tk.Button(self.master,width=12,height=2,text='Check for files...',command=lambda: fta_func.checkForFiles(self))
    self.btn_check.grid(row=2,column=0,padx=(5,5),pady=(0,5),sticky=W)

    self.btn_transfer = tk.Button(self.master,width=12,height=2,text='Transfer',command=lambda: fta_func.transferFiles(self))
    self.btn_transfer.grid(row=8,column=0,padx=(5,5),pady=(0,0),sticky=S)

    #Define the listbox with a scrollbar and grid them
    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.lst_files = Listbox(self.master,width=52,exportselection=0,yscrollcommand=self.scrollbar1.set)
#    self.lst_files.bind('<<ListboxSelect>>',lambda event: fta_func.onSelect(self,event))
    self.scrollbar1.config(command=self.lst_files.yview)
    self.scrollbar1.grid(row=2,column=2,rowspan=7,columnspan=1,padx=(0,5),pady=(5,0),sticky=N+E+S)
    self.lst_files.grid(row=2,column=1,rowspan=7,columnspan=1,padx=(5,0),pady=(5,0),sticky=N+E+S+W)

if __name__ == "__main__":
    pass