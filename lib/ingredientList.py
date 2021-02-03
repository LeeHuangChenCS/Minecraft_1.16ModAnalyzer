from lib import craftingTree

def ingredientListRecur(craftEnt, returnList):
    if isinstance(craftEnt, list):
        for ingredient in craftEnt:
            ingredientListRecur(ingredient, returnList)
    elif isinstance(craftEnt, dict):
        for key in craftEnt.keys():
            if craftEnt[key] == "":
                returnList.append(key)
            elif isinstance(craftEnt[key], list):
                ingredientListRecur(craftEnt[key], returnList)

def ingredientListDict(craftTree):
    ingredientListDictRet = {}
    for itemID in craftTree.keys():
        ingredients = []
        ingredientListRecur(craftTree[itemID], ingredients)
        ingredientListDictRet[itemID] = ingredients
    return ingredientListDictRet


def ingredientListForAllModItems():
    craftTree = craftingTree.craftingTreeForAllMods()
    ingredientList = ingredientListDict(craftTree)
    return ingredientList
