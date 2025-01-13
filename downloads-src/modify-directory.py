import os

root = os.path.join("/Users/niaapple", "Downloads")
for directory, subdir_list, file_list in os.walk(root):
    for name in file_list:
        #relocate unsorted downloads by file extension type
        if name.endswith(('.gif', '.png', '.PNG', '.jpeg', '.jpg', '.heic', '.HEIC', 'webp', 'avif')):
            source_name = os.path.join(directory, name)
            target_name = os.path.join('../Downloads/Images', name)
            print(f'Moving: {source_name} to: {target_name}')
            os.rename(source_name, target_name)
        if name.endswith('.pdf'):
            source_name = os.path.join(directory, name)
            target_name = os.path.join('../Downloads/PDF', name)
            print(f'Moving: {source_name} to: {target_name}')
            os.rename(source_name, target_name)
        if name.endswith(('.ics', '.docx', '.epub')):
            source_name = os.path.join(directory, name)
            target_name = os.path.join('../Downloads/Documents', name)
            print(f'Moving: {source_name} to: {target_name}')
            os.rename(source_name, target_name)
        if name.endswith(('.xml', '.html')):
            source_name = os.path.join(directory, name)
            target_name = os.path.join('../Downloads/Developer', name)
            print(f'Moving: {source_name} to: {target_name}')
            os.rename(source_name, target_name)
        if name.endswith('.pptx'):
            source_name = os.path.join(directory, name)
            target_name = os.path.join('../Downloads/Presentation', name)
            print(f'Moving: {source_name} to: {target_name}')
            os.rename(source_name, target_name)
        if name.endswith(('.dmg', '.zip')):
            source_name = os.path.join(directory, name)
            target_name = os.path.join('../Downloads/Other', name)
            print(f'Moving: {source_name} to: {target_name}')
            os.rename(source_name, target_name)
    break