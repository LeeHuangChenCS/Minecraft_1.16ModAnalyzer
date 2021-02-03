import json
import os
from lib import const, paths

def getResult(recipe):
    if isinstance(recipe["result"], str):
        return recipe["result"]
    if isinstance(recipe["result"], list):
        if isinstance(recipe["result"][0], str):
            return recipe["result"][0]
        if isinstance(recipe["result"][0]["item"], str):
            return recipe["result"][0]["item"]
    if isinstance(recipe["result"]["item"], str):
        return recipe["result"]["item"]
    return const.Err

def appendToRecipeDict(recipeDictParent, recipe):
    resultID = getResult(recipe)
    if resultID != const.Err:
        if resultID not in recipeDictParent.keys():
            recipeDictParent[resultID]=[]
        recipeDictParent[resultID].append(recipe)

def recipeDict(modRecipeFolder):
    allRecipeFiles = os.listdir(modRecipeFolder)
    recipeDictRet = {}
    for recipeFile in allRecipeFiles:
        recipeDir = os.path.join(modRecipeFolder, recipeFile)
        if os.path.isfile(recipeDir):
            recipe = json.load(open(recipeDir, "r"))
            appendToRecipeDict(recipeDictRet, recipe)
    return recipeDictRet

def mergeRecipeDicts(recipeDictParent, recipeDictAdd):
    for addKey in recipeDictAdd.keys():
        recipeList = recipeDictAdd[addKey]
        for recipe in recipeList:
            appendToRecipeDict(recipeDictParent, recipe)
    return recipeDictParent

def getAllRecipesIncludingSubfolders(recipeFolderLoc):
    dir1Names = os.listdir(recipeFolderLoc)
    recipeDictRet = recipeDict(recipeFolderLoc)
    for dir1Name in dir1Names:
        dir1 = os.path.join(recipeFolderLoc, dir1Name)
        if os.path.isdir(dir1):
            mergeRecipeDicts(recipeDictRet, recipeDict(dir1))
            dir2Names = os.listdir(dir1)
            for dir2Name in dir2Names:
                dir2 = os.path.join(dir1, dir2Name)
                if os.path.isdir(dir2):
                    mergeRecipeDicts(recipeDictRet, recipeDict(dir2))
    return recipeDictRet

def mergedRecipeDictOfAllMods():
    modFolders = os.listdir(paths.extractedFolder)
    allRecipe = {}
    for modFolder in modFolders:
        modDir = os.path.join(paths.extractedFolder, modFolder)
        modRecipeFolder = paths.recipeFolder(modDir)
        modRecipes = getAllRecipesIncludingSubfolders(modRecipeFolder)
        mergeRecipeDicts(allRecipe, modRecipes)
    return allRecipe
