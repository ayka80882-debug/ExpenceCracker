import uuid
from datatime import date
from storage import *
from validitions import *
from execeptions import expensesNotFound


def addExpence(title,amount,category):
    expenses = loadExpences

    expence = {
        "id" : str(uuid.uuid4())[:8],
        "title": validateTitle(title),
        "amount": validateAmount(amount),
        "category":validataCategory(category),
        "date": date.today().isoformat()

    }
    expenses.append(expence)
    saveExpences(expenses)
    return expence

def getAllExpenses():
    return loadExpences()

def searchExpenses(expenceID):
    expenses = loadExpences()

    for expence in expenses:
        if expence["id"] == expenceID:
            return expence
        
    expensesNotFound()        

def updateExpence(expenceID, title , amount ,category):
    expences = loadExpences()    

    for e in expences:
        if e["id"]==expenceID:
            e["title"]= validateTitle(title)
            e["amount"]= validateAmount(amount)
            e["category"]= validataCategory(category )
            
            saveExpences(expences)
            return e
        
    expensesNotFound()

def deleteExpence(expenceID):
    expences = loadExpences()
    for e in expences:
        if e["id"] == expenceID:
            expences.remove(e)
            saveExpences(expences)
            
            return True
    
    expensesNotFound()
