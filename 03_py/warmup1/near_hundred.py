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
