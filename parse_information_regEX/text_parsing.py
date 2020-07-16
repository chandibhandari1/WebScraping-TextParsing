"""This is 1st day: we manually parse the information
Next class: we define class method"""
import numpy as np
import pandas as pd
import sys
import re
sys.path.append('C:\\Users\\bhandch\\Documents\pipDownloads')

# read the text file and print to view the data
# f = codecs.open('parsing.txt', 'r')
# contents = f.read()
# print(contents)

# Method to read the html file
# with open('parsing.txt', 'r') as f:
#     contents = f.read()
# print(contents)

# parse the information using RegEX
# Next_class: we will write the class method and loops pull them
# Third_class: with html taggs to parse
admin_sec={}
with open('parsing.txt') as myfile:
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
        if 'CNT ' in lines:
            extract = re.split('\\bCNT\\b', lines)[-1].rstrip('\n')
            admin_sec['CNT']=re.sub('-', '', extract).strip()
        if 'CN/PR VERS ' in lines:
            extract = re.split('\\bCN/PR VERS\\b', lines)[-1].rstrip('\n')
            admin_sec['CN/PR VERS']=re.sub('-', '', extract).strip()
        if 'TICKETING ID' in lines:
            extract = re.split('\\bTICKETING ID\\b', lines)[-1].rstrip('\n')
            admin_sec['TICKETING ID']=re.sub(':', '', extract).strip()
        if 'Project implement date ' in lines:
            extract = re.split('\\bProject implement date\\b', lines)[-1].rstrip('\n')
            admin_sec['Project implement date']=re.sub('-', '', extract).strip()
        if 'Created date' in lines:
            extract = re.split('\\bCreated date\\b', lines)[-1].rstrip('\n')
            admin_sec['Created date']=re.sub(':', '', extract).strip()
        if 'VIRU ' in lines:
            str_split = re.sub('-', '', re.split('\\bVIRU\\b', lines)[-1].rstrip('\n'))
            if 'Section' in str_split:
                pass
            else:
                admin_sec['VIRU']=re.sub('-', '', str_split).strip()
        if 'CRD ' in lines:
            if 'RE CRD' in lines:
                extract = re.split('\\bCRD\\b', lines)[-1].rstrip('\n')
                admin_sec['RE CRD']=re.sub('-', '', extract).strip()
            else:
                admin_sec['CRD'] = re.sub('-', '', re.split('\\bCRD\\b', lines)[-1].rstrip('\n')).strip()
        if 'CE-PLAN ' in lines:
            extract = re.split('\\bCE-PLAN\\b', lines)[-1].rstrip('\n')
            admin_sec['CE-PLAN']=re.sub('-', '', extract).strip()

print(admin_sec)


# another way to include the text after remarks and before another key word as remarks
with open('parsing.txt','r') as f:
    con = f.read()
    # clean_text =BeautifulSoup(con, 'lxml').text.strip()
    lines = con.split('\n')
    full_text = ''
    for lin in lines:
        full_text +=lin
    a= 'REMARKS'
    b = 'TICKETING ID'
    after_remark = full_text[full_text.find(a)+len(a):full_text.find(b)].strip()
admin_sec['REMARK']=re.sub('-', '',after_remark)
print(after_remark )
print(admin_sec)
# convert the dictionary to dataframe
df = pd.DataFrame(admin_sec.items(), columns=['Key', 'Whatever_name'])
print(df.head(20))
