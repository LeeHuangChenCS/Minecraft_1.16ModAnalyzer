import json
import os
from lib import paths, craftTweaker, jsonExport

if __name__ == "__main__":
    saleComboDict = json.load(open(os.path.join(paths.inputFolder, "saleCombos.json"), "r"))
    salePrices = json.load(open(os.path.join(paths.inputFolder, "saleComboPrices.json"), "r"))
    saleRecipeDicts = []
    for salePricePair in salePrices:
        comboName = salePricePair[0]
        comboSale = salePricePair[1]
        mealsInCombo = saleComboDict[comboName]["ingredients"]
        saleComboDict[comboName]["sale"] = comboSale
        saleRecipeDict = craftTweaker.shapelessDict(comboName, "minecraft:emerald", comboSale, mealsInCombo)
        saleRecipeDicts.append(saleRecipeDict)
    craftTweaker.exportScript(saleRecipeDicts, "saleRecipes")
    jsonExport.exportFile(saleComboDict, "saleCombos_0.0.3")
