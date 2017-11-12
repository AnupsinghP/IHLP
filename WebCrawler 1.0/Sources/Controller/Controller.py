'''
Created on Sep 28, 2017

@author: Anupsingh Pardeshi
'''
import requests
from bs4 import BeautifulSoup
from wsgiref.util import application_uri
from Sources.ObjectModel.AppDetails import AppDetails
from Sources.Modules.Spider import SpiderClass
from Sources.Modules.Crawler import Crawler 
from Sources.CSVHandler.CSVHandlerClass import CSVHandlerClass


#Controller class controls and manages the workflow between application
class Controller:

    #Use spider to crawl the particular web site using SpiderClass
    #Creating the object for the Spider class
    spiderObj = SpiderClass()        
    
    #Creating crawler to crawl all the information from the app web link
    #Creating the object for the crawler class
    crawlerObj = Crawler()

    #Excel File handler
    csvHandler = CSVHandlerClass()
    
    #trackingList = spiderObj.Spider(2)

    #applicationObjectsList = crawlerObj.GooglePlayCrawler(trackingList)
    

    
    #print(applicationObjectsList)

