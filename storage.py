import json


DATA_FILE = "data/expences.json"


def loadExpences():
    try:
        with open(DATA_FILE,"r", encoding="utf-8")as file:
            expences = json.load(file)

        return expences
    except FileNotFoundError:
        return []


    except json.JSONDecodeError:
        raise ValueError("JSON file is corrupted!")

    
def saveExpences():
    with open(DATA_FILE, "w",encoding="utf-8")as file:
        json.dump(expences, file , indent=4, ensure_ascii=False)