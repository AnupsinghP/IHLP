'''
Created on Nov 11, 2017

@author: Anupsingh Pardeshi
'''
import os
import xlsxwriter
from Sources.ObjectModel.AppDetails import AppDetails

class ExcelHandlerClass:
    
    global filePath
    
    filePath =r'C:\Users\Anupsingh Pardeshi\Desktop\IHLP\Project\ApplicationData.xlsx'
    
    def __init__(self):    
        
        if (os.path.isfile(filePath)!= True):   
            self.InitializeExcel(filePath)
        
        
    def InitializeExcel(self, filePath):
        workbook = xlsxwriter.Workbook(filePath)
        worksheet1 = workbook.add_worksheet('PlayStores')
        worksheet2 = workbook.add_worksheet('URLs')
        worksheet3 = workbook.add_worksheet('Application Details')
        
        bold = workbook.add_format({'bold': True})
        worksheet1.write('A1', 'Play stores', bold)
        worksheet2.write('A1', 'Urls', bold)
        
        worksheet3.write('A1', 'Title', bold)
        worksheet3.write('B1', 'Price', bold)
        worksheet3.write('C1', 'Rating', bold)
        worksheet3.write('D1', 'totalReviews', bold)
        worksheet3.write('E1', 'genere', bold)
        worksheet3.write('F1', 'price', bold)
        worksheet3.write('G1', 'author', bold)
        worksheet3.write('H1', 'Installs', bold)
        worksheet3.write('I1', 'Adult', bold)
        
        print("Workbook created")
        workbook.close()
    
    def GetAppDetailsWorkSheet(self):
        workbook = xlsxwriter.Workbook(filePath)
        return workbook.get_worksheet_by_name('Application Details')
    
    #Returns Worksheet for App details
    def CollectData(self, results):
        print(results[0].title)
        