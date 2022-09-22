'''
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

diff21(0) → 21	
diff21(1) → 20	
diff21(2) → 19	
diff21(-1) → 22	

DISCO: Learned something cool here. The abs function in Python as it is in Java. 
abs(a-b) gives you the absolute value of the difference between a-b. Swag. 

'''

def diff21(n):
  if n > 21:
    return abs(21-n) * 2  #found absolute difference then multiplied by 2 since n is over 21
  
  else:
    return abs(21-n) #found absolute difference
