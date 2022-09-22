'''
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

makes10(9, 10) → True	
makes10(9, 9) → False	
makes10(1, 9) → True	
makes10(10, 1) → True	

DISCO: Similar to Java, you do not need an else statement to just go directly into the 
statement if the "if" statement isn't triggered. 
'''

def makes10(a, b):
  if a == 10 or b == 10 or b + a == 10:
    return True
  return False
