'''
Created on Nov 10, 2017

@author: Anupsingh Pardeshi
'''
import requests
from bs4 import BeautifulSoup
from wsgiref.util import application_uri
from Sources.ObjectModel.AppDetails import AppDetails
from multiprocessing import Pool

#Crawler class to crawl the app web link and extract the data.
class Crawler:
    
    #def MultiProCrawling(self, appList):
        
        #with Pool(10) as P:
          #  p.Map
    
    def GooglePlayCrawler(self, appList):
        #List for Application Objects
        applicationsObjects = []
        
        #Iterating through the Application list of Urls to fetch the contents of an app
        for appLink in appList:
            appDetails = AppDetails()
            sourceCode = requests.get(appLink)
            rawText = sourceCode.text
            soupObj = BeautifulSoup(rawText,"html.parser")
        
            #User Rating
            for score in soupObj.find_all(attrs={'class': 'score'}):
                appDetails.rating = score.text
                #print(appDetails.rating)
        
            #Number of Reviews
            for totalReviews in soupObj.find_all(attrs={'class': 'reviews-num'}):
                appDetails.totalReviews = totalReviews.text
                #print(appDetails.totalReviews)
        
            #Genere
            for genere in soupObj.find_all(attrs={'itemprop': 'genre'}):
                appDetails.genere = genere.text
                #print(appDetails.genere)
        
            #Developer
            for dev in soupObj.find_all(attrs={'class': 'document-subtitle primary'}):
                appDetails.author = dev.text.strip()
                #print(appDetails.author)
            
            #Installs
            for pull in soupObj.find_all(attrs={'itemprop': 'numDownloads'}):
                appDetails.Installs = pull.text.strip()
                #print(appDetails.Installs)
        
            #Content
            for contents in soupObj.find_all(attrs={'itemprop': 'contentRating'}):
                fetchedContents = contents.text
           
                if(fetchedContents.count('Mature') | fetchedContents.count('+')):
                    appDetails.adult = True
            
            applicationsObjects.append(appDetails)
        
        return applicationsObjects
        