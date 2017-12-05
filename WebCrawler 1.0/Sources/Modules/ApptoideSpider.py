'''
Created on Dec 5, 2017

@author: Anupsingh Pardeshi
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
from asyncio.log import logger
import html
import requests

class AppSpiderClass:
    
    def SpiderA(self):
        
        appList =[]
        
        while True:
            urls =['https://en.aptoide.com/apps/latest/more','https://en.aptoide.com/apps/latest/more?offset=45','https://en.aptoide.com/apps/latest/more?offset=84','https://en.aptoide.com/apps/latest/more?offset=126','https://en.aptoide.com/apps/latest/more?offset=161','https://en.aptoide.com/apps/latest/more?offset=200','https://en.aptoide.com/apps/latest/more?offset=235','https://en.aptoide.com/apps/latest/more?offset=276','https://en.aptoide.com/apps/latest/more?offset=324','https://en.aptoide.com/apps/latest/more?offset=367','https://en.aptoide.com/apps/latest/more?offset=411','https://en.aptoide.com/apps/latest/more?offset=456','https://en.aptoide.com/apps/latest/more?offset=500','https://en.aptoide.com/apps/latest/more?offset=535','https://en.aptoide.com/apps/latest/more?offset=573','https://en.aptoide.com/apps/latest/more?offset=614','https://en.aptoide.com/apps/latest/more?offset=660','https://en.aptoide.com/apps/latest/more?offset=692','https://en.aptoide.com/apps/latest/more?offset=734','https://en.aptoide.com/apps/latest/more?offset=772','https://en.aptoide.com/apps/latest/more?offset=805','https://en.aptoide.com/apps/latest/more?offset=839','https://en.aptoide.com/apps/latest/more?offset=872','https://en.aptoide.com/apps/latest/more?offset=906','https://en.aptoide.com/apps/latest/more?offset=940']
            
            #try:
            for pagelink in urls:
                htmlPages = requests.get(pagelink)
                text = htmlPages.text
                soup = BeautifulSoup(text,"html.parser")
                
                self.FetchAptoideLinks(soup,appList)
                
                
            except requests.ConnectionError as connError:
                logger.log("Connection Error while connecting to Play store: ", urls," Error: ", connError)
            
            except requests.HTTPError as httpError:
                logger.log("Invalid HTTP response to Play store: ", urls, " Error: ", httpError)
            
            except requests.Timeout() as requestTimeoutError:
                logger.log("Time-out to connect to Play store: ", urls, " Error: ", requestTimeoutError)
                
            except requests.TooManyRedirects() as redirectsError:
                logger.log("Too many redirects for connection to Play store: ", urls, " Error: ", redirectsError)
                
            except Exception as e:
                logger.log("Excpetion occured at Func Spider: ", e)
            
            except requests.exceptions.Timeout as timeoutException:
                logger.log("Timeout Exception", timeoutException)
                
            return appList
    
    
    def FetchAptoideLinks(self,soup,appList):
        
            for link in soup.findAll("span",{"class":"bundle-item__info__span--big"}):
                hreff = link.find('a').get('href')
                
                if(appList.__contains__(hreff)!=True):
                    appList.append(str(hreff))

    