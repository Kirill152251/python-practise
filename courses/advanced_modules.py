import re
import os

# Way to open files:
# with open('extracted_content/Instructions.txt') as f:
#     content = f.read()
#     print(content)

# Way to unzip file:
# shutil.unpack_archive('unzip_me_for_instructions.zip','','zip')

# Or:
# zip_obj = zipfile.ZipFile('comp_file.zip','r')
# zip_obj.extractall("extracted_content")

pattern = r'\d{3}-\d{3}-\d{4}'
my_dir = '/home/kirill/Downloads/unzip_me_for_instructions/extracted_content'
[print(x) for x in os.listdir(my_dir)]
my_file = open(my_dir + '/Instructions.txt')
print(my_file.read())
my_file.close()
number = {}
print()

for folder, sub_folders, files in os.walk(my_dir):
    for f in files:
        file = open(folder + f'/{f}')
        content = file.read()
        file.close()
        match = re.search(pattern, content)
        if match is not None:
            number[folder + f'/{f}'] = content[match.start():match.end()]

print(number)
