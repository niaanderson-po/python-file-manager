import os

def organize_downloads(root):
    file_type_map = {
            ('gif', 'png', 'PNG', 'jpeg', 'jpg', 'heic', 'HEIC', 'webp', 'avif'): 'Images',
            ('pdf',): 'PDF',
            ('ics', 'docx', 'epub'): 'Documents',
            ('xml', 'html'): 'Developer',
            ('pptx',): 'Presentation',
            ('dmg', 'zip'): 'Other'
        }

    for directory, subdir_list, file_list in os.walk(root):
        for name in file_list:
            file_extension = name.split('.')[-1].lower()

            #relocate unsorted downloads by file extension type
            for extensions, folder in file_type_map.items():
                if file_extension in extensions:
                    source_name = os.path.join(directory, name)
                    target_name = os.path.join(f'/Users/niaapple/Downloads/{folder}', name)
                    try:
                        print(f'Moving: {source_name} to: {target_name}')
                        os.rename(source_name, target_name)
                    except Exception as e:
                        print(f"Error moving {source_name} to {target_name}: {e}")
        break

if __name__ == "__main__":
    root = "/Users/niaapple/Downloads"
    organize_downloads(root)