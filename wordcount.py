from sys import argv
import re 

script, filename = argv


def create_dict():

    f = open(filename)
    new_dict = {}
    # create a loop that will split by whitespace
    for line in f:
        line = line.rstrip()
        #words = re.findall(r"[\w']+", line)
        words = re.split("\W+|_" , line)
    # check if the word is in the current dictionary; if yes, add 1 to the value; if no, add the word as a key and 1 as the value
        for word in words:
            word = word.lower()
            if word in new_dict:
                new_dict[word] = new_dict[word] + 1
            else:
                new_dict[word] = 1
    del new_dict[""]            

    return new_dict
# print word count
def print_dict(dictionary):
    for k, v in dictionary.items():
        print k, v

new_dict = create_dict()
#print_dict(new_dict)
dict_range = max(new_dict.values())
print dict_range
#print type(dict_range)
#print new_dict["a"]
#print new_dict["the"]
#print "" in new_dict

sorted_keys = sorted(new_dict)
sorted_keys.reverse()
organized_list = []

for i in range(1 , (dict_range + 1)):
    if i not in new_dict.values():
        continue
    for key in sorted_keys:
        if new_dict[key] == i:
            organized_list.append((key, new_dict[key]))
        else:
            pass

organized_list.reverse()

def print_list(sample_list):
    for k, v in sample_list:
        print k, v
print_list(organized_list)        

