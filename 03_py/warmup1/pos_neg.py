'''
Given 2 int values, return True if one is negative and one is positive. 
Except if the parameter "negative" is True, then return True only if both are negative.

pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
pos_neg(-4, -5, False) → False
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
