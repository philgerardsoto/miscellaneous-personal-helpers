#!/usr/bin/env python
# coding: utf-8

# In[2]:


from PIL import Image
import os


# In[4]:


# Directory containing the JPG files
directory = '/Users/macbookair/Documents/tita_josie'


# In[9]:


# Initialize a counter for the filenames
counter = 1

# Loop through all the files in the directory
for filename in sorted(os.listdir(directory)):
    if filename.endswith('.jpg'):
        img_path = os.path.join(directory, filename)
        with Image.open(img_path) as img:
            # Calculate the width to split the image into two halves
            width, height = img.size
            width_cutoff = width // 2

            # Split the image into two halves
            left_half = img.crop((0, 0, width_cutoff, height))
            right_half = img.crop((width_cutoff, 0, width, height))

            # Save each half with a new filename using the counter
            left_half.save(os.path.join(directory, f'{counter}.jpg'))
            counter += 1
            right_half.save(os.path.join(directory, f'{counter}.jpg'))
            counter += 1


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




