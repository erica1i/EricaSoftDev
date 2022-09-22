'''
Given a string, return a new string where "not " has been added to the front. 
However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
not_string('bad') → 'not bad'

'''

def not_string(str):not_string('candy') → 'not candy'	'not candy'	OK	
not_string('x') → 'not x'	'not x'	OK	
not_string('not bad') → 'not bad'	'not bad'	OK	
not_string('bad') → 'not bad'	'not bad'	OK	

  if str[:3] == "not":
    return str
  return "not "+str
