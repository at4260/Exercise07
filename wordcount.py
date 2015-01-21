from sys import argv 

script, filename = argv

f = open(filename)
new_dict = {}
# create a loop that will split by whitespace
for line in f:
    line = line.rstrip()
    words = line.split(' ')
# check if the word is in the current dictionary; if yes, add 1 to the value; if no, add the word as a key and 1 as the value
    for word in words:
        if word in new_dict:
            new_dict[word] = new_dict[word] + 1
        else:
            new_dict[word] = 1

# print word count


