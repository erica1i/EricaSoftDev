'''
Return a new string where the char at index n has been removed. 

missing_char('kitten', 1) → 'ktten'	
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
missing_char('Hi', 0) → 'i'

'''
def missing_char(str, n):
  return str[0:n] + str[n+1:]
