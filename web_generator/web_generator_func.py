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

import os
from tkinter import *
from tkinter import messagebox
import webbrowser

file = "index.html"

#Function takes in the th.Text object created in the gui and loads into itthe data in index.html.
#If it doesn't exist, a default set of code is used.
def onLoad(txt_code):
	txt_code.delete('1.0', END)
	if (os.path.exists(file)):
		f = open(file, "r")
		txt_code.insert(END, f.read())
		f.close()
	else:
		txt_code.insert("""<html>
	<body>
		<h1>
	Stay tuned for our amazing summer sale!
		</h1>
	</body>
</html>""")

# 1) opens index.html for writing and writes all the code in the txt.code tk.Text object into it, then
# 2) loads it in a new browser window.
def onCommit(txt_code):
	f = open(file, "w")
	f.write(txt_code.get("1.0", END))
	f.close()
	webbrowser.open(file, 2, True)

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

if __name__ == "__main__":
    pass