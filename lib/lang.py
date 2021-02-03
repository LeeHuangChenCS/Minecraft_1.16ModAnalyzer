import re
import json
import os
from lib import paths

def itemTagToID(langTag):
    return langTag[5:].replace(".", ":")

def blockTagToID(langTag):
    return langTag[6:].replace(".", ":")

def itemDictFmLangFile(langFileDir):
    itemDict = {}
    file = open(langFileDir, "r")
    fileContent = file.read()
    file.close()
    fileContentFiltered = re.sub("//.*\n", "", fileContent)
    langObj = json.loads(fileContentFiltered)
    for key in langObj.keys():
        if key[0:5] == "item.":
            itemID = itemTagToID(key)
            itemName = langObj[key]
            itemDict[itemID] = itemName
        elif key[0:6] == "block.":
            itemID = blockTagToID(key)
            itemName = langObj[key]
            itemDict[itemID] = itemName
    return itemDict

def mergeLangDicts(langDictParent, langDictAdd):
    for keyAdd in langDictAdd.keys():
        if keyAdd not in langDictParent.keys():
            langDictParent[keyAdd] = langDictAdd[keyAdd]
    return langDictParent

def mergedLangDictOfAllMods():
    modFolders = os.listdir(paths.extractedFolder)
    allLang = {}
    for modFolder in modFolders:
        modDir = os.path.join(paths.extractedFolder, modFolder)
        langDir = paths.USLangFile(modDir)
        modLang = itemDictFmLangFile(langDir)
        mergeLangDicts(allLang, modLang)
    return allLang
