import os
print('WARNING! ONLY THE FILES TO RENAME MUST BE IN THE FOLDER!')
folder_path = input('Please enter the folder path to the files:\n')
if not folder_path[-1] == '\\':
    folder_path = folder_path + '\\'

prefix = input('Please enter a filename prefix:\n')
files = os.listdir(folder_path)

for file in files:
    print(f'Renaming file: {file}')
    old_file_name = folder_path + file
    new_file_name = folder_path + prefix + file
    os.rename(old_file_name, new_file_name)

print('Finished!')
input('Press any key to close this window...')
