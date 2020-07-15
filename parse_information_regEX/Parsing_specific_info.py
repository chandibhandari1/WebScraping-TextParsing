import numpy as np
import pandas as pd
import sys
import re
# when parsing based on key word from string
# # Method 1
string_check = 'Nothing to match REMARKS - Something note is given but this should be parsed at the given level. Skipping those information will lose data.' \
               'silence please I dont SEE the difference'
key_word = 'REMARKS'
before_keyWord, keyWord, after_keyWord = string_check.partition(key_word)
print(f'before Key word {before_keyWord}  \n after keyWord{after_keyWord}')
print(' ')

# Method 2
print(' *'*10)
regp = re.compile("REMARKS(.*)$")
print(regp.search(string_check).group(1))

# Method3
print(' #'*10)
par = re.search('(?<=REMARKS)(.*)', string_check)
after_key = par.groups()
print(after_key)

# Method4
print(' $'*10)
keyWord='REMARKS'
print(string_check[string_check.index(keyWord)+len(keyWord):])


#########%%%%%%%%%%%%%%%%%%%%%%%% Between Two Keywords%%%%%%%%%%%%%%%%
# when parsing string between two key
# # Method 1
string_check = 'Nothing to match REMARKS - Something note is given but this should be parsed at the given level. Skipping those information will lose data.' \
               'silence please I dont SEE the difference'
a = 'REMARKS'
b = 'SEE'
# After a
print(len(a))
text_inBetween = string_check[string_check.index(a)+len(a):] # or
text_inBetween2 = string_check[string_check.find(a)+len(a):]
# between a and b
text_inBetween3 = string_check[string_check.index(a)+len(a):string_check.index(b)] #or
text_inBetween4 = a + string_check[string_check.find(a)+len(a):string_check.find(b)] # including the key word
print(text_inBetween4)