#import serial
import time
import json
import random
import sys
from Database.DB import Database
#from wsgiref.types import InputStream

class DispenseDrink:
    def __init__(self):
        self.db = Database()
        self.drinkList = self.db.queryDrinkDB()
    
    def handler(self,mode,drinkID,userID):
        #Print file for testing
        if mode == '0':
            self.writeToFile(drinkID,userID)
        #Dispense drink
        if mode == '1':
            self.dispense(drinkID,userID)
        #Random recipe
        if mode == '2':
            self.randomRecipe(userID)
        #Random drink
        if mode == '3':
            self.genRandomDrink(10,userID)
        
    def dispense(self,drinkID,userID):
        drinkData = list(self.db.getDrinkFromID(drinkID)[0])
        pumpArr = self.db.getPumpList()
        drinkCommand = ""
        err = self.db.takeMoney(userID,drinkData[2])
        print(err)
        #Generate pump string 31 22 12 means Pump3:1push and so on
        if err == None:
            for i in range(6):
                for j in range(6):
                    if drinkData[4][i].lower() == pumpArr[j][0]:
                        if pumpArr[j][1] > 0:
                            drinkCommand += str(pumpArr[j][2]) + "" + str(drinkData[5][i])
                        else:
                            drinkCommand += str(pumpArr[j][2]) + "0"
        else:
            print("Not enough money")
        
        #Update Pump
        for i in range(6):
            self.db.updatePump(drinkData[4][i].lower(),drinkData[5][i])
        
        drinkCommand = "0" + drinkCommand
        #Result  
        print(drinkCommand)
        
    def writeToFile(self,drinkID,userID):
        info = self.db.getDrinkFromID(drinkID)
        data = {'user' : userID,
                'drink': info}

        with open("DRINK.json", 'w') as outfile:
            json.dump(data, outfile, indent=4)
    
    def randomRecipe(self,userID):
        randomRecipe = self.db.getRandomRecipe()
        self.dispense(randomRecipe[1],userID)
        self.writeToFile(randomRecipe[1],userID)
    
    def genRandomDrink(self,val,userID):
        pumpArr = self.db.getPumpList()
        drinkCommand = ""
        #Take 30 THB
        # err = self.db.takeMoney(userID,30)
        # print(err)
        
        err = None

        #Generate pump string 31 22 12 means Pump3:1push and so on
        if err == None:
            arr = [0,0,0,0,0,0]
            #Random nums
            for i in range(val):
                index = random.randrange(0,6)
                arr[index] += 1
            
            for i in range(6):
                drinkCommand += str(i + 1) + str(arr[i])
            
            drinkCommand = "0" + drinkCommand
            print(drinkCommand)
            return arr

uwu = DispenseDrink()
# # print(uwu.genRandomDrink(10,10))
uwu.handler(sys.argv[1],sys.argv[2],sys.argv[3])

