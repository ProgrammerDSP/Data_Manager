import os
import shutil

path = input("Enter the path : ")

all_files = []
all_dirs = []

paths = {}

def movefiles(path):

    try:
        os.chdir(path)
        os.mkdir("Images")
        os.mkdir("Files")
        os.mkdir("Documents")
        os.mkdir("Videos")
        os.mkdir("Audio")
    
    except Exception as e:
        pass

    for f in all_files:

        try:

            if ".png" in f or ".jpg" in f or ".jpeg" in f or ".jfif" in f:
                filepath = paths[f]
                path = os.path.join(os.getcwd(), "Images")
                shutil.move(filepath, path)

            elif ".py" in f or ".js" in f or ".html" in f or ".txt" in f or ".css" in f:
                filepath = paths[f]
                path = os.path.join(os.getcwd(), "Files")
                shutil.move(filepath, path)

            elif ".xlsx" in f or ".doc" in f or ".xlx" in f or ".pdf" in f:
                filepath = paths[f]
                path = os.path.join(os.getcwd(), "Documents")
                shutil.move(filepath, path)

            elif ".mp4" in f or ".mkv" in f or ".gif" in f or ".webm" in f or ".flv" in f:
                filepath = paths[f]
                path = os.path.join(os.getcwd(), "Videos")
                shutil.move(filepath, path)

            elif ".mp3" in f:
                filepath = paths[f]
                path = os.path.join(os.getcwd(), "Audio")
                shutil.move(filepath, path)

        except Exception as e:
            pass

while True:
    for root, directories, files in os.walk(path, topdown=False):
        for name in files:
            all_files.append(name)
            pathF = os.path.join(root, name)
            paths[name] = pathF

        for name in directories:
            all_dirs.append(name)
            pathF = os.path.join(root, name)
            paths[name] = pathF

    movefiles(path)