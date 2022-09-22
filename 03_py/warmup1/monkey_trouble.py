'''
Return true if both or neither are smiling. 

monkey_trouble(True, True) → True	True	
monkey_trouble(False, False) → True	True	
monkey_trouble(True, False) → False	False	
monkey_trouble(False, True) → False	False	

'''
def monkey_trouble(a_smile, b_smile):
  if (a_smile) == (b_smile): #if both are the same (smiling or not smiling) return True
    return True
    
  else:
    return False
