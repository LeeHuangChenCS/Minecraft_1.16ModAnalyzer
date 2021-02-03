import os
import json
from lib import paths

def exportFile(exportObj, fileName):
    if not os.path.isdir(paths.resultsFolder):
        os.mkdir(paths.resultsFolder)

    with open(os.path.join(paths.resultsFolder, fileName+".json"), "w") as f:
        json.dump(exportObj, f, indent=2)