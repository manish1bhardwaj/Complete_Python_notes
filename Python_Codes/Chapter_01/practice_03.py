import os

# Specify the directory path (current directory by default)
path = '/'

# Get the list of all files and directories in the specified path
directory_contents = os.listdir(path)

# Print the contents of the directory
for item in directory_contents:
    print(item)
