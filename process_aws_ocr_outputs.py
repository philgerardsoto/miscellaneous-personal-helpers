import os
import re
from natsort import natsorted

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

path = os.getcwd()

# Path to the output file
output_file_path = os.path.join(path, 'combined_output.txt')

# Sort the folder names using natsorted with the custom key
for foldername in natsorted(os.listdir(path), key=numeric_sort_key):
    # Construct the path to the rawText.txt file within the folder
    text_file_path = os.path.join(path, foldername, 'rawText.txt')
    # Open the rawText.txt file and append its contents to the output file
    try:
        with open(text_file_path, 'r') as file:
            # Read the contents of the file
            contents = file.read()
            # Append the contents to the output file
            with open(output_file_path, 'a') as output_file:
                output_file.write(contents + '\n')  # Add a newline for separation
    except:
        pass