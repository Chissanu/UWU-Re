import myQueue
import serial
import time
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

drink = dispenseDrink()
drink.queueD(dummyData[0])
while True:
    drink.dispense()
    
