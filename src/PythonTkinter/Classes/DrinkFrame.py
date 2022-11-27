import random, os
import tkinter as tk
import customtkinter as ctk
from PIL import Image,ImageTk
from Database.DB import Database

CURRENT_PATH = os.getcwd()
ASSETS_PATH = os.path.join(CURRENT_PATH, "src", "PythonTkinter", "assets")
class DrinkFrame(tk.Frame):
    def __init__(self, parent, drink, color, preview_canvas, fav):
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
        self.button = ctk.CTkButton(self.canvas,text="UwU Time!",fg_color="red",width=50,height=40, text_font=('Helvetica 15 bold'), command=lambda : self.order).place(x=680,y=60)
        
        #Fav btn
        if fav == False:
            self.icon = ImageTk.PhotoImage(Image.open(os.path.join(ASSETS_PATH, "FavHeartInactive.png")).resize((20,20),Image.ANTIALIAS))
            button=  ctk.CTkButton(self.canvas, image=self.icon,width=5,height=5,text="",command= lambda: self.favorite_add(self.drink[1],2),
            borderwidth=0,fg_color = color, hover_color = color)
            button.place(x=640,y=70)
        else:
            self.icon = ImageTk.PhotoImage(Image.open(os.path.join(ASSETS_PATH, "FavHeartActive.png")).resize((20,20),Image.ANTIALIAS))
            button=  ctk.CTkButton(self.canvas, image=self.icon,width=5,height=5,text="",command= lambda: self.favorite_remove(self.drink[1],2, self.canvas),
            borderwidth=0,fg_color = color, hover_color = color)
            button.place(x=640,y=70)
        
        #Fav Text
        self.canvas.create_text(630, 80, text="Favorite", fill="white", font=('Helvetica 15'),anchor="e")

        #preview button
        previewBtn = ctk.CTkButton(self.canvas,
                            width=210,
                            height=118,
                            text="Preview",
                            text_font=("Inter",20),
                            text_color="black",
                            corner_radius=30,
                            hover_color=("#ACACAC"),
                            fg_color="#E5E5E5",
                            command=lambda: self.preview(preview_canvas))
        previewBtn.place(x=820,y=0)

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
        
    def favorite_add(self,userID,drinkID):
        db = Database()
        db.addFavorite(userID,drinkID)
        print("I like that shit")

    def favorite_remove(self, userID, drinkID, canvas):
        print("I don't like that")

class PumpFrame(tk.Frame):
    def __init__(self, parent, drink, color,mainCanvas,text):
        super().__init__(parent)
        self.drink = drink
        self.amount_remaining = self.drink[1]
        self.amount_need = 0
        self.total = 0
        self.mainCanvas = mainCanvas
        self.amountText = text
        # Create your widgets
        self.canvas = tk.Canvas(self,width=1150,height=118,background=color,highlightthickness=0)
        
        # Sample output
        #('coffee', 10, 1)
        
        #Name
        self.canvas.create_text(25, 60, text=drink[0], fill="black", font=('Helvetica 40 bold'),anchor="w")
        
        #Remaining
        self.remaining = self.canvas.create_text(1080, 30, text=("Remaining: " + str(self.amount_remaining)), fill="black", font=('Helvetica 20 bold'),anchor="e")
        #amount need
        self.need = self.canvas.create_text(990, 80, text=(str(self.amount_need)), fill="black", font=('Helvetica 30 bold'),anchor="e")
        
        #incrase btn
        self.icon = ImageTk.PhotoImage(Image.open(os.path.join(ASSETS_PATH, "increase_btn.png")).resize((51,56),Image.ANTIALIAS))
        button=  ctk.CTkButton(self.canvas, image=self.icon,width=5,height=5,text="",command=lambda: self.increase(),
        borderwidth=0,fg_color = color, hover_color = color)
        button.place(x=1030,y=50)

        #incrase btn
        self.icon = ImageTk.PhotoImage(Image.open(os.path.join(ASSETS_PATH, "decrease_btn.png")).resize((50,63),Image.ANTIALIAS))
        button=  ctk.CTkButton(self.canvas, image=self.icon,width=5,height=5,text="",command=lambda: self.decrease(),
        borderwidth=0,fg_color = color, hover_color = color)
        button.place(x=880,y=46)

        #Pack Canvas
        self.canvas.grid()
    
    def order(self):
        print("Order for drink", self.drink[1]) 
        
    def increase(self):
        if self.total < 10 and self.remaining > 0:
            self.amount_need += 1
            self.total += 1
            self.amount_remaining -= 1
            self.canvas.itemconfig(self.need, text = str(self.amount_need))
            self.canvas.itemconfig(self.remaining, text = "Remaining: " + str(self.amount_remaining), fill = "black")

            txt = self.mainCanvas.itemcget(self.amountText,'text')
            print(txt)
            self.mainCanvas.itemconfig(self.amountText, text=self.total)
        elif self.amount_remaining <= 0:
            self.amount_remaining = 0
            self.canvas.itemconfig(self.remaining, text = "Remaining: " + str(self.amount_remaining), fill = "red")

    def decrease(self):
        if self.total > 0 and self.remaining < self.drink[1]:
            self.amount_need -= 1
            self.total -= 1
            self.amount_remaining += 1
            self.canvas.itemconfig(self.need, text = str(self.amount_need))
            self.canvas.itemconfig(self.remaining, text = "Remaining: " + str(self.amount_remaining), fill = "black")
        elif self.amount_remaining > self.drink[1]:
            self.amount_remaining = self.drink[1]
            self.canvas.itemconfig(self.remaining, text = "Remaining: " + str(self.amount_remaining), fill = "black")

    def get_total(self):
        return self.total

class DrinkSetting(tk.Frame):
    def __init__(self, parent, drink, color):
        super().__init__(parent)
        self.drink = drink
        # Create your widgets
        self.canvas = tk.Canvas(self,width=1150,height=118,background=color,highlightthickness=0)
        
        # Sample output
        #('coffee', 10, 1)

        #Name
        self.canvas.create_text(25, 60, text=drink[0], fill="white", font=('Helvetica 40 bold'),anchor="w")
        
        #Pump index Btn 1-6
        x = 530
        for i in range (6):
            self.button = ctk.CTkButton(self.canvas, width=70, height=50, text=i + 1, text_color="black",text_font=("Inter",15), fg_color="white",command=lambda: self.order()).place(x=x,y=45)
            x += 100
        
        #Fav Text
        self.canvas.create_text(880, 20, text="Times left: " + str(drink[1]), fill="white", font=('Helvetica 15'),anchor="e")

        #Pack Canvas
        self.canvas.grid()       
    
    def order(self):
        print("Order for drink", self.drink[1]) 
        
    def favorite_add(self,userID,drinkID):
        db = Database()
        db.addFavorite(userID,drinkID)
        print("I like that shit")

    def favorite_remove(self, userID, drinkID, canvas):
        print("I don't like that")
    