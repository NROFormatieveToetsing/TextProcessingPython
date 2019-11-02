from Tkinter import *
import os
import re
import tkMessageBox
import tkFileDialog
from wordcloudtemplates import *
from process import *
from wordcloud import WordCloud, STOPWORDS,ImageColorGenerator
from examples import *
from assignments import *
from classes import *
#global variables


def closeprogram ():
    root.quit()
      
class Application (Frame):

  def __init__ (self, master):
    """ initialize the frame"""
    Frame.__init__ (self, master)
    self.grid ()
    self.master=master
    self.file1=""       #name of file1
    self.file2=""       #name of file2
    self.file3=""       #name of file 3
    self.array0 = []    #list of words derived from input textbox
    self.array1 = []    #list of words derived from file1
    self.array2 = []    #list of words derived from file2
    self.array3 = []   #list of words derived from file
    self.create_widgets ()

  def openfile(self, fileno):
      temparray =[]
      if fileno==1:
        self.file1 = tkFileDialog.askopenfilename()
        self.statusbar1.delete("1.0", END)
        # print (self.file1)
        self.statusbar1.insert("1.0", self.file1)
        text_file = open(self.file1, "r")
        temparray = re.sub("[^\w]", " ", text_file.read()).split() #excluding space characters
        temparray = [item.lower() for item in temparray]  #converting all words to lower case
        for i in range (0, len (temparray)):  #Excludng stopwords from self.array1
            if temparray [i] not in STOPWORDS:
                 self.array1.append (temparray [i])

        
      if fileno==2:
       self.file2 = tkFileDialog.askopenfilename()
       self.statusbar2.delete("1.0", END)
       # print (self.file1)
       self.statusbar2.insert("1.0", self.file2)
       text_file = open(self.file2, "r")
       temparray = re.sub("[^\w]", " ", text_file.read()).split()  #excluding space characters
       temparray = [item.lower() for item in temparray]   #converting all words to lower case
       for i in range (0, len (temparray)):  #Excludng stopwords from self.array2
           if temparray [i] not in STOPWORDS:
                 self.array2.append (temparray [i])

     
      if fileno == 3:
        self.file3 = tkFileDialog.askopenfilename()
        self.statusbar3.delete("1.0", END)
        # print (self.file1)
        self.statusbar3.insert("1.0", self.file3)
        text_file = open(self.file3, "r")
        temparray = re.sub("[^\w]", " ", text_file.read()).split()  #excluding space characters
        temparray = [item.lower() for item in temparray]   #converting all words to lower case
        for i in range (0, len (temparray)):  #Excludng stopwords from self.array3
            if temparray [i] not in STOPWORDS:
                  self.array3.append (temparray [i])
        
      self.upload_btn.config (state=NORMAL, background='cadetblue') 


  def create_widgets (self):

    self.logo = Label(self, text="Smart Text Analyzer!", fg="blue", font = "Verdana 14 bold" )
    self.logo.grid(row=1, column=0, sticky=W+E+N+S)
    self.instruction = Label(self, text="Type your text:", font = "Verdana 13 italic")
    self.instruction.grid(row=3, column=0, sticky=W)


    self.input_txt = Text(self, width=40, height=14, borderwidth=3, bg="salmon", relief="sunken", font=("consolas", 12), undo=True,
                      wrap=WORD)
    self.input_txt.grid(row=4, column=0, sticky=W+E+N+S)


    self.fileupload_btn1=Button (self, text="Choose text file 1....", foreground="red", background="blue",  command=lambda i=1: self.openfile (i))
    self.fileupload_btn1.config (foreground='green')
    self.fileupload_btn1.grid (row= 6, column=0, sticky=W)

    self.statusbar1 = Text(self, width=30, height=1, borderwidth=1, bg= "yellow", relief="sunken", font=("consolas", 12))
    self.statusbar1.grid(row= 7, column=0)

    self.fileupload_btn2 = Button(self, text="Choose text file 2....", command=lambda i=2: self.openfile (i))
    self.fileupload_btn2.grid(row=8, column=0, sticky=W)

    self.statusbar2 = Text(self, width=30, height=1, borderwidth=1, bg= "yellow",relief="sunken", font=("consolas", 12))
    self.statusbar2.grid(row=10, column=0)

    self.fileupload_btn3 = Button(self, text="Choose text file 3....", command=lambda i=3: self.openfile (i))
    self.fileupload_btn3.grid(row=11, column=0, sticky=W)

    self.statusbar3 = Text(self, width=30, height=1, borderwidth=1, bg="yellow",relief="sunken", font=("consolas", 12))
    self.statusbar3.grid(row=13, column=0)

    self.upload_btn = Button(self, text="Upload inputs...", command=self.upload)
    self.upload_btn.grid(row=14, column=0, sticky=W)

    self.clear_btn = Button(self, text="Clear entries...", command=self.clear_entries)
    self.clear_btn.grid(row=14, column=0, sticky=E)



