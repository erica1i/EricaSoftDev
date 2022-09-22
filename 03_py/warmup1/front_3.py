'''
Front = first 3 chars of the string
If the string length is less than 3, the front is whatever is there. 
Return a new string which is 3 copies of the front.

front3('Java') → 'JavJavJav'	
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'	
front3('abcXYZ') → 'abcabcabc'	

DISCO: You can copy/repeat strings just by using the * sign. 
'''

def front3(str):
  if (len(str) < 3): #tests if length is less than 3
    return str * 3 #if so, just copies the entire str 3 times
  front = str[0:3] #takes the first 3 chars
  return front * 3 #copies front 3 times
