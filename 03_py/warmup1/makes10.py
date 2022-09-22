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
