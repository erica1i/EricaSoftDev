'''
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

diff21(0) → 21	
diff21(1) → 20	
diff21(2) → 19	
diff21(-1) → 22	

'''

def diff21(n):
  if n > 21:
    return abs(21-n) * 2
  
  else:
    return abs(21-n)
