import os

root = os.path.join("/Users/niaapple", "Downloads")
for directory, subdir_list, file_list in os.walk(root):
    print("\n\nDirectory:", directory)
    for name in subdir_list:
        print('Subdirectory:', name)
    for name in file_list:
        #identify downloads by file extension type
        if name.endswith(('.gif', '.png', '.PNG', '.jpeg', '.jpg', '.heic', '.HEIC', 'webp', 'avif')):
            print("File: (Image)", name)
        if name.endswith('.pdf'):
            print("File: (PDF)", name)
        if name.endswith(('.ics', '.docx', '.epub')):
            print("File: (Documents)", name)
        if name.endswith('.pptx'):
            print("File: (Presentation)", name)
        if name.endswith(('.xml', '.html')):
            print("File: (Developer)", name)
        if name.endswith(('.ddmg', '.zip')):
            print("File: (Other)", name)