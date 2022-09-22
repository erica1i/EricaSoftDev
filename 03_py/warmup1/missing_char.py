'''
Return a new string where the char at index n has been removed. 

DISCO: Very cool discovery here. To get the substring of a string from index n to the end, 
all you need to do is [n:]. Python automatically assumes that it goes to the last index. 
'''

def missing_char(str, n):
  return str[0:n] + str[n+1:] #took substring before index n and the substring after it & combined them together

print(missing_char('kitten', 1)) # → 'ktten'	
print(missing_char('kitten', 0)) # → 'itten'
print(missing_char('kitten', 4)) #→ 'kittn'
print(missing_char('Hi', 0)) # → 'i'
