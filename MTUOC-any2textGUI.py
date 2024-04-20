#!/usr/bin/python3
#    any2text
#    Copyright (C) 2023  Antoni Oliver
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import argparse
import codecs
import textract
import os
import sys

from tkinter import *
from tkinter.ttk import *

import tkinter 
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askdirectory
from tkinter import messagebox

def select_file():
    infile = askopenfilename(initialdir = ".",filetypes =(("All Files","*.*"),),
                           title = "Select the input file.")
    E1.delete(0,END)
    E1.insert(0,infile)
    E1.xview_moveto(1)

def arregla(text):
    text=text.replace("\n\n","@SALTPARA@")
    text=text.replace("\n"," ")
    text=text.replace("@SALTPARA@","\n")
    return(text)
    
def go():
    inputfile=E1.get()
    file_name, file_extension = os.path.splitext(inputfile)
    fixpdf=False
    if var.get()==1:
        fixpdf=True
    outputfile=inputfile+".txt"

    sortida=codecs.open(outputfile,"w",encoding="utf-8")
    try:
        text = textract.process(inputfile).decode("utf-8")
        if fixpdf and file_extension in [".pdf",".PDF"]:
            text=arregla(text)
        for linia in text.split("\n"):
            linia=linia.rstrip()
            sortida.write(linia+"\n")
        sortida.close()
    except:
        print("ERROR converting:",inputfile,sys.exc_info())
        
top = Tk()
top.title("MTUOC-any2textGUI")

B1=tkinter.Button(top, text = str("Select file"), borderwidth = 1, command=select_file,width=14).grid(row=0,column=0)
E1 = tkinter.Entry(top, bd = 5, width=80, justify="right")
E1.grid(row=0,column=1)

var = tkinter.IntVar()
CB1 = tkinter.Checkbutton(top, text="Fix PDF", variable=var)
CB1.grid(row=1,column=0)

B2=tkinter.Button(top, text = str("Convert!"), borderwidth = 1, command=go,width=14).grid(sticky="W",row=3,column=0)

top.mainloop()

