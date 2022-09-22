'''
Return true if both or neither are smiling. 

'''
def monkey_trouble(a_smile, b_smile):
  if (a_smile) == (b_smile): #if both are the same (smiling or not smiling) return True
    return True
    
  else:
    return False


print(monkey_trouble(True, True)) # → True
print(monkey_trouble(False, False)) # → True
print(monkey_trouble(True, False)) # → False
print(monkey_trouble(False, True)) # → False

