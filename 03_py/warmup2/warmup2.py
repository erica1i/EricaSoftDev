'''
DISCO
To create a string, you have to initalize it even if it's empty.
Specfic substrings can be obtains using brackets.
the len() function returns the numer of character in the string
and is used instead of &&
'''

# You can use * symbol to multiply string
def string_times(str, n):
  return (str * n)

print(string_times('Hi', 2))	
print(string_times('Hi', 3))	
print(string_times('Hi', 1))	

# To create a string, you have to initalize it even if it's empty.
def front_times(str, n):
  new = ""
  if len(str) < 3:
    return str * n
  
  else:
    new = str[0:3]
    return new * n
  
print(front_times('Chocolate', 2))
print(front_times('Chocolate', 3))
print(front_times('Abc', 3))

# Specfic substrings can be obtains using brackets.
def string_bits(str):
  index = 0
  new = ""
  for e in str:
    new += str[index:index + 1]
    index += 2
  return new

print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))
  
# You cannot do ++ on python for some reason.
def string_splosion(str):
  index = 0
  new = ""
  for e in str:
    new += str[:index + 1]
    index += 1
  return new

print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))

# the len() function returns the numer of character in the string
def last2(str):
  last = str[len(str)-2:]
  count = 0
  for e in range (len(str)-2):
    if (str[e:e+2] == last):
      count+=1
  return count

print(last2('11212'))	
print(last2('13121311'))	
print(last2('1717171'))

# integer variables have to be initalized.
def array_count9(nums):
  count = 0
  for e in nums:
    if (e == 9):
      count+=1
  return count

print(array_count9([1, 9, 9]))
print(array_count9([1, 9, 9, 3, 9]))		
print(array_count9([1, 2, 3]))

# You don't have to write else if the while loop tests all the cases for either True or False
def array_front9(nums):
  i = 0
  for e in nums:
    if (e == 9 and i < 4):
      return True
    i+=1
  return False

print(array_front9([1, 2, 3, 4, 5]))	
print(array_front9([9, 2, 3]))	
print(array_front9([1, 9, 9]))


# and is used instead of &&
def array123(nums):
  i = 0
  for e in range(len(nums)-2):
    if (nums[e] == 1 and nums[e+1] == 2 and nums[e+2] == 3):
      return True
  return False

print(array123([1, 1, 2, 3, 1]))
print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 1, 2, 3]))

# range function could be used effective to bound the function
def string_match(a, b):
  count = 0
  for e in range(len(a)-1):
    if (a[e:e+2] == b[e:e+2]):
      count+=1
  return count

print(string_match('abc', 'abc'))	
print(string_match('abc', 'axc'))	
print(string_match('hello', 'he'))
