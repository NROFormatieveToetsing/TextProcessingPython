from process import *
import Tkinter
import tkMessageBox
 



def example1_main_routine (t):
     s=" "
     lent= textlen (t)
     for i in range(0, lent):
         if t[i] =='#':
             t1 = cuttext (t, i, lent)
             number = findnumber (t1)
             if number <> "":
               #print ('#'+ number)
                s = s + '#' + number +'\n'
                  
     tkMessageBox.showinfo("Example 1: #number pattern", s)
         
         

    
def example2_main_routine (t):
   
    max_frequency = 0
    temp = ""
    cnt = 0
    for i in range(0, len(t)):
        cnt = word_frequency_in_array (t[i],t)
        if cnt > max_frequency:
            temp = t[i] 
            max_frequency = cnt     

    #print (temp, max_frequency)
    tkMessageBox.showinfo("Example 2: Most frequent word", temp + ' ('+ str (max_frequency) +')')
    

    
