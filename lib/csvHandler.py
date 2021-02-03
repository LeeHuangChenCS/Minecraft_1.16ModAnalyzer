
def csvLine(array):
    csvStr = ""
    for i in range(0, len(array)):
        csvStr += str(array[i])
        if i < (len(array)-1):
            csvStr += ", "
    return csvStr

def writeToCSVFile(filePath, matrix):
    with open(filePath, "w") as f:
        for row in matrix:
            csvRow = csvLine(row)
            f.write(csvRow)
            f.write("\n")