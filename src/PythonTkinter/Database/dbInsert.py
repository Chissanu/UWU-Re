import psycopg2

command = """ INSERT INTO drink_tables(drinkName,ingredientList,drinkList) VALUES(%s,%s,%s) """
#establishing the connection
con = psycopg2.connect(
   database="uwure",
   user='admin',
   password='uwure',
   host='127.0.0.1',   
   port= '5432'
)

def insertDrink(val):
   #Creating a cursor object using the cursor() method
   cur = con.cursor()
   
   cur.execute(command, val)
   #Commit to database
   con.commit()
   #Close connection
   con.close()
   
def getDrink():
   cur = con.cursor()
   name = input("What drink are you looking for? >")
   sql = "SELECT * FROM drink_tables where drinkName like '{drinkName}'".format(drinkName = name)
   cur.execute(sql)
   data = cur.fetchall()
   if not data:
      print("Could not find drink with that name")
   else:
      print(data)
   
def containDrink():
   cur = con.cursor()
   name = input("What ingredient are you looking for? >")
   sql = "select * from drink_tables where '{ingrName}'=any(ingredientlist);".format(ingrName = name)
   cur.execute(sql)
   data = cur.fetchall()
   if not data:
      print("Could not find drink with that name")
   else:
      print(data)

def main():
   ingredientList = []
   drinkList = []
   drinkName = input("What's the drink name? > ")
   for i in range(6):
      text = "How much ML for Drink {drinkNum}: >".format(drinkNum = i+1)
      ml = int(input(text))
      name = input("What's the ingredient name? >")
      ingredientList.append(name)
      drinkList.append(ml)
      
   val = (drinkName,ingredientList,drinkList)
   insertDrink(val)
   print(drinkList)
   
#main()
containDrink()
#getDrink()
