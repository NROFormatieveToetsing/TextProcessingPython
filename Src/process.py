from os import path
import Tkinter as tk
import matplotlib.pyplot as plt
import numpy as np


def simple_search (keyword , arr):  # test for emptiness and for membership
    if keyword in arr: 
        return 1
    else:
        return 0

def textlen (t):
    i = 0
    for c in t:
        if c == "":
            break
        else:
            i = i + 1

    return i


def cuttext (t, i, lent): 
    s = ""
    j = i+1
    while (j < lent):
        s= s + t[j]
        j = j + 1
    return (s)





def substr(*arg):  #this function receives 2 or three parameters:string, start, [l] and returns a slice of string starting from start with length of l
                    #... if l is not defined it returns a slice from start to the end of the string
  a= len (arg[0])
  if len (arg)==2: #only array and start positin has been sent
     return arg[0][arg[1]:a]  #slicing array arr[begining:]
  if len (arg) ==3:
     return arg[0][arg[1]:arg[1]+arg[2]]  #slicing array arr[begining:begining+length] 


def match_pattern (pattern,string): #this function receives a pattern and a string and checks if all characters of the string matches the pattern

  for i in range (0, len(string)):
      if (search_char_in_string(string[i],pattern) == -1000):
               return False
  return True    


def findnumber (k):
    s= ""
    j = 0
    lent= textlen (k)
    while (j < lent):
     
        if k[j] in "0123456789":
           s= s + k[j]
        else:
            break
        j = j + 1
    return (s)


    
def text_equals (p,q):
    if textlen (p) != textlen (q):
         return (0)
    for i in range (0, textlen (p)):
         if p[i].lower() != q[i].lower():
            return (0)
    return (1)

def word_frequency_in_array (p,a):  #this function calculates the frequency of parameter p in array a and return it
      cnt=0 
      for i in range(0, len(a)):
                 if text_equals (p , a[i])== 1:
                    cnt+=1
      return (cnt)


def search_in_array (keyword , arr): #this function checks whether value k exists in array arr and return its index (if exists) or -1000 (if not exist).

    i=0
    for i in range (0, len(arr)):
       if keyword == arr[i]:
           return (i)
    return (-1000)

def search_char_in_string (ch, string): #this function searches character c in string s and returns the index of its first occourance otherwise return -1000

    for i in range (0, len(string)):
        if ch==string[i]:
            return (i)
    return (-1000)    



    

def array_unique (a): #this function receives array arr and remove duplicated elements and return a new array without duplicated elements
      temp = a
      asort (temp)
      uarray = []  # includes all words sorted without repetions
      #farray = []  # includes frequencies for each item of uarray
      index = 0
      i = 0
      while i < len(temp):
          uarray.append (temp[i])
          #farray.append(1)
          cnt = 1
          j = i + 1
          if j >= len(temp):
              break
          while ( j<len (temp)):
              if temp[i] == temp[j]:
                j += 1
                cnt += 1
              else:
                 break
          #farray [index]=cnt
          i = i + cnt
          index=index+1
      #print ("array uarray in find_frequency_of_words func:", uarray)
      #print ("array farray in find_frequency_of_words func:", farray)    
      return (uarray)
    

def simplesort (a, sorttype):  #Ascending sort for sort type = 'A', descending sort for sort type='D'
    #sortedarray= [] 
    for i in range(0, len(a)):
          for j in range(i + 1, len(a)):
              if sorttype=='A':
                 if a[j] <= a[i]:
                      temp = a[i]
                      a[i] = a[j]
                      a[j] = temp
                      
              if sorttype=='D':
                 if a[j] >= a[i]:
                      temp = a[i]
                      a[i] = a[j]
                      a[j] = temp
                      
    return (a)

def sizeof (a):    # to be used in assignments module meant to be compatible with php document
    return (len(a))

def asort (a):  #Ascending sort  to be used in assignments module meant to be compatible with php document
   
    for i in range(0, len(a)):
          for j in range(i + 1, len(a)):
              
                 if a[j] <= a[i]:
                      temp = a[i]
                      a[i] = a[j]
                      a[j] = temp
                                
    return (a)

def merge(a0, a1):   #this function recieves two arrays a0 and a1 and merge them
      temparray = []
      for i in range(0, len(a0)):  
          temparray.append(a0[i]+' ')
      for i in range(0, len(a1)):  
          temparray.append(a1[i]+' ')

      return (temparray)

"""def createinputfile (a0, a1, a2, a3):
      merged= merge(a0, a1, a2, a3)
      sorted=simplesort (merged)
      d = path.dirname(__file__)
      file = open(path.join(d, 'input.txt'), "w")
      file.writelines(sorted)
      file.close()"""

def createinputfile (a0, a1, a2, a3):  #this function recieves four arrays a0, a1,a2,a3 and create a file consisting of these arrays
      merged1= merge(a0, a1)
      merged2= merge(a2, a3)
      merged3= merge(merged1, merged2)
      #sorted=simplesort (merged)
      d = path.dirname(__file__)
      file = open(path.join(d, 'input.txt'), "w")
      file.writelines(merged3)
      file.close()


