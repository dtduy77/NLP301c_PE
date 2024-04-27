# Q2
# import re
# text = '  this is. \n a sample \t. sentence.'
# find = re.findall(r'\b\S\w*\S*\b', text) 
# #print(find) # ['this', 'is', 'a', 'sample', 'sentence']
# string = ' '.join(find) + '.'
# print(string)

#Student solution
import re

def remove_whitespace(s):
  # replace multiple whitespace with a single space
  s = re.sub(r'\s+',' ',s)
  # replace leading and trailing space
  s = s.strip()
  return s

text_to_test = '  this is.     \n a sample \t. sentence.   '
result = remove_whitespace(text_to_test)
print(result)