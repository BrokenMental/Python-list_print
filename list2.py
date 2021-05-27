import os

root_name = "./"
for (root, dirs, files) in os.walk(root_name):
    print("\n#root : " + root)
    
    if len(dirs) > 0:
        for dir_name in dirs:
            print("folder: " + dir_name)

    if len(files) > 0:
        for file_name in files:
            print("file: " + file_name)
