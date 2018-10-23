# imports

import json
from difflib import get_close_matches

# load in data
filename = r"D:\dev\practice_workspace\app1_dictionary\resources\data.json"
data = json.load(open(filename))

# get_definition
#   w   the word to be queried
# output
#   the definition of the word w or error message

def get_definition(w) :
    w = w.lower()
    if w in data :
        return data[w]
    elif w.title() in data :
        return data[w.title()]
    elif w.upper() in data :
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys(),n=1, cutoff=0.8)) > 0 :
        for count in range(3) :
            yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w,data.keys(), cutoff=0.8)[0])
            if yn == "Y" :
                return data[get_close_matches(w,data.keys(), cutoff=0.8)[0]]
            elif yn == "N" :
                return "The word %s does not exist, Please double check it!" % w
            else :
                print("We didn't understand your entry!")
        return "Exiting"
    else :
        return "The word %s does not exist, Please double check it!" % w

# query the user for a word
# print out definition of word

query = input("Please Enter Query: ")
output = get_definition(query)
if type(output) == list :
    [print(str(cnt+1),'. ', x) for x,cnt in zip(output,range(len(output)))]
else :
    print(output)
