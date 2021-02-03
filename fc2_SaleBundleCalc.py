from lib import extract, jsonExport, difficultyScore, ingredientList, paths, csvHandler, lang
import json
import os

def mergeLists(listParent, listChild):
    for item in listChild:
        if item not in listParent:
            if "minecraft" not in item:
                listParent.append(item)

def CalcDiffAnalysisForAllCombo(saleComboDict):
    extract.extractAllModsIfFolderNotExist()
    diffScoreDict = difficultyScore.difficultyScoreForAllModItems()
    ingredients = ingredientList.ingredientListForAllModItems()
    langDict = lang.mergedLangDictOfAllMods()
    comboDiffAnalysis = {}
    for comboKey in saleComboDict.keys():
        comboInfo = {}
        comboIngredients = saleComboDict[comboKey]["ingredients"]
        subIngredients = []
        comboDifficulty = 0
        comboMeals = ""
        for ingredient in comboIngredients:
            difficulty = 0
            if ingredient in diffScoreDict.keys():
                difficulty = diffScoreDict[ingredient]

                mergeLists(subIngredients, ingredients[ingredient])
            comboInfo[ingredient] = difficulty
            comboDifficulty += difficulty
            if ingredient in langDict.keys():
                ingName = langDict[ingredient]
            else:
                ingName = ingredient
            if comboMeals == "":
                comboMeals = ingName
            else:
                comboMeals += "; "
                comboMeals += ingName

        comboInfo["ingredients"] = subIngredients
        comboInfo["meals"] = comboMeals
        comboInfo["totalDifficulty"] = comboDifficulty
        comboInfo["ingredientListLength"] = len(subIngredients)
        comboDiffAnalysis[comboKey] = comboInfo
    return comboDiffAnalysis

def exportMatrixInfo(comboDiffAnalysis, outFile):
    matrix = []
    header = ["Combo", "Craft Diff", "Ing Len", "Meals"]
    matrix.append(header)
    for comboKey in comboDiffAnalysis.keys():
        combo = comboDiffAnalysis[comboKey]
        row = [comboKey, combo["totalDifficulty"], combo["ingredientListLength"], combo["meals"]]
        matrix.append(row)
    csvHandler.writeToCSVFile(outFile, matrix)


if __name__ == "__main__":
    saleComboDict = json.load(open(os.path.join(paths.inputFolder, "saleCombos.json"), "r"))
    comboDiffAnalysis = CalcDiffAnalysisForAllCombo(saleComboDict)
    jsonExport.exportFile(comboDiffAnalysis, "FarmingCrossingComboDifficulty")

    csvFileLog = os.path.join(paths.resultsFolder, "FarmingCrossingComboDifficulty.csv")
    exportMatrixInfo(comboDiffAnalysis, csvFileLog)
