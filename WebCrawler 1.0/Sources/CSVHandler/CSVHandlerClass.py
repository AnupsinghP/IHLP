'''
Created on Nov 11, 2017

@author: Anupsingh Pardeshi
'''
import os
import pathlib
from pathlib import Path
import csv
from lib2to3.fixer_util import Newline

class CSVHandlerClass:
    
    def __init__(self):
        filePath =r'C:\Users\Anupsingh Pardeshi\Desktop\IHLP\Project\ApplicationData.csv'
        
        if (os.path.isfile(filePath)!= True):   
            with open(r'C:\Users\Anupsingh Pardeshi\Desktop\IHLP\Project\ApplicationData.csv', 'wb') as csvfile:
                fieldNames = ['Application Name','Rating','Installs','Genere','Installations','AgeBar','Price','Total Ratings']
                
                theWriter = csv.DictWriter(csvfile, fieldnames=fieldNames)
                theWriter.writeheader()
                theWriter.writerow({'Application Name' : '1a','Rating' :'2a','Installs' :'3a','Genere' :'4a','Installations' :'5a','AgeBar' :'6a','Price' : '7a','Total Ratings' : '8a'})
    
            