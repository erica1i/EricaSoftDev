'''
Return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
front_back('abc') → 'cba'
front_back('') → ''

'''

def front_back(str):
  if (len(str) <= 1):
    return str
  return str[len(str)-1] + str[1:len(str)-1] + str[0:1]


