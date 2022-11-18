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
        
    def dispense(self,drinkID):
        drinkData = list(self.db.getDrinkFromID(drinkID)[0])
        pumpArr = self.db.getPumpList()
        drinkCommand = ""
        #Generate pump string 31 22 12 means Pump3:1push and so on
        for i in range(6):
            for j in range(6):
                if drinkData[4][i].lower() == pumpArr[j][0]:
                    if pumpArr[j][1] > 0:
                        drinkCommand += str(pumpArr[j][2]) + "" + str(drinkData[5][i])
                    else:
                        drinkCommand += str(pumpArr[j][2]) + "0"
        
        #Update Pump
        for i in range(6):
            self.db.updatePump(drinkData[4][i].lower(),drinkData[5][i])
        
        drinkCommand = "0" + drinkCommand
        #Result  
        print(drinkCommand)
    

dis = DispenseDrink()
dis.dispense(1)

"""
=======================================================
            This code will sort input datas
            to match pump order in drinkList.json
=======================================================
"""
# def sortDrink():
#     f = open ('./src/PythonTkinter/Database/drinkList.json', "r")
#     drinkOrder = json.loads(f.read())
#     drinks = []
#     sortedDrink = []
    
#     #Insert json drink to dict
#     for drink in drinkOrder.keys():
#         drinkDict = {}
#         drinkDict["name"] = drink
#         drinkDict["amountLeft"] = drinkOrder[drink]
#         drinks.append(drinkDict)
    
#     #Nested loop to sort the item
#     for drink in drinks:
#         for data in dummyData:
#             if data["drinkName"] == drink["name"]:
#                 sortedDrink.append(data)
#                 break
    
#     return sortedDrink
        

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
    
