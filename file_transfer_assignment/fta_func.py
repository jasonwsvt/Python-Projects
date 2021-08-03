#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Python Ver:   3.5.1
#
# Author:       Daniel A. Christie (modified by Jason Storer)
#
# Purpose:      Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested to work with Windows 10.

import os, time, shutil
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def center_window(self, w, h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)


def select_folder(textfield, title="Select folder", folder=".", master=None):
    """
    Display a box to select a folder.

    If a folder is selected the folder path is returned, otherwise `None` is returned.

    :param string title:
        The title to be displayed on the box. Defaults to 'Select file'.
    :param string folder:
        The initial folder to open. Defaults to '.'.
    :param App master:
        Optional guizero master which the popup will be placed over. Defaults
        to `None`.
    :return:
        The path of folder selected or `None`.
    """
    if not os.path.isdir(folder):
        print("The folder '{}' specified for select_folder does not exist.".format(folder))
        folder = "."
    
    textfield.delete(0, END)
    textfield.insert(0, filedialog.askdirectory(title=title, initialdir=folder, parent=None if master is None else master.tk))

def checkForFiles(self):
    #set the source path
    source = os.path.normpath(self.txt_source.get())

    #Create a list of all files in the source directory that end with ".txt"
    files = filter(lambda x: x.endswith(".txt"), os.listdir(source))

    #Conversion from unix timestamp to days
    tsToDays = 24 * 60 * 60

    for i in files:
        # get the normalized path of the file
        file = os.path.normpath(os.path.join(source, i))

        # The time the file was modified
        modificationTime = os.stat(file).st_mtime

        # If the amount of time between now and the file modification time in days is less than 1
        if((time.time() - modificationTime) / tsToDays <= 1):
            # update listbox with the filename
            self.lst_files.insert(END, i)

def transferFiles(self):
    #get the list of files
    files = list(self.lst_files.get(0, END))

    #set the source path
    source = self.txt_source.get()

    #set the destination path
    destination = self.txt_destination.get()

    #Go through each of the files in the list as an array
    for i in files:
        # create the full path of the file from the source directory and the filename
        file = os.path.normpath(os.path.join(source, i))
        #move the file to the destination folder
        shutil.move(file, destination)

    #Delete all files in list
    self.lst_files.delete(0, END)

if __name__ == "__main__":
    pass