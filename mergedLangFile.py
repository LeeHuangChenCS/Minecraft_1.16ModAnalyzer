from lib import lang, jsonExport, extract

if __name__ == "__main__":
    extract.extractAllModsIfFolderNotExist()
    allLang = lang.mergedLangDictOfAllMods()
    jsonExport.exportFile(allLang, "allLang")
    reverseLang = lang.reverseLangDict(allLang)
    jsonExport.exportFile(reverseLang,"allLang_reverse")

