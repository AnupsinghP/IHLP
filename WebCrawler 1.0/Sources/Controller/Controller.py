'''
Created on Sep 28, 2017

@author: Anupsingh Pardeshi
'''
from Sources.Modules.Spider import SpiderClass
from Sources.Modules.Crawler import Crawler
from Sources.DataHandler.ExcelHandler import ExcelHandlerClass

#Controller class controls and manages the workflow between application
class Controller:

    #Use spider to crawl the particular web site using SpiderClass
    #Creating the object for the Spider class
    spiderObj = SpiderClass()        
    
    #Creating crawler to crawl all the information from the app web link
    #Creating the object for the crawler class
    crawlerObj = Crawler()
    
    urlsList = spiderObj.Spider(2)
   
    #Using main process to create child processes which will fetch the details of fetched app links
    if __name__ == '__main__':
        
        detailsList = crawlerObj.Crawl(urlsList)
    
        #TO-DO Call data handler to handle data
        DBHandler = ExcelHandlerClass()
    
        DBHandler.CollectData(detailsList)