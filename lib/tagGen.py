import os
import json
import re
from lib import paths, lang

defaultDataPackName = "customtags"
defaultDataPackDesc = [
    {
        "text": "custom tags",
        "color": "gold"
    }
]


def packMcMetaDict(dataPackDesc):
    return {
        "pack": {
            "pack_format": 6,
            "description": dataPackDesc
        }
    }

def tagJson():
    return {
        "replace": False,
        "values": []
    }

def itemJson(itemID):
    itemDict = tagJson()
    itemDict["values"].append(itemID)
    return itemDict

def tagValueEntry(tagName, itemName):
    return f"#forge:{tagName}/{itemName}"

def createBaseDatapack():
    dataPackLocation = os.path.join(paths.dataPackLocation, defaultDataPackName)
    tagFolderLocation = os.path.join(dataPackLocation, paths.tagLocation)
    paths.makeAllSubfolders(tagFolderLocation)

    with open(os.path.join(dataPackLocation, "pack.mcmeta"), "w") as f:
        json.dump(packMcMetaDict(defaultDataPackDesc), f, indent=2)

def cleanStrForFilename(regFileName):
    regFileName = regFileName.strip().replace(" ","_")
    regFileName = re.sub("\W","", regFileName)
    regFileName = regFileName.lower()
    return regFileName

# nameItemDict:
#   key: name of the item
#   val: the id of the item
def generateTag(tagName, nameItemDict):
    tagFolderLocation = os.path.join(paths.dataPackLocation, defaultDataPackName, paths.tagLocation)
    tagLocation = os.path.join(tagFolderLocation, tagName)
    paths.makeAllSubfolders(tagLocation)
    tagName = cleanStrForFilename(tagName)
    tagDict = tagJson()

    for itemName in nameItemDict:
        itemID = nameItemDict[itemName]
        itemFileName = cleanStrForFilename(itemName)
        tagDict["values"].append(tagValueEntry(tagName, itemFileName))
        with open(os.path.join(tagLocation, itemFileName+".json"), "w") as f:
            json.dump(itemJson(itemID), f, indent=2)
    with open(os.path.join(tagFolderLocation, tagName+".json"), "w") as f:
        json.dump(tagDict, f, indent=2)

# nameKeywordDict
#   key: tagName
#   val: keyword to search items
def createTagsFromNameKeywordDict(nameKeywordDict):
    createBaseDatapack()

    reverseLang = lang.reverseLangDict(lang.mergedLangDictOfAllMods())

    for tagName in nameKeywordDict.keys():
        keyword = nameKeywordDict[tagName]
        nameItemDict = {}

        for itemName in reverseLang.keys():
            if keyword in itemName:
                nameItemDict[itemName] = reverseLang[itemName]
        generateTag(tagName, nameItemDict)

