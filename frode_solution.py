import os

# Change this to your desired directory and extension
folder_path = '/path/to/folder'
file_extension = '.txt'

# Get all files with the specified extension
files = [os.path.join(root, file)
         for root, dirs, files in os.walk(folder_path)
         for file in files if file.endswith(file_extension)]

print(files)