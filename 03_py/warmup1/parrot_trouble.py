'''
Return true if talking = true and hour is before 7 or after 20. 

parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False	
parrot_trouble(True, 21) → True
parrot_trouble(False, 21) → False	

'''

def parrot_trouble(talking, hour):
  if talking == True and (hour < 7 or hour > 20):
    return True
    
  else:
    return False
