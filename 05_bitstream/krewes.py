'''
Trio: April, Wanying, Erica
Soft Dev
K05 -- Random Devo and Ducky from Krewes
2022-09-28
time spent: 15 min 
DISCO: 
QCC:
OPS SUMMARY:
If krewes is empty, return ERROR
Gets a list of the keys in the krewes
Randomly iterates through all the list of keys to determine whether it contains values or not. If the key is empty, it will remove the key and continue on. If all the keys’ lists are empty, return ERROR. 
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

krewes1 = {1:["1", "2", "3"], 2:["A", "B", "C"]}
krewes2 = {
    2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY", "Ruiwen"],
    7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
    8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "Wanying", "Kevin"]
}
krewes3 = {}
krewes4 = {1:["1"], 2:[]}
krewes5 = {1:[], 2:[]}

def getRandom(dictionary):
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
            k = dictionary.get(period)  #gets the list associated with the random key
            break
    return k[r] #returns value at random index of random list

def createKrewes():
    

def addPd(pd, dictionary):
    dictionary[pd] = []

def rmPd(pd, dictionary):
    return dictionary.pop(pd)

def addStu(name, pd, dictionary):
    dictionary[pd].append(name)
    
def rmStu(name, pd, dictionary):
    for e in range(len(dictionary[pd])):
        if dictionary[pd][e] == name:
            return dictionary[pd].pop(e)
    return "no student with " + name + " found"