def find_frequency_of_words (a):  #this function recieves sorted array a and calculate the frequency of words in this array 
      uarray = []  # includes all words sorted without repetions
      farray = []  # includes frequencies for each item of uarray
      index = 0
      i = 0
      while i < len(a):
          uarray.append (a[i])
          farray.append(1)
          cnt = 1
          j = i + 1
          if j >= len(a):
              break
          while ( j<len (a)):
              if a[i] == a[j]:
                j += 1
                cnt += 1
              else:
                 break
          farray [index]=cnt
          i = i + cnt
          index=index+1
      #print ("array uarray in find_frequency_of_words func:", uarray)
      #print ("array farray in find_frequency_of_words func:", farray)    
      return (uarray, farray)

def sort_frequency (f, w):  #this function receives two associated arrays f and w and sorts array f and change elements of array w accordingly

    for i in range(0, len(f)):
          for j in range(i + 1, len(f)):
                 if f[j] >= f[i]:
                      tempf = f[i]
                      f[i] = f[j]
                      f[j] = tempf
                      tempw=w[i]
                      w[i]=w[j]
                      w[j]=tempw
    return (w,f)


def calculatetopwords(a):  #this function receives an array and then creates two arrays consisting top words and frequency of top words
      # first sorting array a
      sortedarray = []  # includes all words sorted and with repetition
      words= []         #includes all words without repetionn
      frequency= []     #includes frequency of words in the words array  
    
      sortedarray=simplesort (a, 'A')   #sort array a in Ascending manner

      #print ("array sortedarray in calculatetopwords func:", sortedarray)     

      words, frequency = find_frequency_of_words (sortedarray)
      #now we need to do descending sort of frequency array and also change words array accordingly
      words, frequency = sort_frequency (frequency, words)
      return (words, frequency)  #these two arrays include words and and their frequency sorted based on frequency
    
def create_plot_top_words (topwords, frequency_of_top_words, no_of_items_to_plot): #this function create a plot. x-axis: topwords, y-axis:frequency-of-top-words
      my_x= []
      for i in range (0, no_of_items_to_plot):
          my_x.append (i)
        
      x = np.asarray(my_x)
      #x = np.array([0,1,2,3])
      my_y= frequency_of_top_words [0:no_of_items_to_plot]
      #y = np.array([20,21,22,23])
      y=np.asarray (my_y)
      my_xticks = topwords [0:no_of_items_to_plot]
      plt.tick_params(axis='x', colors='green')
      plt.xticks(x, my_xticks, rotation=30, fontsize=10)
      plt.plot(x, y)
      plt.show()

def trends (a):
      topwords= []
      #print ("array a in trends func:", a)
      frequency_of_top_words = []
      topwords, frequency_of_top_words=calculatetopwords(a)
      #print (topwords)
      #print (frequency_of_top_words)
      create_plot_top_words (topwords, frequency_of_top_words, 30)  #30 is the number of words to show


def frequency_in_array (p,a):  #this function calculates the frequency of parameter p in array a and return it
      cnt=0 
      for i in range(0, len(a)):
                 if p == a[i]:
                    cnt+=1
      return (cnt)
    
def plot_pattern (p1,p2, p3, p4, p5, a0,a1, a2, a3): #this function calculates the frequency of strings p1, p2, p3, p4, p5 in arrays a0, a1, a2, a3 and plots these frequencies
      fr_p1=[0,0,0,0]
      fr_p2=[0,0,0,0]
      fr_p3=[0,0,0,0]
      fr_p4=[0,0,0,0]
      fr_p5=[0,0,0,0]
      
      fr_p1 [0]= frequency_in_array (p1, a0)
      fr_p1 [1]= frequency_in_array (p1, a1)
      fr_p1 [2]= frequency_in_array (p1, a2)
      fr_p1 [3]= frequency_in_array (p1, a3)

      fr_p2 [0]= frequency_in_array (p2, a0)
      fr_p2 [1]= frequency_in_array (p2, a1)
      fr_p2 [2]= frequency_in_array (p2, a2)
      fr_p2 [3]= frequency_in_array (p2, a3)

      fr_p3 [0]= frequency_in_array (p3, a0)
      fr_p3 [1]= frequency_in_array (p3, a1)
      fr_p3 [2]= frequency_in_array (p3, a2)
      fr_p3 [3]= frequency_in_array (p3, a3)

      fr_p4 [0]= frequency_in_array (p4, a0)
      fr_p4 [1]= frequency_in_array (p4, a1)
      fr_p4 [2]= frequency_in_array (p4, a2)
      fr_p4 [3]= frequency_in_array (p4, a3)

      fr_p5 [0]= frequency_in_array (p5, a0)
      fr_p5 [1]= frequency_in_array (p5, a1)
      fr_p5 [2]= frequency_in_array (p5, a2)
      fr_p5 [3]= frequency_in_array (p5, a3)

      my_x=[0,1,2,3]
      x = np.asarray(my_x)
      #x = np.array([0,1,2,3])
      #my_y= frequency_of_top_words [0:no_of_items_to_plot]
      #y = np.array([20,21,22,23])
      y=np.asarray (fr_p1)
      my_xticks = ["source1", "source2", "source3", "source4"]
      plt.tick_params(axis='x', colors='green')
      plt.xticks(x, my_xticks, rotation=30, fontsize=10)
      plt.plot(x, y)
      y=np.asarray (fr_p2)
      plt.plot (x, y)
      y=np.asarray (fr_p3)
      plt.plot (x, y)
      y=np.asarray (fr_p4)
      plt.plot (x, y)
      y=np.asarray (fr_p5)
      plt.plot (x, y)
      plt.legend([p1, p2, p3, p4, p5], loc='upper left')
      plt.show()


