#!/usr/bin/python3
#    any2textDIRGUI
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

def select_input_directory():
    infile = askdirectory(initialdir = ".",title = "Select the input directory.")
    E1.delete(0,END)
    E1.insert(0,infile)
    E1.xview_moveto(1)
    
def select_output_directory():
    infile = askdirectory(initialdir = ".",title = "Select the output directory.")
    E2.delete(0,END)
    E2.insert(0,infile)
    E2.xview_moveto(1)

def arregla(text):
    text=text.replace("\n\n","@SALTPARA@")
    text=text.replace("\n"," ")
    text=text.replace("@SALTPARA@","\n")
    return(text)

def go():
    inputdir=E1.get()
    outputdir=E2.get()
    isExist = os.path.exists(outputdir)
    fixpdf=False
    if var.get()==1:
        fixpdf=True
    if not isExist:
       os.makedirs(outputdir)

    for file_path in os.listdir(inputdir):
        if os.path.isfile:
            error=False
            file_pathIN=os.path.join(inputdir, file_path)
            file_name, file_extension = os.path.splitext(file_path)
            file_pathOUT=os.path.join(outputdir, file_path+".txt")
            sortida=codecs.open(file_pathOUT,"w",encoding="utf-8")
            try:
                text = textract.process(file_pathIN).decode("utf-8")
            except:
                print("ERROR converting:",file_pathIN,sys.exc_info())
                error=True
            if not error:
                if fixpdf and file_extension in [".pdf",".PDF"]:
                    text=arregla(text)
                for linia in text.split("\n"):
                    linia=linia.rstrip()
                    sortida.write(linia+"\n")
                sortida.close()


top = Tk()
top.title("MTUOC-any2textDIRGUI")

B1=tkinter.Button(top, text = str("Select input dir."), borderwidth = 1, command=select_input_directory,width=14).grid(row=0,column=0)
E1 = tkinter.Entry(top, bd = 5, width=80, justify="right")
E1.grid(row=0,column=1)

B2=tkinter.Button(top, text = str("Select output dir."), borderwidth = 1, command=select_output_directory,width=14).grid(row=1,column=0)
E2 = tkinter.Entry(top, bd = 5, width=80, justify="right")
E2.grid(row=1,column=1)

var = tkinter.IntVar()
CB1 = tkinter.Checkbutton(top, text="Fix PDF", variable=var)
CB1.grid(row=2,column=0)

B2=tkinter.Button(top, text = str("Convert!"), borderwidth = 1, command=go,width=14).grid(sticky="W",row=3,column=0)

top.mainloop()