#this method stores the text in the input textbox into array0 and removes its common words
  def upload (self):
     temparray= []
     mystr = self.input_txt.get("1.0", 'end-1c')
     self.array0[:]=[]
     temparray = re.sub("[^\w]", " ", mystr).split()  #excluding space characters
     temparray = [item.lower() for item in temparray]   #converting all words to lower case
     for i in range (0, len (temparray)):  #Excludng stopwords from self.array0
         if temparray [i] not in STOPWORDS:
                 self.array0.append (temparray [i])
     #mergedarray=merge (self.a0, self.a1, self.a2, self.a3)
     createinputfile(self.array0, self.array1, self.array2, self.array3)




 #this method stores the text from the input sources into array0,1,2,3 without removing its common words
  def upload2 (self):
      #loading array 0
     temparray= []
     mystr = self.input_txt.get("1.0", 'end-1c')
     self.array0[:]=[]
     temparray = re.sub("[^\w]", " ", mystr).split()  #excluding space characters
     temparray = [item.lower() for item in temparray]   #converting all words to lower case
     for i in range (0, len (temparray)):            
               self.array0.append (temparray [i])
      #loading array1
     if (self.file1!=""):
       temparray= []
       self.array1[:]=[]
       text_file = open(self.file1, "r")
       temparray = re.sub("[^\w]", " ", text_file.read()).split() #excluding space characters
       temparray = [item.lower() for item in temparray]  #converting all words to lower case
       for i in range (0, len (temparray)):  
                 self.array1.append (temparray [i])
     #loading array2
     if (self.file2!=""):
       temparray= []
       self.array2[:]=[]
       text_file = open(self.file2, "r")
       temparray = re.sub("[^\w]", " ", text_file.read()).split() #excluding space characters
       temparray = [item.lower() for item in temparray]  #converting all words to lower case
       for i in range (0, len (temparray)):  
                 self.array2.append (temparray [i])

 #loading array3
     if (self.file3!=""):
       temparray= []
       self.array3[:]=[]
       text_file = open(self.file3, "r")
       temparray = re.sub("[^\w]", " ", text_file.read()).split() #excluding space characters
       temparray = [item.lower() for item in temparray]  #converting all words to lower case
       for i in range (0, len (temparray)):  
                 self.array3.append (temparray [i])
                
  def normal1(self):
      if (sizeof(self.array0+self.array1+self.array2+self.array3) ==0):
              tkMessageBox.showinfo("Warning!", "Ther is not any input to do the analysis!")
      else:
          normal()  #calling normal method from wordcloudtemplate module
          
  def hope1(self):
      if (sizeof(self.array0+self.array1+self.array2+self.array3) ==0):
              tkMessageBox.showinfo("Warning!", "Ther is not any input to do the analysis!")
      else:
          hope()  #calling hope method from wordcloudtemplate module

  def bird1(self):
      if (sizeof(self.array0+self.array1+self.array2+self.array3) ==0):
              tkMessageBox.showinfo("Warning!", "Ther is not any input to do the analysis!")
      else:
          bird()  #calling bird method from wordcloudtemplate module

  def heart1(self):
      if (sizeof(self.array0+self.array1+self.array2+self.array3) ==0):
              tkMessageBox.showinfo("Warning!", "Ther is not any input to do the analysis!")
      else:
          heart()  #calling heart method from wordcloudtemplate module         
          
  def searching_a_pattern (self):
      if (sizeof(self.array0+self.array1+self.array2+self.array3) ==0):
              tkMessageBox.showinfo("Warning!", "Ther is not any input to do the analysis!")
      else:        
             root.withdraw()
             search_pattern_window (self.master, self.array0, self.array1, self.array2, self.array3)

      
  def trend_of_top_words (self):
      if (sizeof(self.array0+self.array1+self.array2+self.array3) ==0):
              tkMessageBox.showinfo("Warning!", "Ther is not any input to do the analysis!")
      else:        
              trends (self.array0+self.array1+self.array2+self.array3)

  def example1_assignment (self):
      example_str = self.input_txt.get("1.0", 'end-1c')
      example1_main_routine (example_str.strip())

  def example2_assignment (self):
     """example_str = self.input_txt.get("1.0", 'end-1c')"""
     
     self.upload2 ()
     example2_main_routine (self.array0+self.array1+self.array2+self.array3)


  def assignments_assignment1 (self):     #similarity percentage assignment
     assignment1 (self.array1,self.array2)

  def assignments_assignment2 (self):     #sentiment analysis assignment
      # making positive and negative words arrays
       positivewords= []
       text_file = open("positivewords.txt", "r")
       positivewords = re.sub("[^\w]", " ", text_file.read()).split() #excluding space characters
       positivewords = [item.lower() for item in positivewords]  #converting all words to lower case

       negativewords= []
       text_file = open("negativewords.txt", "r")
       negativewords = re.sub("[^\w]", " ", text_file.read()).split() #excluding space characters
       negativewords = [item.lower() for item in negativewords]  #converting all words to lower case

       self.upload2 ()   #making array0,1,2,3 including common words
       allarrays=[]
       allarrays= self.array0+self.array1+self.array2+self.array3   #combining the content of all arrays
       
       assignment2 (allarrays, positivewords, negativewords)   

  def assignments_assignment3 (self):     #repeating pattern assignment
      
       self.upload2 ()   #making array0,1,2,3 including common words
       allarrays=[]
       allarrays= self.array0+self.array1+self.array2+self.array3   #combining the content of all arrays
       
       assignment3 (allarrays)

  def assignments_assignment4 (self):     #url recognition assignment
      
       self.upload2 ()   #making array0,1,2,3 including common words
       allarrays=[]
       allarrays= self.array0+self.array1+self.array2+self.array3   #combining the content of all arrays
       
       assignment4 (allarrays)

  def assignments_assignment5 (self):     #email recognition assignment
      
       self.upload2 ()   #making array0,1,2,3 including common words
       allarrays=[]
       allarrays= self.array0+self.array1+self.array2+self.array3   #combining the content of all arrays
       
       assignment5 (allarrays)

  def assignments_assignment6 (self):     #free assignment
      
       self.upload2 ()   #making array0,1,2,3 including common words
       
       assignment6 (self.array0, self.array1, self.array2, self.array3)    
      
  def clear_entries (self):
      self.input_txt.delete ('1.0', END)
      self.statusbar1.delete ('1.0', END)
      self.statusbar2.delete ('1.0', END)
      self.statusbar3.delete ('1.0', END)
      self.file1=""     
      self.file2=""     
      self.file3=""       
      self.upload_btn.config (state=DISABLED, background='cadetblue')
      #delete input file if exists
      d = path.dirname(__file__)
      if os.path.exists(path.join(d, 'input.txt')):
         os.remove(path.join(d, 'input.txt'))
      #clearing arrays0,1,2,3
      self.array0 [:]=[]
      self.array1 [:]=[]
      self.array2 [:]=[]
      self.array3 [:]=[]
      


