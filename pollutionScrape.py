#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
21/01/2020, the air quality still remained at unhealthy level for Bangkok, Thailand and its nearby provinces.
this workbook only satisfy my current interest in data exploratory, forecasting, programming in python 
and the current air pollution situation in Bangkok, Thailand. 

pollutionScrape.py - Only for Scraping data from Berkeley Earth website 
Remark- the available air quality data that provided by Pollution Control Department
(http://www.aqmthai.com/) can be trace only 1 month back
, luckily I found the article from Khun Worasom Kundhikanjana
https://towardsdatascience.com/identifying-the-sources-of-winter-air-pollution-in-bangkok-part-ii-72539f9b767a
she suggest that "historical data can be found in Berkeley Earth website"
so, here i am scraping data from Berkeley Earth website.

Credits to Khun Worasom Kundhikanjana, and Berkeley Earth website

regards
CM

"""


# In[97]:



# import libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
cwd = os.getcwd()
from pathlib import Path
import wget #Using the wget Module The method accepts two parameters: the URL path of the file to download and local path where the file is to be stored.


# In[98]:


nburl='http://berkeleyearth.lbl.gov/air-quality/maps/cities/Thailand/Bangkok/Bangkok.neighbors.json'


# In[112]:


r = requests.get(nburl)
soup = BeautifulSoup(r.content, "html.parser")


# # Get name of BKK neighborhoods and store in nblist

# In[113]:


nblist = soup.get_text()
nblist


# In[114]:


nblist = nblist.split(",\r\n")
nblist


# In[93]:


'''[i for i in(row.split(',') for row in z[0:])]

for row in z[1:]:
    x=row.split(',')
    for i in x:
        print(i)
        print()
    break'''


# In[157]:


# replace non word the matching strings [" "]
nblist=nbhood.replace(to_replace ='[^\w\s]', value = '', regex = True) 

#strip leading and trailing space
nblist['Province'] = nblist['Province'].str.strip()
nblist['City'] = nblist['City'].str.strip()

#replace space with _
nblist=nblist.replace(to_replace =' ', value = '_', regex = True) 
nblist.head(10)


# # Get http path

# In[159]:


#get access to each path in bkk neighborhood.json
globalurl ='http://berkeleyearth.lbl.gov/air-quality/maps/cities/Thailand/'
#get access to each path in bkk neighborhood.json
for index, row in nblist.iterrows():
    path = globalurl+row['Province']+'/'+row['City']+'.json'
    #path gives http://berkeleyearth.lbl.gov/air-quality/maps/cities/Thailand/Nonthaburi/Bang_Kruai.json
    print(path)


# In[184]:


#get access to each path in bkk neighborhood.json
for index, row in nblist.iterrows():
    globalurl ='http://berkeleyearth.lbl.gov/air-quality/maps/cities/Thailand/'
    cityname=row['City']
    path = globalurl+row['Province']+'/'+row['City']+'.txt'#'.json'
    #path gives http://berkeleyearth.lbl.gov/air-quality/maps/cities/Thailand/Nonthaburi/Bang_Kruai.json
    r = requests.get(path)
    soup = BeautifulSoup(r.content, "html.parser")
    
    download(path,cityname) # call download function
    #break
    


# In[182]:


#create new directory name 'pollutiondata'
Path('pollutiondata').mkdir(parents=True, exist_ok=True)

#download data from file path and save as .txt
def download(path,cityname):
    wget.download(path, cwd+'/pollutiondata/'+cityname+'.txt')
    #print(path)
    


# # Get Bangkok data and download it into .txt

# In[185]:


bkkurl='http://berkeleyearth.lbl.gov/air-quality/maps/cities/Thailand/Bangkok/Bangkok.txt'
cityname='Bangkok'
download(path,cityname)


# In[ ]:




