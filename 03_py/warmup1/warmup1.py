'''
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
DISCO: Learned something cool here. The abs function in Python as it is in Java. 
abs(a-b) gives you the absolute value of the difference between a-b.
'''

def diff21(n):
  if n > 21:
    return abs(21-n) * 2  #found absolute difference then multiplied by 2 since n is over 21
  
  else:
    return abs(21-n) #found absolute difference
 
print(diff21(0)) # → 21	
print(diff21(1)) # → 20	
print(diff21(2)) # → 19	
print(diff21(-1))# → 22	
    
  '''
Front = first 3 chars of the string
If the string length is less than 3, the front is whatever is there. 
Return a new string which is 3 copies of the front.
DISCO: You can copy/repeat strings just by using the * sign. 
'''

def front3(str):
  if (len(str) < 3): #tests if length is less than 3
    return str * 3 #if so, just copies the entire str 3 times
  front = str[0:3] #takes the first 3 chars
  return front * 3 #copies front 3 times
  
print(front3('Java')) # → 'JavJavJav'	
print(front3('Chocolate')) # → 'ChoChoCho'
print(front3('abc')) # → 'abcabcabc'	
print(front3('abcXYZ')) # → 'abcabcabc'
  
 '''
Return a new string where the first and last chars have been exchanged.
'''

def front_back(str):
  if (len(str) <= 1): #if length is less or equal to 1, there is no difference between the first and last chars
    return str        #thus, you would just return the str
  return str[len(str)-1] + str[1:len(str)-1] + str[0:1]
  
print(front_back('code')) # → 'eodc'
print(front_back('a')) # → 'a'
print(front_back('ab')) #→ 'ba'
print(front_back('abc')) #→ 'cba'
print(front_back('')) #→ ''
 
'''
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
DISCO: Similar to Java, you do not need an else statement to just go directly into the 
statement if the "if" statement isn't triggered. 
'''

def makes10(a, b):
  if a == 10 or b == 10 or b + a == 10: #returned True if one or their sum is 10. 
    return True
  return False
  
print(makes10(9, 10)) #→ True	
print(makes10(9, 9)) #→ False	
print(makes10(1, 9)) #→ True	
print(makes10(10, 1)) #→ True	


'''
Return a new string where the char at index n has been removed. 
DISCO: Very cool discovery here. To get the substring of a string from index n to the end, 
all you need to do is [n:]. Python automatically assumes that it goes to the last index. 
'''
def missing_char(str, n):
  return str[0:n] + str[n+1:] #took substring before index n and the substring after it & combined them together

print(missing_char('kitten', 1)) # → 'ktten'	
print(missing_char('kitten', 0)) # → 'itten'
print(missing_char('kitten', 4)) #→ 'kittn'
print(missing_char('Hi', 0)) # → 'i'

'''
Return true if both or neither are smiling. 
'''

def monkey_trouble(a_smile, b_smile):
  if (a_smile) == (b_smile): #if both are the same (smiling or not smiling) return True
    return True
    
  else:
    return False
print(monkey_trouble(True, True)) # → True
print(monkey_trouble(False, False)) # → True
print(monkey_trouble(True, False)) # → False
print(monkey_trouble(False, True)) # → False

'''
Given an int n, return True if it is within 10 of 100 or 200.
'''

def near_hundred(n):
  if abs(100-n) <= 10 or abs(200-n) <= 10: #used abs to find the difference b/c it doesn't matter whether it is positive or negative difference 
    return True
  return False

print(near_hundred(93)) # → True
print(near_hundred(90)) #→ True	
print(near_hundred(89)) #→ False
print(near_hundred(110)) # → True	
  
'''
Given a string, return a new string where "not " has been added to the front. 
However, if the string already begins with "not", return the string unchanged.
DISCO: First DISCO of the warmup! You can combine strings just by using the + sign. 
'''

def not_string(str):
  if str[:3] == "not": #if string began with not, then it would be unchanged. 
    return str
  return "not" + str 

print(not_string('candy')) #→ 'not candy'
print(not_string('x')) #→ 'not x'
print(not_string('not bad')) #→ 'not bad'
print(not_string('bad')) #→ 'not bad'
  
'''
Return true if talking = true and hour is before 7 or after 20. 
'''

def parrot_trouble(talking, hour):
  if talking == True and (hour < 7 or hour > 20):
    return True
    
  else:
    return False
  
print(parrot_trouble(True, 6)) # → True
print(parrot_trouble(True, 7)) #→ False
print(parrot_trouble(False, 6)) #→ False	
print(parrot_trouble(True, 21)) #→ True
print(parrot_trouble(False, 21)) #→ False	

'''
Given 2 int values, return True if one is negative and one is positive. 
Except if the parameter "negative" is True, then return True only if both are negative.
'''

def pos_neg(a, b, negative):
  if negative == True:  #triggers second req since parameter "negative" is True
    if a < 0 and b < 0: #checked for the second req where you return True only if both are negative
      return True
    else:
      return False
      
  if (a > 0 and b > 0) or (a < 0 and b < 0): #checked if both are pos or both are neg
    return False
  
  return True
  
print(pos_neg(1, -1, False)) #→ True
print(pos_neg(-1, 1, False)) #→ True
print(pos_neg(-4, -5, True)) #→ True
print(pos_neg(-4, -5, False)) #→ False
  
 '''
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
'''

def sleep_in(weekday, vacation):
    if not weekday or vacation:
      return True
    else:
      return False
      
print(sleep_in(True, False)) #False
print(sleep_in(False, False)) #True
print(sleep_in(True, True)) #True
print(sleep_in(False, True)) #True      
      
'''
Return the sum of the given two ints...
Unless the two values are the same, then return double their sum.
'''

def sum_double(a, b):
  if (a == b):  #checked if the two values were the same
    return (a+b)*2  #returned double
    
  return a + b
print(sum_double(1, 2)) #→ 3
print(sum_double(3, 2)) #→ 5
print(sum_double(2, 2)) #→ 8
print(sum_double(-1, 0)) #→ -1
