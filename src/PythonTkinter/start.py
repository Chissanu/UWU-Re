import psycopg2
from Main import App

con = psycopg2.connect(
   database="uwure",
   user='admin',
   password='uwure',
   host='127.0.0.1',   
   port= '5432'
)

    
def main():
    #Log in screen
    app = App("Chissanu",1000)
    app.mainloop()
    
main()