import random
import tkinter as tk
import customtkinter as ctk
from PIL import Image,ImageTk
from Database.DB import Database

class DrinkFrame(tk.Frame):
    def __init__(self, parent, drink, color, preview_canvas):
        super().__init__(parent)
        self.drink = drink
        # Create your widgets
        self.canvas = tk.Canvas(self,width=1000,height=118,background=color,highlightthickness=0)
        
        # Sample output
        #('CustomDrink1', 1, 55, 'Unknown', ['Juice', 'Tea', 'Coffee', 'Cider', 'Sodar', 'Water'], [1, 2, 1, 3, 4, 3])
        
        #Name
        self.canvas.create_text(25, 60, text=drink[0], fill="white", font=('Helvetica 30 bold'),anchor="w")
        
        #Price
        self.canvas.create_text(780, 30, text=("THB " + str(drink[2])), fill="white", font=('Helvetica 20 bold'),anchor="e")
        
        #Buy Btn
        self.button = ctk.CTkButton(self.canvas,text="Order",bg="#058ED9",width=30,command=self.order).place(x=720,y=80)
        
        #Fav btn
        self.icon = ImageTk.PhotoImage(Image.open("src\\PythonTkinter\\assets\\heart.png").resize((20,20),Image.ANTIALIAS))
        button=  ctk.CTkButton(self.canvas, image=self.icon,width=5,height=5,text="",command= lambda: self.favorite(self.drink[1],2),
        borderwidth=0,fg_color = color, hover_color = color)
        button.place(x=680,y=82)
        
        #Fav Text
        self.canvas.create_text(675, 92, text="Favorite", fill="white", font=('Helvetica 15'),anchor="e")

        #preview button
        previewBtn = ctk.CTkButton(self.canvas,
                            width=200,
                            height=50,
                            text="Preview",
                            text_font=("Inter",20),
                            text_color="black",
                            corner_radius=30,
                            hover_color=("#ACACAC"),
                            fg_color="#E5E5E5",
                            command=lambda: self.preview(preview_canvas))
        previewBtn.place(x=800,y=34)

        #Pack Canvas
        self.canvas.grid()
        
    def preview(self, preview_canvas):
        preview_canvas.delete('all')
        y = 20
        for i in self.drink[4]:
            preview_canvas.create_text(10, y, text=i + str(random.randint(0, 20)), fill="black", font=('Helvetica 30'),anchor="w")
            y += 70
        y = 20
        for j in self.drink[5]:
            preview_canvas.create_text(300, y, text=j, fill="black", font=('Helvetica 30'),anchor="w")
            y += 70
        
    
    def order(self):
        print("Order for drink", self.drink[1]) 
        
    def favorite(self,userID,drinkID):
        db = Database()
        db.addFavorite(userID,drinkID)
        print("I like that shit")


class PumpFrame(tk.Frame):
    def __init__(self, parent, drink, color):
        super().__init__(parent)
        self.drink = drink
        # Create your widgets
        self.canvas = tk.Canvas(self,width=1000,height=118,background=color,highlightthickness=0)
        
        # Sample output
        #('CustomDrink1', 1, 55, 'Unknown', ['Juice', 'Tea', 'Coffee', 'Cider', 'Sodar', 'Water'], [1, 2, 1, 3, 4, 3])
        
        #Name
        self.canvas.create_text(25, 60, text=drink[0], fill="white", font=('Helvetica 30 bold'),anchor="w")
        
        #Price
        self.canvas.create_text(780, 30, text=("Remaining: " + str(drink[1])), fill="white", font=('Helvetica 20 bold'),anchor="e")
        
        #incrase btn
        self.icon = ImageTk.PhotoImage(Image.open("src\\PythonTkinter\\assets\\increase_btn.png").resize((51,56),Image.ANTIALIAS))
        button=  ctk.CTkButton(self.canvas, image=self.icon,width=5,height=5,text="",command=lambda: self.increase(),
        borderwidth=0,fg_color = color, hover_color = color)
        button.place(x=730,y=50)

        #incrase btn
        self.icon = ImageTk.PhotoImage(Image.open("src\\PythonTkinter\\assets\\decrease_btn.png").resize((50,63),Image.ANTIALIAS))
        button=  ctk.CTkButton(self.canvas, image=self.icon,width=5,height=5,text="",command=lambda: self.decrease(),
        borderwidth=0,fg_color = color, hover_color = color)
        button.place(x=580,y=46)

        #Pack Canvas
        self.canvas.grid()
    
    def order(self):
        print("Order for drink", self.drink[1]) 
        
    def increase(self):
        print("press")
        db = Database()
        #db.addFavorite(userID,drinkID)

    def decrease(self):
        print("press")
        db = Database()
        #db.addFavorite(userID,drinkID)
    