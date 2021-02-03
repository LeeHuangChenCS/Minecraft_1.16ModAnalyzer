import os

modsFolder = "mods"
extractedFolder = "extracted"
resultsFolder = "results"
inputFolder = "input"

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
    return os.path.join(extractedFolder, modFolder, "data", "forge", "tags", "items")
