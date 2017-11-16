'''
Created on Nov 10, 2017

@author: Anupsingh Pardeshi
'''
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import threading
from asyncio.log import logger
import re
from Sources.ObjectModel.AppDetails import AppDetails

#Crawler class to crawl the app web link and extract the data.
class Crawler:
            
    def Crawl(self,appList):
       
        try:
            appPool = Pool()
        
            result = appPool.map(self.GooglePlayStoreCrawler, appList)
        
            appPool.close()
        
            appPool.join()
            
            return result
                    
        except Exception as e:
            logger.critical(e)
       
        self.GooglePlayStoreCrawler(appList)
        
    
    def GooglePlayStoreCrawler(self, appLink):
         
        #for appLink in appList:
        appDetails = AppDetails()
        
        #print(appLink)
        sourceCode = requests.get(appLink)
        rawText = sourceCode.text
        soupObj = BeautifulSoup(rawText,"html.parser")
    
        #Thread for title
        tTitle = threading.Thread(target=self.GetTitle, args=(soupObj, appDetails))
                   
        #Thread for ratings
        tReviews = threading.Thread(target=self.GetRatings,args=(soupObj, appDetails))
        
        #Thread for price
        tPrice = threading.Thread(target=self.GetPrice, args=(soupObj, appDetails))
            
        #Thread for total Reviewers
        tTotalReviewers = threading.Thread(target=self.GetTotalReviewers, args=(soupObj, appDetails))
            
        #Thread for Genere
        tGenere = threading.Thread(target=self.GetGenere, args=(soupObj, appDetails))
                       
        #Thread for author
        tAuthor = threading.Thread(target=self.GetDeveloper, args=(soupObj, appDetails))
            
        #Installs
        tInstalls = threading.Thread(target=self.GetInstalls, args=(soupObj, appDetails))
                        
        #Content
        tContent = threading.Thread(target=self.GetContent, args=(soupObj, appDetails))
    
        threadList = [tTitle, tGenere, tPrice, tAuthor, tContent, tInstalls, tReviews, tTotalReviewers]
            
        try:
                
            #Initializing the threads
            for threadApp in threadList:
                threadApp.start()
                
            #Waiting for threads to complete their tasks    
            for threadApp in threadList:
                threadApp.join()
            
        except Exception as e: 
            logger.log("Exception caught in threading in Crawler Class: ", e)
                        
        
        return appDetails
    
    def GetPrice(self, soupObj, appDetails):
        priceList = soupObj.find('button',{'class': 'price buy id-track-click id-track-impression'})
        
        priceRaw = priceList.find_all('span')
            
        priceLast = priceRaw[(len(priceRaw)-1)]
                  
        price =  priceLast.text
        
        if ("Install" in price):
            appDetails.price = 0
        elif("Buy" in price):
            price = re.sub('Buy', '', price)
            price = re.sub('$', '', price)
        
            appDetails = price.strip()
            
            
    def GetTitle(self, soupObj, appDetails):
        #User Rating
        title = soupObj.find(attrs={'class': 'id-app-title'})
        
        appDetails.title = title.text.strip()
    
    def GetRatings(self, soupObj, appDetails):
        #User Rating
        score = soupObj.find(attrs={'class': 'score'})
        
        appDetails.rating = score.text.strip()
        
    
    def GetGenere(self, soupObj, appDetails):
        genere = soupObj.find(attrs={'itemprop': 'genre'})
        
        appDetails.genere = genere.text.strip()
    
    def GetInstalls(self, soupObj, appDetails):
        try:
            pull = soupObj.find(attrs={'itemprop': 'numDownloads'})
            appDetails.Installs = pull.text
        
        except TypeError as typeError:
            logger.log("Type Error at GetInstalls: ", typeError)
        
        except Exception as e:
            logger.log("Exception at GetInstalls: ", e)
        
    def GetTotalReviewers(self, soupObj, AppDetails):
        totalReviews = soupObj.find(attrs={'class': 'review-num'})
        
        AppDetails.totalReviews = totalReviews
    
    def GetDeveloper(self, soupObj, appDetails):    
        dev = soupObj.find(attrs={'class': 'document-subtitle primary'})
        
        appDetails.author = dev.text.strip()
    
    def GetContent(self, soupObj, appDetails):    
        contents = soupObj.find(attrs={'itemprop': 'contentRating'})
        
        fetchedContents = contents.text.strip()
        
        if(fetchedContents.count('Mature') | fetchedContents.count('+')):
            appDetails.adult = True