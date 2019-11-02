from Tkinter import *
import os
import re
import tkFileDialog
from process import *

class search_pattern_window (Frame):

      def __init__(self,parent, a0,a1,a2,a3):
        #Save parent reference
        """ initialize the frame"""
        Frame.__init__ (self, parent)
        self.grid ()
        self.parent = parent
        #self.root = tk.Toplevel(parent)
        self.root= Toplevel(parent)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        #t = tk.Toplevel(parent)
        self.ta0=a0
        self.ta1=a1
        self.ta2=a2
        self.ta3=a3
        self.root.wm_title("Searching a pattern")
        w = 300 # width for the Tk root
        h = 300 # height for the Tk root

        ws, hs = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))


        self.l = Label(self.root, text="Enter your list of words to search", font = "Verdana 14 bold")
        self.l.grid(row=1, column=0, sticky=W+E+N+S)

        self.l_word1 = Label(self.root, text="First word to search:", font = "Verdana 12")
        self.l_word1.grid(row=4, column=0, sticky=W)
        self.entry1= Entry(self.root)
        self.entry1.grid(row=5, column=0, sticky=W)
        self.l_word2 = Label(self.root, text="Second word to search:", font = "Verdana 12")
        self.l_word2.grid(row=7, column=0, sticky=W)
        self.entry2= Entry(self.root)
        self.entry2.grid(row=8, column=0, sticky=W)
        self.l_word3 = Label(self.root, text="Third word to search:", font = "Verdana 12")
        self.l_word3.grid(row=10, column=0, sticky=W)
        self.entry3= Entry(self.root)
        self.entry3.grid(row=11, column=0, sticky=W)
        self.l_word4 = Label(self.root, text="Fourth word to search:", font = "Verdana 12")
        self.l_word4.grid(row=13, column=0, sticky=W)
        self.entry4= Entry(self.root)
        self.entry4.grid(row=14, column=0, sticky=W)
        self.l_word5 = Label(self.root, text="Fifth word to search:", font = "Verdana 12")
        self.l_word5.grid(row=16, column=0, sticky=W)
        self.entry5= Entry(self.root)
        self.entry5.grid(row=17, column=0, sticky=W)
        self.pattern_search_btn = Button(self.root, text="Search the pattern", command=self.search_pattern)
        self.pattern_search_btn.grid(row=19, column=0, sticky=W)
        self.clear_btn = Button(self.root, text="Clear entries", command=self.clear_entries)
        self.clear_btn.grid(row=19, column=0, sticky=E)
        

      def search_pattern (self):
        
        search_param1 = ""
        serach_param2 = ""
        search_param3 = ""
        search_param4 = ""
        search_param5 = ""
        search_param1= self.entry1.get ().lower ()
        search_param2= self.entry2.get ().lower ()
        search_param3= self.entry3.get ().lower ()
        search_param4= self.entry4.get ().lower ()
        search_param5= self.entry5.get ().lower ()
        plot_pattern (search_param1,search_param2, search_param3, search_param4, search_param5, self.ta0,
                      self.ta1, self.ta2, self.ta3)

        
      def clear_entries (self):
        self.entry1.delete (0, END)
        self.entry2.delete (0, END)
        self.entry3.delete (0, END)
        self.entry4.delete (0, END)
        self.entry5.delete (0, END)

      def on_closing (self):
        self.root.destroy()
        self.parent.deiconify()
