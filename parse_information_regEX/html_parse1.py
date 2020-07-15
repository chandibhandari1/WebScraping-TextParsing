import numpy as np
import pandas as pd
import sys
import re
import codecs
from bs4 import BeautifulSoup
sys.path.append('C:\\Users\\bhandch\\Documents\pipDownloads')

# read the html file and print to view the data
# f = codecs.open('doc1.html', 'r')
# contents = f.read()
# print(contents)

# Method to read the html file
# with open('doc1.html', 'r') as f:
#     contents = f.read()
# print(contents)

# parse the information using RegEX
# Next_class: we will write the class method and loops pull them
# Third_class: with html taggs to parse
admin_sec={}
with open('doc1.html', 'rt') as myfile:
    for lines in myfile:
        if 'PPNA ' in lines:
            extract = re.split('\\bPPNA\\b', lines)[-1].rstrip('\n')
            admin_sec['PPNA']=re.sub('-', '', extract).strip() # .strip()- remove white spaces
        if 'PON ' in lines:
            extract = re.split('\\bPON\\b', lines)[-1].rstrip('\n')
            admin_sec['PON']=re.sub('-', '', extract).strip()
        if 'VERS ' in lines:
            extract = re.split('\\bVERS\\b', lines)[-1].rstrip('\n')
            admin_sec['VERS']=re.sub('-', '', extract).strip()
        if 'AP Supervisor' in lines:
            str_split = re.sub('-', '', re.split('\\bAP Supervisor\\b', lines)[-1].rstrip('\n'))
            if 'TEL' in str_split:
                admin_sec['AP Supervisor TEL']=re.sub(':', '', re.split('\\bTEL\\b', str_split)[-1].rstrip('\n')).strip()
            elif 'Email' in str_split:
                admin_sec['AP Supervisor Email']=re.sub(':', '', re.split('\\bEmail\\b', str_split)[-1].rstrip('\n')).strip()
            else:
                admin_sec['AP Supervisor']=re.sub(':', '', str_split).strip()
        if 'AP Manager ' in lines:
            extract = re.split('\\bAP Manager\\b', lines)[-1].rstrip('\n')
            admin_sec['AP Manager']=re.sub('-', '', extract).strip()
        if 'REMARKS ' in lines:
            extract = re.split('\\bREMARKS\\b', lines)[-1].rstrip('\n')
            admin_sec['REMARKS']=re.sub('-', '', extract).strip()

print(admin_sec)

# another way to include the text after remarks

with open('doc1.html','r') as f:
    con = f.read()
    lines = con.split('\n')
    full_text = ''
    for lin in lines:
        full_text +=lin
    a= 'REMARKS'
    after_remark = full_text[full_text.index(a)+len(a):]
admin_sec['REMARK']=after_remark
print(after_remark )
print(admin_sec)
# convert the dictionary to dataframe
df = pd.DataFrame(admin_sec.items(), columns=['Key', 'Whatever_name'])
print(df.head(10))

sys.exit(0)
# To excel
df.to_excel('file_output.xlsx')