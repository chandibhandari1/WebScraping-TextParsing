"""This is 3rd day: we define class method and looping in this method
Next class: we apply list comprehensive"""
import numpy as np
import pandas as pd
import sys
import re

class dataParsing:
    def __init__(self, contents, lists):
        self.text =contents
        self.lists = lists
    def h2D(self,keyw):
        lin = self.text.split('\n')
        for lines in lin:
            if keyw in lines:
                extract =re.split(keyw, lines)[-1].rstrip('\n')
                sr = re.sub('-', '', extract).strip()
        return sr

    # Method to create the dict
    def create_dict(self):
        admin_sec = {}
        for keys in self.lists:
            admin_sec[keys]=self.h2D(keys)
        return admin_sec
    # Method to create the dataframe
    def dict_dataframe(self):
        dict_val = self.create_dict()
        df = pd.DataFrame(dict_val.items(), columns=['Key', 'Whatever_name'])
        return df

# call the method and get the result
# read the file
with open('parsing.txt', 'r') as f:
    contents = f.read()
# call the method from object s to get the information
lis = ['PPNA ', 'PON', 'AP Manager', 'CNT', 'CN/PR VERS', 'Dir', 'REMARKS', 'VERS']
s = dataParsing(contents, lis)
print(s.dict_dataframe())
