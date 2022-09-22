'''
Front = first 3 chars of the string
If the string length is less than 3, the front is whatever is there. 
Return a new string which is 3 copies of the front.

front3('Java') → 'JavJavJav'	'JavJavJav'	OK	
front3('Chocolate') → 'ChoChoCho'	'ChoChoCho'	OK	
front3('abc') → 'abcabcabc'	'abcabcabc'	OK	
front3('abcXYZ') → 'abcabcabc'	'abcabcabc'	OK
'''

def front3(str):
  if (len(str) < 3): #tests if length is less than 3
    return str * 3 #if so, just copies the entire str 3 times
  front = str[0:3] #takes the first 3 chars
  return front * 3 #copies front 3 times
