'''
Women in STEM: April(horanghae), Wanying(pancake), Erica(hugo)  
Soft Dev
K06 -- CSV
2022-09-30
time spent: 2 hrs 

DISCO: 
Discovered the method random.choices() and its usages
Pprint :) 

QCC:
How to access values inside the dictionary keys (SOLVED) 
How to print a new line for each new key for dictionary 

OPS SUMMARY:
Make dictionary by splitting string by new line and commas from the right and then input those values into the dictionary
Created random_list that ran the choose_weighted fucntion for a specified amount of time and recorded how many teams each key appeared to see if the weighted fucntion worked
Add_val adds the new key to the dictionary if it doesn't exist or adds the value specified to the already existing key

'''

occupations_file = open("occupations.csv", "r") 
c = occupations_file.read() #read in file and make it a string
import random
import pprint

def make_dictionary(content):
    counter = 1
    dictionary = {}
    content_list = content.split('\n')
    while counter < len(content_list):
        occupation_list = content_list[counter].rsplit(",", maxsplit = 1)
        percentage = float(occupation_list[1]) #turning percentage to number 
        occupation = occupation_list[0]
        if occupation[0] == '"': #to remove the extra " around the strings 
            occupation = occupation.split('"')[1]
        dictionary[occupation] = percentage #add key and term to dictionary
        counter += 1
    return dictionary

def choose_weighted(dictionary):
    options = list(dictionary)
    options = options[0:len(options)-1] #removes total
    option_weights = []
    for e in dictionary: #adds value in key to list of its weights
        option_weights.append(dictionary.get(e))
    option_weights = option_weights[0:len(option_weights)-1] #removes total
    return random.choices(options, weights=option_weights) #returns options based on their weight

def add_val(val, key, dictionary):
    keys = list(dictionary)
    if not (key in keys): #checks to see if the period is already in the dictionary 
        dictionary[key] = 1 #sets default val to 1 since appeared once
    dictionary[key] = dictionary.get(key)+1 

def random_list(dictionary, loops):
    new_dictionary = {}
    while loops > 0:
        key = choose_weighted(dictionary)[0] #want value from input dictionary
        add_val(1, key, new_dictionary) #adds new value to new_dictionary  
        loops -= 1
    return new_dictionary 
    
c_dict = make_dictionary(c)
print(c_dict)
print(choose_weighted(c_dict))
pprint.pprint(random_list(c_dict, 100)) #prints each key of dictionary on new line