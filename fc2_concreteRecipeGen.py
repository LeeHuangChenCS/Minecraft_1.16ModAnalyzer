from lib import craftTweaker, vanillaLang

if __name__ == "__main__":
    recipeDictArray = []
    for color in vanillaLang.colorArray():
        productName = f"{color} Concrete"
        ingName = f"{color} Concrete Powder"
        productID = vanillaLang.itemLookup(productName)
        ingId = vanillaLang.itemLookup(ingName)
        recipeName = productName.lower().replace(" ","_") + "_from_powder"
        recipeDict = craftTweaker.shapelessDict(recipeName, productID, 1, [ingId])
        recipeDictArray.append(recipeDict)
    craftTweaker.exportScript(recipeDictArray, "concrete_from_powder")
