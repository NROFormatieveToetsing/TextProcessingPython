def generatesimplewordcloud (self):

    content, weights= self.processinput ()



    colours=['red', 'blue','green', 'purple']
    #print (weights)
    r=1
    c=0
    self.output_txt.config (borderwidth=3, relief="sunken")
    self.output_txt.delete("1.0", END)
    for i in range (0,len (content)):

      #print (content [i], weights [i])
      self.output_txt.insert(END, content [i])
      start_idx= str (r)+'.'+str (c)
      c += len(content[i])
      end_idx= str (r)+'.'+str (c)
      self.output_txt.tag_add("tag"+str (i), start_idx, end_idx)
      self.output_txt.tag_config("tag"+str (i), background='white', foreground=colours [int(random.random ()*4)],
                                 font=('times', int ((weights [i]/min (weights))* 6)+10, 'normal'))
