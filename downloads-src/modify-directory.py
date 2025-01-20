import os
import logging


script_directory = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(script_directory, "organize_downloads.log")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()      
    ]
)

def organize_downloads(root):
    file_type_map = {
            ('gif', 'png', 'PNG', 'jpeg', 'jpg', 'heic', 'HEIC', 'webp', 'avif'): 'Images',
            ('pdf',): 'PDF',
            ('ics', 'docx', 'epub'): 'Documents',
            ('xml', 'html'): 'Developer',
            ('pptx',): 'Presentation',
            ('dmg', 'zip'): 'Other'
        }

    for directory, _, file_list in os.walk(root):
        for name in file_list:
            file_extension = name.split('.')[-1].lower()

            #relocate unsorted downloads by file extension type
            for extensions, folder in file_type_map.items():
                if file_extension in extensions:
                    source_name = os.path.join(directory, name)
                    target_name = os.path.join(f'/Users/niaapple/Downloads/{folder}', name)
                    try:
                        logging.info(f'Moving: {source_name} to: {target_name}')
                        os.rename(source_name, target_name)
                    except Exception as e:
                        logging.error(f"Error moving {source_name} to {target_name}: {e}")
        break

if __name__ == "__main__":
    root = "/Users/niaapple/Downloads"
    organize_downloads(root)