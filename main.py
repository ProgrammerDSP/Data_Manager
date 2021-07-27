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
        os.mkdir("Videos")
        os.mkdir("Documents")
        os.mkdir("Audio")
        os.mkdir("Files")

    except Exception as e:
        pass

    for f in all_files:
        try:
            if ".png" in f or ".jpg" in f or ".jpeg" in f:
                filespath = paths[f]
                path = os.path.join(os.getcwd() , "Images")
                shutil.move(filespath , path)

            elif ".py" in f or ".js" in f:
                filespath = paths[f]
                path = os.path.join(os.getcwd() , "Files")
                shutil.move(filespath , path)

        except:
            pass

while True:
    for path , folders , files in os.walk(path, topdown=False):
        for n in files:
            all_files.append(n)
            pathF = os.path.join(path , n)
            paths[n] = pathF

        for n in folders:
            all_dirs.append(n)
            pathF = os.path.join(path , n)
            paths[n] = pathF

    movefiles(path)