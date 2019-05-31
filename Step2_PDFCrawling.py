# Crawl data from PDF which downlaoded from Bursa Malaysia website.
# Identify the table data to crawl and repeated for daily stocks data.

# Import library and data files for data Extraction
import os
import tabula
import numpy as np
import pandas as pd
from pandas import DataFrame
from PyPDF2 import PdfFileReader, PdfFileWriter


arr = []
for file in os.listdir(r"https://github.com/lauweitiong/Milestone6/tree/master/Data"):
    if file.endswith(".pdf"):
        arr.append(file)

filenames = [f for f in arr] 
filenames


# Data extraction
stocks = pd.DataFrame([])

for data in filenames:
    reader = PdfFileReader(open(data,mode='rb'))
    n =  reader.getNumPages()
    print(data)
    print("number of pages:",n)
    for i in range(4,n):
        df = tabula.read_pdf(data,pages=i,sort=True)
        df.Stock = df.Stock.apply('="{}"'.format)
        df=df.dropna()
        df= df.drop_duplicates(subset ="Stock")
        df.reset_index(drop=True)
        stocks = stocks.append(df)


        
stocks_final = stocks
del stocks_final['Unnamed: 2']     

stocks_final = stocks_final.rename(columns={'Cur.':'Currency', 'Stock Name':'Stock_name', 'Value Traded': 'Val_traded', 'Volume': 'Vol_traded'}) 

stocks_final.to_csv('Stock_data.csv',index=False)  
Print("Hello")  
