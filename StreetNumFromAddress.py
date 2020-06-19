"""
Teaching simple use of RegEx to ML Students
We need the Zipcode and street Address from the given address:
Note: Here were are only mapping the pattern but we can we other method to get it
"""
# append the path that for manual foler where install the python packages
import sys
sys.path.append('C:\\User\pande\Documents\Python_packages')
import re
import nltk
from nltk.corpus import stopwords

# create the stopwords
stopwords = stopwords.words('english')

# extract the full address from the given text: Street number is given but not Zipcode
text_given = "Automated mail prcessing machine read address on  times mailpiece something from " \
          "the place is 1960 W Chelsea Ave STE 2006R, ALLENTOWN, PA 65543 line outage"

# create the mapping regex
regexp = "[0-9]{1,5} .+, .+, [A-Z]{2} [0-9]{5}"

#extract the full address
address1 = re.findall(regexp,text_given)
print(address1)
"""
[0-9]{1,5}= starts with number 0-9 upto 1-5 counts for street number
.+, = anything after space and then comma before space
.+, = anything after space and then comma again before space
[A-Z]{2} = letter-2 count for State code
[0-9]{1,5}= start with number 0-9 exactly 5 digit for Zipcode
"""
# extract the full address from the given text: Zipcode and Street number is given
text_given2 = "Automated mail prcessing machine read address on  times mailpiece something from " \
          "the place is 1960 W Chelsea Ave STE 2006R, ALLENTOWN, PA  line outage"

# create the mapping regex
regexp2 = "[0-9]{1,5} .+, .+, [A-Z]{2}"

#extract the full address
address2 = re.findall(regexp2,text_given2)
print(" ")
print(address2)

# Just extract the Zipcode
text3 = "3456 notherham blvd Austin, 77643, TX"
regex3 = '\d{5}'
reg = re.compile(regex3)
zipcode1 = reg.findall(text3)
print("The given zipcode is:",zipcode1)
#%%%OR%
reg2 = re.compile('^.*(?P<zipcode>\d{5}).*$')
zipcode2 = reg2.findall(text3)
print("The given zipcode by other method:",zipcode2)
#%%%OR%
reg3 = re.compile('^.*(?P<zipcode>\d{5}).*$')
match =reg3.match(text3)
zipcode3 = match.groupdict()['zipcode']
print("The given zipcode by other method3:",zipcode3)


# Extracting the Street number and street name
# Street Name, Zipcode and state code
text3 = "3456 notherham blvd Austin, 77643, TX"
streetname= re.findall(r'^\d+|\S+ +\S+$', text3)
print(streetname)

# street number only
streetnumber =re.split(r'(?<=\d)(?:-\d+)?\s+', text3)[0]
print(streetnumber)
# street name and zipcode
streetname =re.split(r'(?<=\d)(?:-\d+)?\s+', text3)[1]
print(streetname)






