from lib import paths, defaultValues
import os

def shapelessDict(recipeName="", result="", resultNum=1, ingredientIDs=defaultValues.emptyList):
    return {
        "type" : "shapeless",
        "recipeName" : recipeName,
        "result" : result,
        "resultNum": resultNum,
        "ingredientIDs": ingredientIDs
    }

def ctID(minecraftID):
    return f"<item:{minecraftID}>"

def craftingShapeless(recipeName, resultID, resultNum, ingredientIDs):
    ingredientIDString = ""
    for i in range(0, len(ingredientIDs)):
        ingredientIDString += "\n\t\t"
        ingredientIDString += (ctID(ingredientIDs[i]))
        if i < (len(ingredientIDs) - 1):
            ingredientIDString += ctID(ingredientIDs[i])

    return f"craftingTable.addShapeless(\"{recipeName}\",\n\t{ctID(resultID)}*{resultNum}, [{ingredientIDString}]);\n"

def craftingShaplessFmDict(recipeDict):
    return craftingShapeless(recipeDict["recipeName"], recipeDict["result"], recipeDict["resultNum"], recipeDict["ingredientIDs"])

def scriptGen(commandDictArray):
    script = ""
    for commandDict in commandDictArray:
        commandType = commandDict["type"]
        if commandType == "shapeless":
            script += craftingShaplessFmDict(commandDict)
    return script

def exportScript(commandDictArray, filename):
    script = scriptGen(commandDictArray)
    with open(os.path.join(paths.resultsFolder,filename+".zs"), "w") as f:
        f.write(script)
