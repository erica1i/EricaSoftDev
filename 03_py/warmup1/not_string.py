'''
Given a string, return a new string where "not " has been added to the front. 
However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
not_string('bad') → 'not bad'

DISCO: First DISCO of the warmup! You can combine strings just by using the + sign. 

'''

def not_string(str):
  if str[:3] == "not": #if string began with not, then it would be unchanged. 
    return str
  return "not" + str 
