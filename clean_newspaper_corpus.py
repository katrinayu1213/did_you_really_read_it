#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
from pathlib import Path
import pandas as pd


    """
    Purpose: Transforms corpus text files into csv file, in preparation for building model 
    Uses science related text files from 20 Newsgroups http://qwone.com/~jason/20Newsgroups/
    """

# add each text file into news_combined.csv, stripping new lines
with open('news_combined.csv', 'w', encoding='Latin-1') as out_file:
    csv_out = csv.writer(out_file)
    csv_out.writerow(['FileName', 'Content'])
    for fileName in Path('./sci.electronics').glob('*'):
        lines = [ ]
        with open(str(fileName.absolute()),'rb') as one_text:
            for line in one_text.readlines():
                lines.append(line.decode(encoding='Latin-1',errors='ignore').strip())
        csv_out.writerow([str(fileName),' '.join(lines)])
    for fileName in Path('./sci.crypt').glob('*'):
        lines = [ ]
        with open(str(fileName.absolute()),'rb') as one_text:
            for line in one_text.readlines():
                lines.append(line.decode(encoding='Latin-1',errors='ignore').strip())
        csv_out.writerow([str(fileName),' '.join(lines)])
    for fileName in Path('./sci.med').glob('*'):
        lines = [ ]
        with open(str(fileName.absolute()),'rb') as one_text:
            for line in one_text.readlines():
                lines.append(line.decode(encoding='Latin-1',errors='ignore').strip())
        csv_out.writerow([str(fileName),' '.join(lines)])
    for fileName in Path('./sci.space').glob('*'):
        lines = [ ]
        with open(str(fileName.absolute()),'rb') as one_text:
            for line in one_text.readlines():
                lines.append(line.decode(encoding='Latin-1',errors='ignore').strip())
        csv_out.writerow([str(fileName),' '.join(lines)])

# clean data: remove symbols, numbers 
# cleaning specific to this corpus, mostly science related email exchanges 
data = pd.read_csv("news_combined.csv", engine= 'python')

documents = data["Content"].tolist() 

bad_chars = [';', ':', ".","[","]","#",'!',"?","*", "/","From","Subject","To", "@", "(", ")", "<", ">", "|", "-", ",", "&", "0", "1", "2", "3","4", "5", "6","7","8","9"]

for document in documents:
    document.encode('utf-8').strip()
    for i in bad_chars :
        document = document.replace(i, '')

