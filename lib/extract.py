
import zipfile
import shutil
import os
from lib import paths

def extractAllModsInFolder():
    modFiles = os.listdir(paths.modsFolder)
    for modFile in modFiles:
        with zipfile.ZipFile(os.path.join(paths.modsFolder, modFile), "r") as zip:
            print("extracting", modFile)
            extractModFolder = os.path.join(paths.extractedFolder, modFile)
            os.mkdir(extractModFolder)
            zip.extractall(extractModFolder)
    print("extraction complete!")

def forceExtractAllModsInFolder():
    if os.path.isdir(paths.extractedFolder):
        print("Deleting temp data")
        shutil.rmtree(paths.extractedFolder)
    os.mkdir(paths.extractedFolder)
    extractAllModsInFolder()

def extractAllModsIfFolderNotExist():
    if os.path.isdir(paths.extractedFolder):
        return
    os.mkdir(paths.extractedFolder)
    extractAllModsInFolder()

