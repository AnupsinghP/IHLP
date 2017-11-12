'''
Created on Nov 10, 2017

@author: Anupsingh Pardeshi
'''
import requests
from bs4 import BeautifulSoup
from wsgiref.util import application_uri

#Spider Class to gather all the app web links for the analyzation.
class SpiderClass:
    
    def Spider(self, limit):
        page = 1
        
        list = []
        
        while page < limit:
            url ='https://play.google.com/store/apps/new'
            
            source_Code = requests.get(url)
            
            raw_text = source_Code.text
        
            soup = BeautifulSoup(raw_text, "html.parser")
          
            for link in soup.find_all('a',{'class': 'title'}):
                hreff = "https://play.google.com" + link.get('href')
            
                if((list.__contains__(hreff))!= True):
                    list.append(str(hreff))
            page += 1
        
        return list
        
    #print(list)    
    