import psycopg2

command = """ INSERT INTO drink_tables(drinkName,ingredientList,timepressed) VALUES(%s,%s,%s) """
#establishing the connection
con = psycopg2.connect(
   database="uwure",
   user='admin',
   password='uwure',
   host='127.0.0.1',   
   port= '5432'
)
con.set_session(autocommit=True)
class Database:
   def __init__(self):
      self.con = con
      
   def insertDrink(self,val):
      #Creating a cursor object using the cursor() method
      cur = con.cursor()
      
      cur.execute(command, val)
      #Commit to database
      con.commit()
      #Close connection
      con.close()
      
   def queryDrinkDB(self):
      cur = con.cursor()
      sql = "SELECT * FROM drink_tables;"
      cur.execute(sql)
      data = cur.fetchall()
      return data
      
   def getDrink(self,name):
      cur = con.cursor()
      sql = "SELECT * FROM drink_tables where drinkName like '{drinkName}'".format(drinkName = name)
      cur.execute(sql)
      data = cur.fetchall()
      if not data:
         print("Could not find drink with that name")
      else:
         return(data)
      
   def containIngredients(self,name):
      cur = con.cursor()
      sql = "select * from drink_tables where '{ingrName}'=any(ingredientlist);".format(ingrName = name)
      cur.execute(sql)
      data = cur.fetchall()
      if not data:
         print("Could not find drink with that name")
      else:
         print(data)
         
   def addFavorite(self,newDrinkID):
      cur = con.cursor()
      sql = "SELECT favdrinkid from users where userid = 1"
      cur.execute(sql)
      userDatas = list(cur.fetchall()[0])
      if userDatas[0] == None:
         userDatas.pop(0)
         userDatas.append(newDrinkID)
         
      print(userDatas)
      #con.commit()
      con.close()

db = Database()
db.addFavorite(5)
# def main():
#    ingredientList = []
#    drinkList = []
#    drinkName = input("What's the drink name? > ")
#    for i in range(6):
#       text = "How much ML for Drink {drinkNum}: >".format(drinkNum = i+1)
#       ml = int(input(text))
#       name = input("What's the ingredient name? >")
#       ingredientList.append(name)
#       drinkList.append(ml)
   
#    val = (drinkName,ingredientList,drinkList)
#    self.insertDrink(val)
#    print(drinkList)
   
