#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os
import re


# In[9]:


# specify the directory you want to use
path = '/Users/macbookair/Documents/tita_josie/ocrd_v2'


# In[14]:


# Custom sorting key that extracts numbers and converts them to integers
def numeric_sort_key(name):
    # Skip system files like .DS_Store
    if name.startswith('.'):
        return float('inf')  # Assign a high value to sort these last
    # Use regular expression to find the first sequence of digits in the folder name
    match = re.search(r'\d+', name)
    if match:
        return int(match.group())
    return float('inf')  # Assign a high value to non-numeric names

# Sort the folder names using the custom key
for foldername in sorted(os.listdir(path), key=numeric_sort_key):
    # print(foldername)
    # Construct the path to the rawText.txt file within the folder
    text_file_path = os.path.join(path, foldername, 'rawText.txt')
    # Open the rawText.txt file and do something with it
    try:
        with open(text_file_path, 'r') as file:
            # For example, read the contents of the file
            contents = file.read()
            # Do something with the contents
            print(contents)
    except:
        pass


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




