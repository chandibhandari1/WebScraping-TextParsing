import numpy as np
import pandas as pd
import sys
import re

class dataParsing:
    def __init__(self, df=None):
        self.data =df
    def createDict(self, text):
        lin = text.split('\n')
        line_no =0
        admin_sec = {}
        for lines in lin:
            if 'PPNA ' in lines:
                extract = re.split('\\bPPNA\\b', lines)[-1].rstrip('\n')
                admin_sec['PPNA'] = re.sub('-', '', extract).strip()  # .strip()- remove white spaces
            if 'PON ' in lines:
                extract = re.split('\\bPON\\b', lines)[-1].rstrip('\n')
                admin_sec['PON'] = re.sub('-', '', extract).strip()
            if 'VERS ' in lines:
                extract = re.split('\\bVERS\\b', lines)[-1].rstrip('\n')
                admin_sec['VERS'] = re.sub('-', '', extract).strip()
            if 'AP Supervisor' in lines:
                str_split = re.sub('-', '', re.split('\\bAP Supervisor\\b', lines)[-1].rstrip('\n'))
                if 'TEL' in str_split:
                    admin_sec['AP Supervisor TEL'] = re.sub(':', '',
                                                            re.split('\\bTEL\\b', str_split)[-1].rstrip('\n')).strip()
                elif 'Email' in str_split:
                    admin_sec['AP Supervisor Email'] = re.sub(':', '', re.split('\\bEmail\\b', str_split)[-1].rstrip(
                        '\n')).strip()
                else:
                    admin_sec['AP Supervisor'] = re.sub(':', '', str_split).strip()
            if 'AP Manager ' in lines:
                extract = re.split('\\bAP Manager\\b', lines)[-1].rstrip('\n')
                admin_sec['AP Manager'] = re.sub('-', '', extract).strip()
            if 'CNT ' in lines:
                extract = re.split('\\bCNT\\b', lines)[-1].rstrip('\n')
                admin_sec['CNT'] = re.sub('-', '', extract).strip()
            if 'CN/PR VERS ' in lines:
                extract = re.split('\\bCN/PR VERS\\b', lines)[-1].rstrip('\n')
                admin_sec['CN/PR VERS'] = re.sub('-', '', extract).strip()
            if 'TICKETING ID' in lines:
                extract = re.split('\\bTICKETING ID\\b', lines)[-1].rstrip('\n')
                admin_sec['TICKETING ID'] = re.sub(':', '', extract).strip()
            if 'Project implement date ' in lines:
                extract = re.split('\\bProject implement date\\b', lines)[-1].rstrip('\n')
                admin_sec['Project implement date'] = re.sub('-', '', extract).strip()
            if 'Created date' in lines:
                extract = re.split('\\bCreated date\\b', lines)[-1].rstrip('\n')
                admin_sec['Created date'] = re.sub(':', '', extract).strip()
            if 'VIRU ' in lines:
                str_split = re.sub('-', '', re.split('\\bVIRU\\b', lines)[-1].rstrip('\n'))
                if 'Section' in str_split:
                    pass
                else:
                    admin_sec['VIRU'] = re.sub('-', '', str_split).strip()
            if 'CRD ' in lines:
                if 'RE CRD' in lines:
                    extract = re.split('\\bCRD\\b', lines)[-1].rstrip('\n')
                    admin_sec['RE CRD'] = re.sub('-', '', extract).strip()
                else:
                    admin_sec['CRD'] = re.sub('-', '', re.split('\\bCRD\\b', lines)[-1].rstrip('\n')).strip()
            if 'CE-PLAN ' in lines:
                extract = re.split('\\bCE-PLAN\\b', lines)[-1].rstrip('\n')
                admin_sec['CE-PLAN'] = re.sub('-', '', extract).strip()
        return admin_sec
    def dict_to_df(self, pass_text):
        dict_val=self.createDict(pass_text)
        # convert the dictionary to dataframe
        df = pd.DataFrame(dict_val.items(), columns=['Key', 'Whatever_name'])
        print(df.head(20))
        return df
# create the object
s = dataParsing()

# read the file
with open('parsing.txt', 'r') as f:
    contents = f.read()
# call the method from object s to get the information
s.dict_to_df(contents)
