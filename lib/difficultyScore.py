from lib import craftingTree

def diffScoreRecur(itemCraftTree, depth):
    if depth > 3:
        return 0
    elif isinstance(itemCraftTree, list):
        score = 1
        for ingredient in itemCraftTree:
            score += diffScoreRecur(ingredient, depth + 1)
        return score
    elif isinstance(itemCraftTree, dict):
        for key in itemCraftTree.keys():
            if itemCraftTree[key] == "":
                return 0
            elif isinstance(itemCraftTree[key], list):
                return diffScoreRecur(itemCraftTree[key], depth)
    elif isinstance(itemCraftTree, str):
        return 0

def diffScore(itemCraftTree):
    return diffScoreRecur(itemCraftTree, 0)


def craftingDiff(craftTree):
    itemIDs = craftTree.keys()
    diffScoreDict = {}
    for itemID in itemIDs:
        itemCraftTree = craftTree[itemID]
        diffScoreDict[itemID] = diffScore(itemCraftTree)
    return diffScoreDict

def difficultyScoreForAllModItems():
    craftTree = craftingTree.craftingTreeForAllMods()
    diffScoreDict = craftingDiff(craftTree)
    return diffScoreDict
