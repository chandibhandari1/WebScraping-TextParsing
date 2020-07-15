import numpy as np
import pandas as pd
import sys
import re
import codecs
from bs4 import BeautifulSoup
sys.path.append('C:\\Users\\bhandch\\Documents\pipDownloads')
# another way to include the text after remarks and before another key word as remarks
admin_sec = {}
rep_sec ={}
tir_sec ={}
with open('new_doc.html','r') as f:
    con = f.read()
    soup = BeautifulSoup(con, 'lxml')
    contents = soup.get_text().split('\n')
    print(contents)
    for lines in contents:
        if 'CON ' in lines:
            extract = re.split('\\bCON\\b', lines)[-1].rstrip('\n')
            admin_sec['CON']=re.sub('-', '', extract).strip() # .strip()- remove white spaces
        if 'JER ' in lines:
            extract = re.split('\\bJER\\b', lines)[-1].rstrip('\n')
            admin_sec['JER']=re.sub('-–', '', extract).strip()
        if 'ISCEL ' in lines:
            extract = re.split('\\bISCEL\\b', lines)[-1].rstrip('\n')
            admin_sec['ISCEL']=re.sub('-–', '', extract).strip()
        if 'VCID ' in lines:
            extract = re.split('\\bVCID\\b', lines)[-1].rstrip('\n')
            admin_sec['VCID']=re.sub('-', '', extract).strip()
        if 'ORD ' in lines:
            if 'IR ORD' in lines:
                extract = re.split('\\bORD\\b', lines)[-1].rstrip('\n')
                admin_sec['IR ORD']=re.sub('-–', '', extract).strip()
            else:
                admin_sec['ORD'] = re.sub('-–', '', re.split('\\bORD\\b', lines)[-1].rstrip('\n')).strip()
        if 'Doctor Calling Date' in lines:
            extract = re.split('\\bDoctor Calling Date\\b', lines)[-1].rstrip('\n')
            admin_sec['Doctor Calling Date']=re.sub(':', '', extract).strip()

print(admin_sec)
# convert the dictionary to dataframe
df = pd.DataFrame(admin_sec.items(), columns=['Key', 'Whatever_name'])
print(df.head(20))

