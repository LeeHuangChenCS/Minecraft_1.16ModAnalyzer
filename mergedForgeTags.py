from lib import tags, jsonExport, extract

if __name__ == "__main__":
    extract.extractAllModsIfFolderNotExist()
    forgeTags = tags.getAllTagDict()
    jsonExport.exportFile(forgeTags, "mergedForgeTags")
