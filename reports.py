import csv
from expences import getAllExpences

def totalExpences():
    expenses = getAllExpences()

    total = 0

    for e in expenses:
        total += e["amount"]

    return total     

def exportToCSV():
    expenses = getAllExpences()

    filePath = "data/expemces.csv"

    fieldNames = ["id ", "title" , "amount" , "category" , "date"]

    with open(filePath, "w" , newLine="", encoding = "utf-8") as file:
        writer = csv.DictWriter(file,fieldnames=fieldNames)
        writer.writeheader()
        writer.writerows(expenses)

    return filePath