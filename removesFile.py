import os
import shutil 
import time

def removeFiles():
    file1=input("enter file name")
    
    with open(file1,'r')as a:
        data_a = a.read()
    
    with open(file1)as a:
        a.delete
    

removeFiles()