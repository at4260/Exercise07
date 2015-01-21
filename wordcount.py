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
print_dict(new_dict)

#print "" in new_dict