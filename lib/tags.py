from lib import paths, const
import os
import json

def getItemID(tagFolder, tagParent, tagChild):
    jsonFileLoc = os.path.join(tagFolder, tagParent, tagChild+".json")
    if os.path.isfile(jsonFileLoc):
        idDict = json.load(open(jsonFileLoc, "r"))
        if "values" in idDict.keys():
            if isinstance(idDict["values"], list):
                if isinstance(idDict["values"][0], str):
                    return idDict["values"][0]
    return const.Err

def processesTagValue(forgeTags, tagValue, tagFolder, tagName):
    tagValue = tagValue.replace("#forge:", "")
    tagHierachy = tagValue.split("/")
    if len(tagHierachy) == 1:
        if tagName not in forgeTags.keys():
            forgeTags[tagName] = []
        if tagHierachy[0] not in forgeTags[tagName]:
            forgeTags[tagName].append(tagHierachy[0])
    elif len(tagHierachy) == 2:
        tagParent = tagHierachy[0]
        tagChild = tagHierachy[1]
        itemID = getItemID(tagFolder, tagParent, tagChild)
        if itemID != const.Err:
            if tagParent not in forgeTags.keys():
                forgeTags[tagParent] = {}
            if tagChild not in forgeTags[tagParent].keys():
                forgeTags[tagParent][tagChild] = []
            if itemID not in forgeTags[tagParent][tagChild]:
                forgeTags[tagParent][tagChild].append(itemID)

def growTagDict(tagFolder, startingForgeTags):
    tagDirNames = os.listdir(tagFolder)
    forgeTags = startingForgeTags
    for tagDirName in tagDirNames:
        tagDir = os.path.join(tagFolder, tagDirName)
        if os.path.isfile(tagDir):
            tagName = tagDirName.replace(".json","")
            tag = json.load(open(tagDir, "r"))
            if isinstance(tag["values"], list):
                for tagValue in tag["values"]:
                    processesTagValue(forgeTags, tagValue, tagFolder, tagName)


def getAllTagDict():
    modFolders = os.listdir(paths.extractedFolder)
    forgeTags = {}
    for modFolder in modFolders:
        tagFolder = paths.tagFolder(modFolder)
        growTagDict(tagFolder, forgeTags)
    return forgeTags

def itemsFmSubEnt(tagSubEnt):
    if isinstance(tagSubEnt, list):
        return tagSubEnt
    if isinstance(tagSubEnt, dict):
        keys = tagSubEnt.keys()
        items = []
        for key in keys:
            items += itemsFmSubEnt(tagSubEnt[key])
        return items
    return []

def getTagItems(forgeTag, tagDict):
    tagItems = []
    forgeTagRoot = "forge:"
    if forgeTagRoot in forgeTag:
        forgeTag = forgeTag.replace(forgeTagRoot, "")
        tagHierachy = forgeTag.split("/")
        tagSubEnt = {}
        if len(tagHierachy) == 1:
            if tagHierachy[0] not in tagDict.keys():
                return []
            tagSubEnt = tagDict[tagHierachy[0]]
        elif len(tagHierachy) == 2:
            parent = tagHierachy[0]
            child = tagHierachy[1]
            if parent not in tagDict.keys():
                return []
            if child not in tagDict[parent].keys():
                return []
            tagSubEnt = tagDict[parent][child]
        tagItems = itemsFmSubEnt(tagSubEnt)

    return tagItems