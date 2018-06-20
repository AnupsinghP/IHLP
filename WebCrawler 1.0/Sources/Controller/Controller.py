'''
Created on Sep 28, 2017

@author: Anupsingh Pardeshi
'''
from Sources.Modules.Crawler import Crawler
from Sources.Modules.Spider import SpiderClass
from Sources.DataHandler.CSVHandler import CSVHandlerClass

#Controller class controls and manages the workflow between application
class Controller:
    #Data Hanler Class
    #TO-DO Call data handler to handle data
    DBHandler = CSVHandlerClass()
    
    fetchedUrlsList = DBHandler.FetchedUrls()
    
    #Use spider to crawl the particular web site using SpiderClass
    #Creating the object for the Spider class
    spiderObj = SpiderClass()      
    
    #Creating crawler to crawl all the information from the app web link
    #Creating the object for the crawler class
    crawlerObj = Crawler()
    
    urlsList = spiderObj.Spider(2)
    
    pendingUrlsList = []
    
    if(len(fetchedUrlsList) > 0):
        pendingUrlsList = crawlerObj.Cleaner(urlsList, fetchedUrlsList)
    else:
        pendingUrlsList = urlsList
    
    #Using main process to create child processes which will fetch the details of fetched app links
    if __name__ == '__main__':
        
        if(len(pendingUrlsList) > 0):
            detailsList = crawlerObj.Crawl(pendingUrlsList)
        
            print(len(detailsList))
    
            r = DBHandler.CollectAppDetails(detailsList)
        
            print(r+1)
