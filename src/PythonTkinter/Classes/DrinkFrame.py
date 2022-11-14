import tkinter as tk
import customtkinter as ctk
from PIL import Image,ImageTk
from Database.DB import Database

class DrinkFrame(tk.Frame):
    def __init__(self, parent,drink):
        super().__init__(parent)
        self.drink = drink
        # Create your widgets
        self.canvas = tk.Canvas(self,width=800,height=118,background="#FF8787",highlightthickness=0)
        
        #Name
        self.canvas.create_text(25, 60, text=drink["drinkName"], fill="white", font=('Helvetica 30 bold'),anchor="w")
        
        #Price
        self.canvas.create_text(780, 30, text=("THB " + str(drink["price"])), fill="white", font=('Helvetica 20 bold'),anchor="e")
        
        #Buy Btn
        self.button = ctk.CTkButton(self.canvas,text="Order",bg="#058ED9",width=30,command=self.order).place(x=720,y=80)
        
        #Fav btn
        self.icon = ImageTk.PhotoImage(Image.open("src\\PythonTkinter\\assets\\heart.png").resize((20,20),Image.ANTIALIAS))
        button=  ctk.CTkButton(self.canvas, image=self.icon,width=5,height=5,text="",command= self.favorite,
        borderwidth=0,fg_color="#FF8787",hover_color="#FF8787")
        button.place(x=680,y=82)
        
        #Fav Text
        self.canvas.create_text(675, 92, text="Favorite", fill="white", font=('Helvetica 15'),anchor="e")
        
        
        #Pack Canvas
        self.canvas.grid()
        
    def order(self):
        print("Order for drink", self.drink["drinkID"]) 
        
    def favorite(self):
        db = Database()
        print(db.queryDrinkDB())
        print("I like that shit")
    