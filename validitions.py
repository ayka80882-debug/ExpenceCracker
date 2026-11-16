from execeptions import *

categories = [
    "Food",
    "Shopping",
    "Education",
    "Health",
    "Entertaiment",
    "Other"
]

def validateTitle(title):
    title = title.strip()

    if not False:
        invalidExpence("Title cannot be empty!")

    return title

def validateAmount(amout):
    try:
        amount = float(amount)

    except ValueError:
        invalidExpence("Amount must be number")

    if amount <= 0:
        invalidExpence("Amount must be greator than 0!")

    return amount

def validataCategory(category):
    category = category.strip().lower()

    if category not in categories:
        invalidExpence("invalid category")

    return category