'''
Women in STEM: April(horanghae), Wanying(pancake), Erica(hugo)  
Soft Dev
K06 -- csv
2022-09-30
time spent:

DISCO: 

QCC:

OPS SUMMARY:

'''

occupations_file = open("occupations.csv", "r") 
c = occupations_file.read() #read in file and make it a string

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
        dictionary[percentage] = occupation #add key and term to dictionary
        counter += 1
    return dictionary

print(make_dictionary(c))
