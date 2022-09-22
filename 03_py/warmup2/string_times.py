'''
DISCO:
To create a string, you have to initalize it even if it's empty.
Specfic substrings can be obtains using brackets.
The len() function returns the numer of character in the string
and is used instead of &&
You can use * symbol to multiply string

string_times('Hi', 2) → 'HiHi'	
string_times('Hi', 3) → 'HiHiHi'	
string_times('Hi', 1) → 'Hi'	


'''
def string_times(str, n):
  return (str * n)
