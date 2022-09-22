'''
DISCO
There are a min and max function in python 
% is the modulus symbol that could be used to find reminders
'''

# % is the modulus symbol that could be used to find reminders
def count_evens(nums):
  count = 0
  for e in nums:
    if e % 2 == 0:
      count+=1
  return count
  
# count_evens([2, 11, 9, 0]) → 2	
# count_evens([2]) → 1
# count_evens([2, 5, 12]) → 2	

# there are a min and max function in python 
def big_diff(nums):
  mi = nums[0]
  ma = nums[0]
  
  for e in nums:
    mi = min(e, mi)
    ma = max(e, ma)
    
  return (ma - mi)
  
# big_diff([2, 3]) → 1	
# big_diff([2, 2]) → 0	
# big_diff([2]) → 0	

# += sign could be used to add on to the original
def centered_average(nums):
  mi = nums[0]
  ma = nums[0]
  s = 0
  for e in nums:
    mi = min(e, mi)
    ma = max(e, ma)
    s += e
  return (s - mi - ma) / (len(nums) - 2)

# centered_average([4, 4, 4, 4, 5]) → 4	
# centered_average([4, 4, 4, 1, 5]) → 4	
# centered_average([6, 4, 8, 12, 3]) → 6		

# sometimes else is needed, other times it's not
def sum13(nums):
  if len(nums) == 0:
    return 0
  
  s = 0
  i = 0
  while i < len(nums):
    if nums[i] == 13:
      i += 2
    else :
      s += nums[i]
      i+=1
  return s

# sum13([5, 13, 2]) → 5	
# sum13([0]) → 0	
# sum13([13, 0]) → 0

# A while loop can exist within a if statement within a while loop
def sum67(nums):
  if len(nums) == 0:
    return 0
  
  i = 0
  s = 0
  while i < len(nums):
    if (nums[i] == 6):
      i+=1
      while (nums[i] != 7):
        i+=1
      i+=1
    else:
      s+= nums[i]
      i+=1
      
  return s
  
# sum67([6, 7, 11]) → 11	11	OK	
# sum67([11, 6, 7, 11]) → 22	22	OK	
# sum67([2, 2, 6, 7, 7]) → 11	11	OK

# and is used instead of &&
def has22(nums):
  i = 0 
  
  while (i < (len(nums) - 1)):
    if nums[i] == 2 and nums[i+1] == 2:
      return True
    i+=1
    
  return False

# has22([]) → False	
# has22([3, 3, 2, 2]) → True		
# has22([5, 2, 5, 2]) → False	
