import psycopg2

command = """ INSERT INTO drink_tables(drinkName,price,ingredientList,timespressed) VALUES(%s,%s,%s,%s) """
#establishing the connection
con = psycopg2.connect(
   database="uwure",
   user='admin',
   password='uwure',
   host='127.0.0.1',   
   port= '5432'
)
def genDrink():
    cur = con.cursor()
    for i in range(5):
        cur.execute(command,(f"CustomDrink{i+1}",55,["Juice","Tea","Coffee","Cider","Sodar","Water"],[1,2,1,3,4,3]))
        con.commit()
    con.close()
    
    
def genUser():
    cur = con.cursor()
    for i in range(5):
        val = (f"TestUser{i+1}","somepass",500)
        sql = "INSERT INTO users(username,userpass,usercoins) VALUES(%s,%s,%s)"
        cur.execute(sql,val)
        con.commit()
    con.close()
    
def genIngredients():
    cur = con.cursor()
    ingredientList = ["coffee","juice","tea","cider","sodar","water","vodka","beer"]
    for i in range(6):
        val = (ingredientList[i],10,i + 1)
        sql = "INSERT INTO pump_list(name,leftovers,pumpID) VALUES(%s,%s,%s)"
        cur.execute(sql,val)
        con.commit()
    for i in range(2):
        val = (ingredientList[i+6],10)
        sql = "INSERT INTO pump_list(name,leftovers) VALUES(%s,%s)"
        cur.execute(sql,val)
        con.commit()
    con.close()
#genUser()
genDrink()
#genIngredients()