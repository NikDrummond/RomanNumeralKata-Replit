import pytest


# Source Code:
lookup = {'I':1, 'V':5}


def from_roman(roman: str) -> int:

  # invert list here
  char = [roman[i] for i in list(range(len(roman)-1,-1,-1))]
  
  #char = [i for i in roman]

  # think about "special" case where not "I" is preceded by "I"
 


  number = 0
  # need to change this - indexing is off (-1)
  for i, rom in enumerate(char):
    if rom =="V":
      return 5
    

    # i is an integer, the keys in the dict. are strings

    # invert dictionary?
    number += lookup[i]
    
        
  return number



# Tests: 

# lets add to this hahaha

cases = [
  ('I', 1),
  ('II', 2),
  ('III', 3),
]
@pytest.mark.parametrize(['num', 'roman'], cases)
def test_roman_1(num: int, roman: str):
  assert from_roman(num) == roman



#for i in range(len(char)):
#  if char[i] == "V":

  # change so if char[i] > char [i+1]

#    if char[i+1] == "I":
#      number += lookup[i]-1
#      i = i+2
#    else:
#      number += lookup[i]
#  else:
#    number += lookup[i]