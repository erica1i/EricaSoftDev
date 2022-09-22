'''
Return the sum of the given two ints...
Unless the two values are the same, then return double their sum.

sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
sum_double(-1, 0) → -1

'''

def sum_double(a, b):
  if (a == b):  #checked if the two values were the same
    return (a+b)*2  #returned double
    
  return a + b
