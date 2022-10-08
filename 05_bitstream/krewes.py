'''
Trio: April(horanghae), Wanying(pancake), Erica(hugo)
Soft Dev
K05 -- Random Devo and Ducky from Krewes
2022-09-28
time spent: 1 hr
DISCO:
Split string with split() and its uses for it

QCC:
How to split dictionaries
How to import files and read it
How to find index of certain characters in strings

OPS SUMMARY:
If krewes is empty, return ERROR
Gets a list of the keys in the krewes
Randomly iterates through all the list of keys to determine whether it contains values or not.
If the key is empty, it will remove the key and continue on. If all the keys’ lists are empty, return ERROR.
When one of the keys is found to have a non-empty list, this key is chosen.
Choose a random index from list associated with chosen key
Return value at the random index of the associated key.

New Part:
Function to change string into a dictionary. 

To choose ducky, we will create another dictionary with identical index values of the person it is connected with.
Now, we will return the period and index of the person.
With those values we will select the corresponding ducky


'''

from random import randint

krewes_file = open("krewes.txt", "r")
content = krewes_file.read() #read in file and make it a string

names_dictionary = {}
ducky_dictionary = {}

def add_pd(pd, dictionary):
    dictionary[pd] = []

def rm_pd(pd, dictionary):
    return dictionary.pop(pd)

def add_stu(name, pd, dictionary):
    periods = list(dictionary)
    if not (pd in periods): #checks to see if the period is already in the dictionary
        add_pd(pd, dictionary)
    dictionary[pd].append(name)

def rm_stu(name, pd, dictionary):
    for e in range(len(dictionary[pd])):
        if dictionary[pd][e] == name:
            return dictionary[pd].pop(e)
    return "no student with " + name + " found"

def make_dictionary():
    people = 0
    content_list = content.split("@@@") #split string into list between @@@
    while people < len(content_list):
        people_list = content_list[people].split("$$$")
        add_stu(people_list[1], people_list[0], names_dictionary)
        add_stu(people_list[2], people_list[0], ducky_dictionary)
        people += 1

def get_random_index(dictionary):
    if len(dictionary) == 0:
        return "ERROR: Dictionary has no values"
    key = []
    for e in dictionary.keys(): #gets all the keys
        key.append(e)
    while True:
        if len(key) == 0:
            return "ERROR: all lists empty"
        period = key[randint(0, len(key)-1)]  #chooses a random key
        if len(dictionary.get(period)) == 0:
            key.remove(period)
        else:
            r = randint(0, len(dictionary.get(period))-1) #chooses random index of the list associated with the random key
            break
    return [period,r]

def get_random(dictionary): #for only one dictionary
    vals = get_random_index(dictionary)
    name_period = dictionary.get(vals[0])
    return "Period " + vals[0] + " || " + name_period[vals[1]]

def get_random_double(dictionary1, dictionary2): #for both dictionaries
    vals = get_random_index(dictionary1)
    name_period = dictionary1.get(vals[0])
    ducky_period = dictionary2.get(vals[0])
    return "Period " + vals[0] + " || " + name_period[vals[1]] + " || " + ducky_period[vals[1]]

make_dictionary()
print(names_dictionary)
print(ducky_dictionary)

print(get_random_double(names_dictionary, ducky_dictionary))
print(get_random(names_dictionary))
