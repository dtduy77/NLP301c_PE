# Q2
import re
text = '  this is. \n a sample \t. sentence.'
find = re.findall(r'\b\S\w*\S*\b', text) 
#print(find) # ['this', 'is', 'a', 'sample', 'sentence']
string = ' '.join(find) + '.'
print(string)