root=Tk ()
root.title ("text visualizer")
w = 300 # width for the Tk root
h = 470 # height for the Tk root

ws, hs = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(0)
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
#root.geometry ("%dx%d+0+0" % (w*2/13, h*4/9))
app = Application (root)
menu=Menu (root)
root.config (menu=menu)
Submenu =Menu (menu)
menu.add_cascade(label="Generate Word Cloud", menu=Submenu)
Submenu.add_command(label= "Normal", command= app.normal1)
#Submenu.add_command(label= "Alice 1", command= alice1)
#Submenu.add_command(label= "Alice 2", command= alice2)
Submenu.add_command(label= "Hope", command= app.hope1)
Submenu.add_command(label= "Bird", command= app.bird1)
#Submenu.add_command(label= "Gun", command= gun)
Submenu.add_command(label= "Heart", command= app.heart1)
Submenu.add_separator()
Submenu.add_command(label= "Exit", command= closeprogram)

editMenu= Menu(menu)
menu.add_cascade(label="Analysis", menu=editMenu)
editMenu.add_command(label= "Search", command= app.searching_a_pattern)
editMenu.add_command(label= "Top Words", command= app.trend_of_top_words)
#editMenu.add_command(label= "Example 1", command= app.example1_assignment)
#editMenu.add_command(label= "Example 2", command= app.example2_assignment)
#editMenu.add_command(label= "Similarity Percentage", command= app.assignments_assignment1)
#editMenu.add_command(label= "Sentiment Analysis", command= app.assignments_assignment2)

exampleMenu= Menu(menu)
menu.add_cascade(label="Examples", menu=exampleMenu)
exampleMenu.add_command(label= "Example 1", command= app.example1_assignment)
exampleMenu.add_command(label= "Example 2", command= app.example2_assignment)
#editMenu.add_command(label= "Similarity Percentage", command= app.assignments_assignment1)
#editMenu.add_command(label= "Sentiment Analysis", command= app.assignments_assignment2)




assignmentMenu= Menu(menu)
menu.add_cascade(label="Asignments", menu=assignmentMenu)
assignmentMenu.add_command(label= "Similarity Percentage", command= app.assignments_assignment1)
assignmentMenu.add_command(label= "Sentiment Analysis", command= app.assignments_assignment2)
assignmentMenu.add_command(label= "Repeating Pattern", command= app.assignments_assignment3)
assignmentMenu.add_command(label= "Url Recognition", command= app.assignments_assignment4)
assignmentMenu.add_command(label= "Email Recognition", command= app.assignments_assignment5)
assignmentMenu.add_command(label= "Free assignment", command= app.assignments_assignment6)

root.mainloop ()



# learning point
# how to disable a button self.fileupload_btn1.config (state=DISABLED, background='cadetblue')
