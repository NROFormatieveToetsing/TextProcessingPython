#                                                     assignments
from examples import *
from process import *
import Tkinter
import tkMessageBox
#====================== you can use the following functions to write your program ===============================
#asort (arr) :  this function receives array a and sort it. Note that this function changes the order of elements in array a  
#simple_search (keyword , arr): this function checks whether value keyword exists in array arr and return 1 (if exists) or 0 (if not exist).
#sizeof (arr): this function returns the length of array arr.
#word_frequency_in_array (keyword , arr): this function calculates the frequency of word p in array arr.
#array_unique (arr): this function receives array arr and removes its duplicate elements and returns an array with non-duplicated elements.
#================================================================================================================ 
        #==========Assignment 1: similarity percentage==========#
            
#================================================================================================================ 

def assignment1 (a,b):
    len_a = sizeof (a)   #size of array a
    len_b= sizeof (b)    #size of array b
    similarity=0         #to store the similarit between a and b

    '''
     write you code here

    '''
    tkMessageBox.showinfo("Similarity percentage", str(similarity))
     

#================================================================================================================ 
        #==========Assignment 2: Sentiment Analysis ==========#
            
#================================================================================================================ 
def assignment2 (a,positivewords, negativewords):
    len_a = sizeof (a)                   #size of array a
    len_pos= sizeof (positivewords)
    len_neg=sizeof (negativewords)
    sentiment = 0

    '''
     write you code here

    '''
    tkMessageBox.showinfo("Sentiment Analysis:", str(sentiment))

#================================================================================================================ 
        #==========Assignment 3: Longest Repeating Pattern ==========#
            
#================================================================================================================ 
def assignment3 (a):
    len_a = sizeof (a)

    longest_pattern = ""

    '''
     write you code here

    '''
    tkMessageBox.showinfo("Longest Repeating Pattern", longest_pattern)    

#================================================================================================================ 
        #==========Assignment 4: URL Recognition ==========#
            
#================================================================================================================ 
def assignment4 (a):
    len_a = sizeof (a)

    urls = ""

    '''
     write you code here

    '''
    tkMessageBox.showinfo("Recognized URLs", urls)    

#================================================================================================================ 
        #==========Assignment 5: EMAIL Recognition ==========#
            
#================================================================================================================ 
def assignment5 (a):
    len_a = sizeof (a)

    emails = ""

    '''
     write you code here

    '''
    tkMessageBox.showinfo("Recognized Emails", emails)    

#================================================================================================================ 
        #==========Assignment 6: Free Assignment ==========#
            
#================================================================================================================ 
def assignment6 (a,b,c,d):    #array a,b,c,d: contains words from text box,file 1, file 2, file 3 
    len_a = sizeof (a)       
    len_b = sizeof (b)
    len_c = sizeof (c)
    len_d = sizeof (d)   

    '''
     write you code here

    '''
    tkMessageBox.showinfo("Free assignment", "your message")    
