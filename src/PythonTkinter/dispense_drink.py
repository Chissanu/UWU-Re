import myQueue
import serial
import time
import json
#from wsgiref.types import InputStream

dummyData = [{"drinkName": "CustomDrink1",
              "drinkID": 1,
              "drinkList": ["Juice","Tea","Coffee","Cider","Sodar","Water"],
              "timesPressed": [1,2,1,3,4,3]
              },
             {"drinkName": "CustomDrink2",
              "drinkID": 2,
              "drinkList": ["Juice","Tea","Coffee","Cider","Sodar","Water"],
              "timesPressed": [1,2,1,3,4,3]
              },
             {"drinkName": "CustomDrink3",
              "drinkID": 3,
              "drinkList": ["Juice","Tea","Coffee","Cider","Sodar","Water"],
              "timesPressed": [1,2,1,3,4,3]
              },
             {"drinkName": "CustomDrink4",
              "drinkID": 4,
              "drinkList": ["Juice","Tea","Coffee","Cider","Sodar","Water"],
              "timesPressed": [1,2,1,3,4,3]
              },
             {"drinkName": "CustomDrink5",
              "drinkID": 5,
              "drinkList": ["Juice","Tea","Coffee","Cider","Sodar","Water"],
              "timesPressed": [1,2,1,3,4,3]
              },
             {"drinkName": "CustomDrink6",
              "drinkID": 6,
              "drinkList": ["Juice","Tea","Coffee","Cider","Sodar","Water"],
              "timesPressed": [1,2,1,3,4,3]
              },]

class dispenseDrink:
    def __init__(self):
        self.arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
        time.sleep(1)
        self.drinkQue = myQueue.queue()
    
    def queueD(self, drinkDataInput):
        for i in range(len(drinkDataInput["drinkList"])):
            self.drinkQue.enqueue([drinkDataInput["drinkList"][i], drinkDataInput["timesPressed"][i]])
    
    def dispense(self):
        #data = None
        #self.arduino.write(self.drinkQue.dequeue())
        a = "hello"
        self.arduino.write(bytes(a, 'utf-8'))
        time.sleep(0.05)
            #while data != "hello":
                #data = self.arduino.readline()
           # print(data)

# drink = dispenseDrink()
# drink.queueD(dummyData[0])

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
    
    for drink in drinks:
        for data in dummyData:
            if data["drinkName"] == drink["name"]:
                sortedDrink.append(data)
                break
    
    for val in sortedDrink:
        print(val["drinkName"])
    
sortDrink()
# while True:
#     drink.dispense()
    
