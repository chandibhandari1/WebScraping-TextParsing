"""
Teaching simple use of RegEx to ML Students
We need the Zipcode and street Address from the given address:
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
