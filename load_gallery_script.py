
import os
import re

def load_gallery_script():
   f = open("C:\\Users\\Jeannius\\Documents\\IntelliJ Projects\\Python projects\\New folder\\LG2200-2008-03-11_13\\2008-03-11_13\\02463\\02463.txt", "r")

   str =""
   for line in f.readlines():
       if line !='\n':
           str += line
       else:
        create_stuff(str)
        break
        str=""




def create_stuff(arr):
    dict = {'iris_code':''}
    for line in arr.splitlines():
        if 'subjectid' in line:
            list_of_words = line.split()
            subjectid= list_of_words[list_of_words.index('string')+1]
            dict['id']= subjectid
    print(dict)
    return dict



load_gallery_script()