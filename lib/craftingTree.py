from lib import lang, tags, recipes, extract, jsonExport

def entDepth(ent):
    if isinstance(ent, dict):
        maxDepth=0
        keys = ent.keys()
        for key in keys:
            depth = entDepth(ent[key])
            if depth > maxDepth:
                maxDepth = depth
        return maxDepth + 1
    if isinstance(ent,list):
        maxDepth=0
        for idx in ent:
            depth = entDepth(idx)
            if depth > maxDepth:
                maxDepth = depth
        return maxDepth + 1
    return 1


def maxCraftTree(parentTree, childTree):
    parentDepth = entDepth(parentTree)
    childDepth = entDepth(childTree)
    if parentDepth > childDepth:
        return parentTree
    else:
        return childTree

def getIngredientsListFromIngredientsNode(nodeList):
    ingList = []
    for entry in nodeList:
        if isinstance(entry, list):
            ingList += entry
        else:
            ingList.append(entry)
    return ingList

def getCraftingTree(itemID, tagDict, allRecipeDict, ingredientListRecur):
    if itemID in allRecipeDict.keys():
        recipeDict = allRecipeDict[itemID][0]
        ingredientList = []
        if "ingredients" in recipeDict.keys():
            ingredientList = getIngredientsListFromIngredientsNode(recipeDict["ingredients"])
        elif "key" in recipeDict.keys():
            for key in recipeDict["key"].keys():
                ingredientList.append(recipeDict["key"][key])
        elif "ingredient" in recipeDict.keys():
            ingredientList = [recipeDict["ingredient"]]
        processedList = []
        for ingredient in ingredientList:
            if "tag" in ingredient.keys():
                forgeTag = ingredient["tag"]
                ingredientIDs = tags.getTagItems(forgeTag, tagDict)
                maxCraftingTree = {}
                for ingredientID in ingredientIDs:
                    if ingredientID not in ingredientListRecur:
                        ingredientListRecur.append(ingredientID)
                        ingCraftTree = getCraftingTree(ingredientID, tagDict, allRecipeDict, ingredientListRecur)
                        maxCraftingTree = maxCraftTree(maxCraftingTree, ingCraftTree)

                if maxCraftingTree != {}:
                    processedList.append(maxCraftingTree)
            if "item" in ingredient.keys():
                ingID = ingredient["item"]
                if ingID not in ingredientListRecur:
                    ingredientListRecur.append(ingID)
                    ingCraftTree = getCraftingTree(ingredient["item"], tagDict, allRecipeDict, ingredientListRecur)
                    if ingCraftTree != {}:
                        processedList.append(ingCraftTree)
        if not processedList:
            processedList = ""
        return {itemID: processedList}
    else:
        return {itemID: ""}

def craftingTree(langDict, tagDict, recipeDict):
    recipeHierachy = {}
    for itemID in langDict.keys():
        ingredientList = [itemID]
        craftingTree = getCraftingTree(itemID, tagDict, recipeDict, ingredientList)
        recipeHierachy[itemID] = craftingTree[itemID]
    return recipeHierachy

def craftingTreeForAllMods():
    langDict = lang.mergedLangDictOfAllMods()
    tagDict = tags.getAllTagDict()
    recipeDict = recipes.mergedRecipeDictOfAllMods()
    craftTree = craftingTree(langDict, tagDict, recipeDict)
    return craftTree
