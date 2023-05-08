import pandas as pd
import datetime 
import json 
import os 
import os.path
from ydata_profiling import ProfileReport
from collections import OrderedDict
import pathlib

class AnalyzeEC2:

    def __init__(self):

        self.__dirToMonitor = ["jsonrecords", 'csvrecords']
     

    def createHMTLAndAnalyze(self): 

        #Setting up file format 
        csvAnalysisTime = datetime.datetime.now()
        recordTime = csvAnalysisTime
        service = "allocate_address"

        csvFile = self.findLastFile(self.__dirToMonitor[1])

        #Reading in CSV 
        df = pd.read_csv(csvFile)

        # #Generating Profile and saving ot a HMTL format
        profile = ProfileReport(df , explorative=True)
        #Parsing out whitespace so web broswer can diplay file
        url = f"templates/{recordTime}{service}analysis.html".replace(" ", "")
        profile.to_file(url)

    # Helper function to normalize data
    def normalizeData(self): 

        jsonFile = self.findLastFile(self.__dirToMonitor[0])
        # Open JSON file
        with open(jsonFile) as dataFile:    
            data = json.load(dataFile)  

        #Setting up file format 
        jsonAnalysisTime = datetime.datetime.now()
        recordTime = jsonAnalysisTime
        service = "allocate_address" 

        #Normalizing Data 
        df = pd.json_normalize(data)

        #Saving to a CSV file 
        csvDF = df.to_csv(f"csvrecords/{recordTime}{service}analysis.csv")
        dataFile.close()

    #Helper function to find last file in directory 
    def findLastFile(self, path): 

        # Defining data structures
        d = OrderedDict()
        record = []

        #Clean repo to get rid of faulty files
        removeFiles = os.listdir(path)

        #Clean repo to get rid of faulty files
        for item in removeFiles:

            if item.endswith(".json") or  item.endswith(".csv") or item.endswith(".html"):
                #ingoring correct file format
                pass 
            
            elif not item.endswith(".json") or  not item.endswith(".csv") or not item.endswith(".html"): 
               
                #removing anything that is not meant to be there
                os.remove(os.path.join(path, item))

        #Getting all files in directory 
        dataPaths = [os.path.join(pth, f) 
        for pth, dirs, files in os.walk(path) for f in files]

        # Building dictionary of files 
        for i in range(len(dataPaths)):
                    
            d[i] = dataPaths[i]
            f_name = pathlib.Path(f"{dataPaths[i]}")
            f_timestamp = f_name.stat().st_mtime
            record.append(f_timestamp)
            i +=i

        # Sorting from least to greatest 
        orderGreatoLeast = sorted(record, reverse=True)

        for p in range(len(record)): 

            if record[p] != orderGreatoLeast[0]:

                pass 

            elif record[p] == orderGreatoLeast[0]: 
                
                # Returning last file postion
                finalPostion = dataPaths[p]
                return finalPostion


a = AnalyzeEC2()
a.createHMTLAndAnalyze()
