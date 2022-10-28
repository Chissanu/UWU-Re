import myQueue
#from wsgiref.types import InputStream

dummyData = [{"drinkName": "CustomDrink1",
              "drinkID": 1,
              "drinkList": ["Juice","Tea","Coffee","Cider","Sodar","Water"],
              "drinkOrder": [20,123,12,45,23,44]
              },
             {"drinkName": "CustomDrink2",
              "drinkID": 2,
              "drinkList": ["Juice","Tea","Coffee","Cider","Sodar","Water"],
              "drinkOrder": [20,123,12,45,23,44]
              },
             {"drinkName": "CustomDrink3",
              "drinkID": 3,
              "drinkList": ["Juice","Tea","Coffee","Cider","Sodar","Water"],
              "drinkOrder": [20,123,12,45,23,44]
              },
             {"drinkName": "CustomDrink4",
              "drinkID": 4,
              "drinkList": ["Juice","Tea","Coffee","Cider","Sodar","Water"],
              "drinkOrder": [20,123,12,45,23,44]
              },
             {"drinkName": "CustomDrink5",
              "drinkID": 5,
              "drinkList": ["Juice","Tea","Coffee","Cider","Sodar","Water"],
              "drinkOrder": [20,123,12,45,23,44]
              },
             {"drinkName": "CustomDrink6",
              "drinkID": 6,
              "drinkList": ["Juice","Tea","Coffee","Cider","Sodar","Water"],
              "drinkOrder": [20,123,12,45,23,44]
              },]
              
drinkQue = myQueue.queue()
drinkDataInput = dummyData[0]
for i in drinkDataInput["drinkOrder"]:
    drinkQue.enqueue(i)

print(drinkQue.get_data())
    
