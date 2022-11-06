import tkinter as tk
import customtkinter as ctk

class DrinkFrame(tk.Frame):
    def __init__(self, parent,drink):
        super().__init__(parent)

        # # Create your widgets
        print(drink["drinkID"])
        self.canvas = tk.Canvas(self,width=500,height=118,background="#FF8787",highlightthickness=0)
        self.canvas.create_text(300, 50, text=drink["drinkName"], fill="black", font=('Helvetica 15 bold'))
        # self.canvas.create_text(10, 10, text="kill me" fill="black",anchor='e', font=('Inter 30 bold'))
        self.canvas.grid()