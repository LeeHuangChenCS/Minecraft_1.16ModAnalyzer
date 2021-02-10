import os

modsFolder = "mods"
extractedFolder = "extracted"
resultsFolder = "results"
inputFolder = "input"
tagLocation = os.path.join("data", "forge", "tags", "items")
dataPackLocation = os.path.join(resultsFolder, "datapacks")

def modName(modFolder):
    return os.listdir(os.path.join(modFolder, "assets"))[0]

def assetsFolder(modFolder):
    return os.path.join(modFolder, "assets", modName(modFolder))

def USLangFile(modFolder):
    return os.path.join(assetsFolder(modFolder), "lang", "en_us.json")

def recipeFolder(modFolder):
    modNameVal = modName(modFolder)
    return os.path.join(modFolder, "data", modNameVal, "recipes")

def tagFolder(modFolder):
    return os.path.join(extractedFolder, modFolder, tagLocation)

def findAllSubfolders(fileOrFolderPath):
    firstCompare = True
    workingPath = fileOrFolderPath
    subfolders = []
    while len(workingPath) > 0:
        folder, tail = os.path.split(workingPath)
        if firstCompare and ("." in tail):
            firstCompare = False
        else:
            if len(tail) > 0:
                subfolders.insert(0, tail)
        workingPath = folder.strip()
    return subfolders

def makeAllSubfolders(fileOrFolderPath):
    allSubFolders = findAllSubfolders(fileOrFolderPath)
    workingFolder = ""
    for folder in allSubFolders:
        workingFolder = os.path.join(workingFolder, folder)
        if not os.path.exists(workingFolder):
            os.mkdir(workingFolder)
