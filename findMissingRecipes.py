from lib import recipes, lang, extract, jsonExport

def findAllMissingRecipes():
    recipeDict = recipes.mergedRecipeDictOfAllMods()
    langDict = lang.mergedLangDictOfAllMods()

    missingRecipeItems = {}
    for itemID in langDict.keys():
        if itemID not in recipeDict.keys():
            missingRecipeItems[itemID] = langDict[itemID]
    jsonExport.exportFile(missingRecipeItems, "missingRecipes")

if __name__ == "__main__":
    extract.forceExtractAllModsInFolder()
    findAllMissingRecipes()

