#import serial
import time
import json
import random
from Database.DB import Database
#from wsgiref.types import InputStream

class DispenseDrink:
    def __init__(self):
        self.db = Database()
        self.drinkList = self.db.queryDrinkDB()
        
        # for drink in self.drinkList:
        #     print(drink)
    def checkDrink(self):
        pass
        
    def dispense(self,drinkID):
        drinkData = list(self.db.getDrinkFromID(drinkID)[0])
        pumpArr = self.db.getPumpList()
        arr = ""
        print(drinkData)
        print(pumpArr)
        for i in range(6):
            for j in range(6):
                if drinkData[4][i].lower() == pumpArr[j][0]:
                    
                    arr += str(pumpArr[j][2]) + "" + str(drinkData[5][i])
        
        print(arr)
        for i in range(6):
            self.db.updatePump(drinkData[4][i].lower(),drinkData[5][i])
    

dis = DispenseDrink()
dis.dispense(1)





"""
=======================================================
            This code will sort input datas
            to match pump order in drinkList.json
=======================================================
"""
def sortDrink():
    f = open ('./src/PythonTkinter/Database/drinkList.json', "r")
    drinkOrder = json.loads(f.read())
    drinks = []
    sortedDrink = []
    
    #Insert json drink to dict
    for drink in drinkOrder.keys():
        drinkDict = {}
        drinkDict["name"] = drink
        drinkDict["amountLeft"] = drinkOrder[drink]
        drinks.append(drinkDict)
    
    #Nested loop to sort the item
    for drink in drinks:
        for data in dummyData:
            if data["drinkName"] == drink["name"]:
                sortedDrink.append(data)
                break
    
    return sortedDrink
        

def genRandomDrink(val):
    arr = [0,0,0,0,0,0]
    for i in range(val):
        index = random.randrange(0,6)
        arr[index] += 1
    return arr


#sortDrink() 
#print(genRandomDrink(10))
# while True:
#     drink.dispense()
    
