import os,json

class Leaderboard:
    def __init__(self):
        self.saveFilePath = os.path.join(os.getcwd(),'src','PythonGame','gameData.json')
        self.users = ""
        self.getUser()
    
    def getUser(self):
        try:
            data = json.load(open(self.saveFilePath))
            self.users = data
        except:
            pass
    
    def saveScore(self,newData):
        try:
            #Append to at the end
            data = json.load(open(self.saveFilePath))
            
            if type(data) is dict:
                data = [data]
    
            data.append({
                "name": newData["name"],
                "score": newData["score"]
            })
            
            with open(self.saveFilePath, 'w') as outfile:
                json.dump(data, outfile, indent=4)
            
        except Exception as e:
            #When file data is not found
            json_object = json.dumps(newData, indent=2)
            with open(self.saveFilePath, "w") as outfile:
                outfile.write(json_object)

    def getSortedScoreboard(self):
        tempArr = []
        sortedArrDict = []
        for data in self.users:
            tempArr.append(data["score"])
        sortedArr = self.quickSort(tempArr)
        for item in self.users:
            for val in sortedArr:
                if val == item["score"]:
                    sortedArrDict.append({
                        "name" : item["name"],
                        "score": item["score"]
                    })
                    sortedArr.remove(val)
                    
        return sortedArrDict
    
    def quickSort(self,array):
        """Sort the array by using quicksort."""
        less = []
        equal = []
        greater = []

        if len(array) > 1:
            pivot = array[0]
            for x in array:
                if x < pivot:
                    less.append(x)
                elif x == pivot:
                    equal.append(x)
                elif x > pivot:
                    greater.append(x)
            return self.quickSort(less) + equal + self.quickSort(greater)
        else:
            return array
        

            