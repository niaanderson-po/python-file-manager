import os

import os

root = os.path.join('..', 'food')
for directory, subdir_list, file_list in os.walk(root):
    print('Directory:', directory)
    for name in subdir_list:
        print('Subdirectory:', name)
    for name in file_list:
        print('File:', name)
        if name == 'tomato.txt':
            source_name = os.path.join(directory, name)
            target_name = os.path.join('../food/vegtables', name)
            print(f'Moving: {source_name} to: {target_name}')
            os.rename(source_name, target_name)
    print()