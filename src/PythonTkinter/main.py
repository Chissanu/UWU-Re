import tkinter as tk
import customtkinter as ctk
import os
import random
import json
from pathlib import Path
from PIL import ImageTk, Image
from Classes.DrinkFrame import DrinkFrame, PumpFrame, DrinkSetting
from Database.DB import Database
from tkinter_dispenser import TkinterDispenser
from dispense_drink import DispenseDrink

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

#Path list
#C:\Users\@USER\Documents\UWU-Re
MAIN_DIR = str(os.path.normpath(os.getcwd() + os.sep))


#Color Pallete
BLUE_BG = "#859FFD"
ALL_BG = "#FFF89A"
FAV_BG = "#FFB2A6"
RAND_BG = "#9ADCFF"
CREATE_BG = "#80D2FF"
YELLOW = "#FDFD96"

db = Database()
pumpData = list(db.getPumpList())
browseData = list(db.queryDrinkDB())
favData = list(db.getFavData(2))

class App(ctk.CTk):
    # def __init__(self,name,coin):
    def __init__(self):
        super().__init__()
        WIDTH = 1920
        HEIGHT = 1080
        global profile
        profile = []
        self.title("UWU:Reborn from Ashes")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.bind('<Escape>',lambda e: quit(e))
        self.config(bg="#6482EB")
        self.attributes('-fullscreen',True)
        CURRENT_PATH = os.getcwd()
        self.profileIconPath = os.path.join(CURRENT_PATH, "src", "PythonTkinter", "assets", "profilePic.png")
        ASSETS_PATH = os.path.join(CURRENT_PATH, "src", "PythonTkinter", "assets")
        self.home_icon = ImageTk.PhotoImage(Image.open(os.path.join(ASSETS_PATH, "Home_Btn.png")).resize((70,63)))
        # self.profileName = name
        # self.coin = coin
        self.profileName = "Chissanu"
        self.coin = "Coins:" + str(1000)
        self.drinkList = {}
        self.drink_arr = ()
        # #random recipe starting list
        # random_recipe = db.getRandomRecipe()

        """
        ======================================
                    Log in FRAME
        ======================================
        """
        # #Frame & Canvas Creation
        # self.loginFrame = ctk.CTkFrame(self,width=WIDTH,height=HEIGHT,fg_color=BLUE_BG)
        # self.loginCanvas = ctk.CTkCanvas(self.loginFrame,width=WIDTH,height=HEIGHT,bg=BLUE_BG,highlightthickness=0)
        
        # # Create Logo
        # nameLabel1 = ctk.CTkLabel(self.loginCanvas,text="UwU:",text_font=("Inter",80),text_color="white")
        # nameLabel1.place(x=750,y=50)
        # nameLabel2 = ctk.CTkLabel(self.loginCanvas,text="Re",text_font=("Inter",80),text_color="black")
        # nameLabel2.place(x=1015,y=50)
        # line = self.loginCanvas.create_line(750,180,1160,180, fill="white", width=10) 
        
        # #Create profile icon
        # img = ImageTk.PhotoImage(Image.open(self.profileIconPath).resize((300,300)))
        # profile.append(img)
        # self.loginCanvas.create_image(800,220,anchor=tk.NW,image=img)
        
        # #Buttons
        # signinBtn = ctk.CTkButton(self.loginFrame,
        #                             width=500,
        #                             height=140,
        #                             text="Start",
        #                             text_font=("Inter",50, 'bold'),
        #                             text_color="white",
        #                             corner_radius=30,
        #                             hover_color=("#4166EA"),
        #                             fg_color="#0938DC",
        #                             command=lambda :self.change_frame(self.mainFrame,"browse"))
        # signinBtn.place(x=580,y=600)
        
        
        
        # #Pack Frame & Canvas
        # self.loginCanvas.pack(fill="both", expand=1)
        # self.loginFrame.pack(fill="both", expand=1)
        
        """
        ======================================
                    SELECT FRAME
        ======================================
        """
        #Frame & Canvas creation
        self.mainFrame = ctk.CTkFrame(self,width=WIDTH,height=HEIGHT,fg_color=BLUE_BG)
        self.mainCanvas = ctk.CTkCanvas(self.mainFrame,width=WIDTH,height=HEIGHT,bg=BLUE_BG,highlightthickness=0)
        
        #Logo Label
        self.nameLabel1 = ctk.CTkLabel(self.mainCanvas,text="UwU:",text_font=("Inter",180),text_color="white")
        self.nameLabel1.place(x=500,y=200)
        self.nameLabel2 = ctk.CTkLabel(self.mainCanvas,text="Re",text_font=("Inter",180),text_color="black")
        self.nameLabel2.place(x=1080,y=200)
        self.nameLine = self.mainCanvas.create_line(500,500,1400,500, fill="white", width=10)
        
        #Buttons
        # self.button(150, 700, "Browse", self.mainCanvas, self.mainFrame, "browse", "#4BD960", 450, 150)
        # self.button(750, 700, "Create", self.mainCanvas, self.mainFrame, "create", "#A1D94B", 450, 150)
        # self.button(1350, 700, "Setting", self.mainCanvas, self.mainFrame, "setting", "#525252", 450, 150)
        browseBtn = ctk.CTkButton(self.mainCanvas,
                            width=450,
                            height=150,
                            text="Browse",
                            text_font=("Inter",50, "bold"),
                            text_color="black",
                            corner_radius=30,
                            hover_color= "#4BD960",
                            fg_color="#4BD960",
                            command=lambda :self.change_frame(self.mainFrame, "browse"))
        browseBtn.place(x=150,y=700)

        createBtn = ctk.CTkButton(self.mainCanvas,
                            width=450,
                            height=150,
                            text="Create",
                            text_font=("Inter",50, "bold"),
                            text_color="black",
                            corner_radius=30,
                            hover_color= "#A1D94B",
                            fg_color="#A1D94B",
                            command=lambda :self.change_frame(self.mainFrame, "create"))
        createBtn.place(x=750,y=700)  

        browseBtn = ctk.CTkButton(self.mainCanvas,
                            width=450,
                            height=150,
                            text="Setting",
                            text_font=("Inter",50, "bold"),
                            text_color="black",
                            corner_radius=30,
                            hover_color= "#939799",
                            fg_color="#939799",
                            command=lambda :self.change_frame(self.mainFrame, "setting"))
        browseBtn.place(x=1350,y=700)
        
        #Pack Frame & Canvas
        self.mainCanvas.pack(fill="both", expand=1)
        self.mainFrame.pack(fill="both", expand=1)
              
        """
        ======================================
                    All FRAME
        ======================================
        """
        #Frame Creation
        self.browseFrame = ctk.CTkFrame(self,width=WIDTH,height=HEIGHT,fg_color=BLUE_BG,corner_radius=0)
        self.browseCanvas = ctk.CTkCanvas(self.browseFrame,width=WIDTH,height=HEIGHT,bg=BLUE_BG,highlightthickness=0)
        
        #Profile
        img = ImageTk.PhotoImage(Image.open(self.profileIconPath).resize((110,110)))
        profile.append(img)
        self.browseCanvas.create_image(1790,20,anchor=tk.NW,image=img)
        self.browseCanvas.create_text(1750, 50, text=self.profileName, fill="black",anchor='e', font=('Inter 30 bold'))
        self.browseCanvas.create_text(1750, 100, text=self.coin, fill="black",anchor='e', font=('Inter 30 bold'))

        #ingredient list Frame
        self.browseIngredientFrame = ctk.CTkFrame(self.browseCanvas,width=450,height=750,fg_color="white",highlightthickness=0)
        self.browseIngredientFrame.place(x=1400,y=200)

        #label ingredient
        ingredientLab = ctk.CTkLabel(self.browseIngredientFrame,text="Ingredient",text_font=("Inter",40, "bold"),text_color="black")
        ingredientLab.place(x=10,y=30)

        #ingredient list Canvas
        self.browseIngredientCanvas = ctk.CTkCanvas(self.browseIngredientFrame,width=350,height=900,bg="white",highlightthickness=0)
        self.browseIngredientCanvas.place(x=0,y=150)
        
        #Item List Frame
        self.browseItemFrame = ctk.CTkFrame(self.browseCanvas,width=1250,height=900,fg_color=ALL_BG,highlightthickness=0)
        self.browseItemFrame.place(x=50,y=80)
        
        #Item List Canvas
        self.browseItemCanvas = ctk.CTkCanvas(self.browseItemFrame,width=1250,height=750,bg=ALL_BG,highlightthickness=0)
        self.browseItemCanvas.place(x=0,y=150)
        
        #Item list Scrollbar
        browse_scrollbar = tk.Scrollbar(self.browseItemFrame, orient=tk.VERTICAL, command=self.browseItemCanvas.yview)
        browse_scrollbar.place(x=1232,y=150,height=750)

        #Configure Canvas to scroll with mouse wheel
        self.browseItemCanvas.configure(yscrollcommand=browse_scrollbar.set)
        self.browseItemCanvas.bind('<Configure>', lambda e: self.browseItemCanvas.configure(scrollregion = self.browseItemCanvas.bbox("all")))
        
        #Pack item frame inside canvas
        second_frame_browse = tk.Frame(self.browseItemCanvas,bg=ALL_BG,width=1250,height=900,highlightthickness=0)
        second_frame_browse.place(x=0,y=0)

        self.browseItemCanvas.create_window((0,0), window=second_frame_browse, anchor="nw")

        #button
        self.button(400, 20, "Favorite", self.browseItemFrame, self.browseFrame, "favorite",  FAV_BG, 200, 80)
        self.button(800, 20, "Random", self.browseItemFrame, self.browseFrame, "random", RAND_BG, 200, 80)
        home_button =  ctk.CTkButton(self.browseCanvas, image=self.home_icon,width=5,height=5,text="",command=lambda :self.change_frame(self.browseFrame, "main"),
        borderwidth=0,fg_color = BLUE_BG, hover_color = BLUE_BG)
        home_button.place(x=1750,y=970)
        
        
        x = 30
        y = 20
        altura = 0
        self.browse_list = []
        for drink in browseData:
            altura = altura + 150
            browse_drink_frame = DrinkFrame(second_frame_browse,drink, "#FF8787", self.browseIngredientCanvas, False)
            self.browse_list.append(browse_drink_frame)
            browse_drink_frame.place(x=x,y=y)
            y += 150
        second_frame_browse.configure(height=altura)
        
        #Frame Label
        allLab = ctk.CTkLabel(self.browseItemFrame,text="All",text_font=("Inter",40, "bold"),text_color="black")
        allLab.place(x=100,y=30)

        """
        ======================================
                    Favorite Frame
        ======================================
        """
        #Frame Creation
        self.favoriteFrame = ctk.CTkFrame(self,width=WIDTH,height=HEIGHT,fg_color=BLUE_BG,corner_radius=0)
        self.favoriteCanvas = ctk.CTkCanvas(self.favoriteFrame,width=WIDTH,height=HEIGHT,bg=BLUE_BG,highlightthickness=0)
        
        #Profile
        img = ImageTk.PhotoImage(Image.open(self.profileIconPath).resize((110,110)))
        profile.append(img)
        self.favoriteCanvas.create_image(1790,20,anchor=tk.NW,image=img)
        self.favoriteCanvas.create_text(1750, 50, text=self.profileName, fill="black",anchor='e', font=('Inter 30 bold'))
        self.favoriteCanvas.create_text(1750, 100, text=self.coin, fill="black",anchor='e', font=('Inter 30 bold'))

        #ingredient list Frame
        self.favoriteIngredientFrame = ctk.CTkFrame(self.favoriteCanvas,width=450,height=750,fg_color="white",highlightthickness=0)
        self.favoriteIngredientFrame.place(x=1400,y=200)

        #label ingredient
        ingredientLab = ctk.CTkLabel(self.favoriteIngredientFrame,text="Ingredient",text_font=("Inter",40, "bold"),text_color="black")
        ingredientLab.place(x=10,y=30)

        #ingredient list Canvas
        self.favoriteIngredientCanvas = ctk.CTkCanvas(self.favoriteIngredientFrame,width=350,height=900,bg="white",highlightthickness=0)
        self.favoriteIngredientCanvas.place(x=0,y=150)
        
        
        #Item List Frame
        self.favoriteItemFrame = ctk.CTkFrame(self.favoriteCanvas,width=1250,height=900,fg_color=FAV_BG,highlightthickness=0)
        self.favoriteItemFrame.place(x=50,y=80)
        
        #Item List Canvas
        self.favoriteItemCanvas = ctk.CTkCanvas(self.favoriteItemFrame,width=1250,height=750,bg=FAV_BG,highlightthickness=0)
        self.favoriteItemCanvas.place(x=0,y=150)
        
        #Item list Scrollbar
        favorite_scrollbar = tk.Scrollbar(self.favoriteItemFrame, orient=tk.VERTICAL, command=self.favoriteItemCanvas.yview)
        favorite_scrollbar.place(x=1232,y=150,height=750)

        #Configure Canvas to scroll with mouse wheel
        self.favoriteItemCanvas.configure(yscrollcommand=favorite_scrollbar.set)
        self.favoriteItemCanvas.bind('<Configure>', lambda e: self.favoriteItemCanvas.configure(scrollregion = self.favoriteItemCanvas.bbox("all")))
        
        #Pack item frame inside canvas
        second_frame_favorite = tk.Frame(self.favoriteItemCanvas,bg=FAV_BG,width=1250,height=900,highlightthickness=0)
        second_frame_favorite.place(x=0,y=0)

        self.favoriteItemCanvas.create_window((0,0), window=second_frame_favorite, anchor="nw")

        #button
        self.button(70, 20, "All", self.favoriteItemFrame, self.favoriteFrame, "browse", ALL_BG, 200, 80)
        self.button(800, 20, "Random", self.favoriteItemFrame, self.favoriteFrame, "random", RAND_BG, 200, 80)
        home_button =  ctk.CTkButton(self.favoriteCanvas, image=self.home_icon,width=5,height=5,text="",command=lambda :self.change_frame(self.favoriteFrame, "main"),
        borderwidth=0,fg_color = BLUE_BG, hover_color = BLUE_BG)
        home_button.place(x=1750,y=970)
        
        
        x = 30
        y = 20
        altura = 0
        self.favorite_list = []
        for drink in favData:
            altura = altura + 150
            fav_drink_frame = DrinkFrame(second_frame_favorite,drink, "#554994", self.favoriteIngredientCanvas, True)
            self.favorite_list.append(fav_drink_frame)
            fav_drink_frame.place(x=x,y=y)
            y += 150
        second_frame_favorite.configure(height=altura)
        
        #Frame Label
        favoriteLab = ctk.CTkLabel(self.favoriteItemFrame,text="Favorite",text_font=("Inter",40, "bold"),text_color="black")
        favoriteLab.place(x=430,y=30)

        """
        ======================================
                    Random Frame
        ======================================
        """
        #Frame & Canvas creation
        self.randomFrame = ctk.CTkFrame(self,width=WIDTH,height=HEIGHT,fg_color=BLUE_BG)
        self.randomCanvas = ctk.CTkCanvas(self.randomFrame,width=WIDTH,height=HEIGHT,bg=BLUE_BG,highlightthickness=0)
        
        #Profile
        img = ImageTk.PhotoImage(Image.open(self.profileIconPath).resize((110,110)))
        profile.append(img)
        self.randomCanvas.create_image(1790,20,anchor=tk.NW,image=img)
        self.randomCanvas.create_text(1750, 50, text=self.profileName, fill="black",anchor='e', font=('Inter 30 bold'))
        self.randomCanvas.create_text(1750, 100, text=self.coin, fill="black",anchor='e', font=('Inter 30 bold'))

        #Choice box canvas
        self.randomChoice = ctk.CTkFrame(self.randomCanvas,width=1250,height=900,fg_color=RAND_BG,highlightthickness=0)
        self.randomChoice.place(x=50,y=80)
        
        #button
        self.button(70, 20, "All", self.randomChoice, self.randomFrame, "browse", ALL_BG, 200, 80)
        self.button(400, 20, "Favorite", self.randomChoice, self.randomFrame, "favorite", FAV_BG, 200, 80)
        
        #button to change canvas
        Recipe_btn = ctk.CTkButton(self.randomChoice,
                            width=250,
                            height=100,
                            text="Random Recipe",
                            text_font=("Inter",50),
                            text_color="white",
                            corner_radius=30,
                            hover_color=("#ACACAC"),
                            fg_color="#000000",
                            command=lambda :self.change_frame_random(self.randomFrame, "random recipe"))
        Recipe_btn.place(x=350,y=300)
        
        Drink_btn = ctk.CTkButton(self.randomChoice,
                            width=250,
                            height=100,
                            text="Random Drink",
                            text_font=("Inter",50),
                            text_color="white",
                            corner_radius=30,
                            hover_color=("#ACACAC"),
                            fg_color="#000000",
                            command=lambda :self.change_frame_random(self.randomFrame, "random drink"))
        Drink_btn.place(x=370,y=500)

        home_button =  ctk.CTkButton(self.randomCanvas, image=self.home_icon,width=5,height=5,text="",command=lambda :self.change_frame(self.randomFrame, "main"),
        borderwidth=0,fg_color = BLUE_BG, hover_color = BLUE_BG)
        home_button.place(x=1750,y=970)

        #Frame Label
        randomLab = ctk.CTkLabel(self.randomChoice,text="Random",text_font=("Inter",40, "bold"),text_color="black")
        randomLab.place(x=830,y=30)

        """
        ============== Random Recipe ==============
        """
        #Frame & Canvas creation
        self.RecipeFrame = ctk.CTkFrame(self,width=WIDTH,height=HEIGHT,fg_color=BLUE_BG)
        self.RecipeCanvas = ctk.CTkCanvas(self.RecipeFrame,width=WIDTH,height=HEIGHT,bg=BLUE_BG,highlightthickness=0)

        #Profile
        img = ImageTk.PhotoImage(Image.open(self.profileIconPath).resize((110,110)))
        profile.append(img)
        self.RecipeCanvas.create_image(1790,20,anchor=tk.NW,image=img)
        self.RecipeCanvas.create_text(1750, 50, text=self.profileName, fill="black",anchor='e', font=('Inter 30 bold'))
        self.RecipeCanvas.create_text(1750, 100, text=self.coin, fill="black",anchor='e', font=('Inter 30 bold'))

        #Random Recipe box canvas
        self.Recipe = ctk.CTkFrame(self.RecipeCanvas,width=1250,height=900,fg_color=RAND_BG,highlightthickness=0)
        self.RecipeInside = ctk.CTkCanvas(self.Recipe,width=1150,height=650,bg="white",highlightthickness=0)
        self.Recipe.place(x=50,y=80)
        self.RecipeInside.place(x=50, y=200)

        self.RecipeInside.create_text(50, 50, text = "ingredient", fill="black",anchor='w', font=('Inter 30 bold'))
        

        #button
        self.UwU_timeBtn(1400, 400, self.RecipeCanvas)
        self.button(1500, 800, "back!", self.RecipeCanvas, self.RecipeFrame, "random", "#80D2FF", 200, 80)
        Recipe_btn = ctk.CTkButton(self.RecipeCanvas,
                            width=250,
                            height=100,
                            text="Random again",
                            text_font=("Inter",50),
                            text_color="white",
                            corner_radius=30,
                            hover_color=("#ACACAC"),
                            fg_color="#000000",
                            command=lambda :self.change_frame_random(self.RecipeFrame, "random recipe"))
        Recipe_btn.place(x=1360,y=600)
        home_button =  ctk.CTkButton(self.RecipeCanvas, image=self.home_icon,width=5,height=5,text="",command=lambda :self.change_frame(self.RecipeFrame, "main"),
        borderwidth=0,fg_color = BLUE_BG, hover_color = BLUE_BG)
        home_button.place(x=1750,y=970)

        """
        ============== Random Drink ==============
        """
        #Frame & Canvas creation
        self.DrinkFrame = ctk.CTkFrame(self,width=WIDTH,height=HEIGHT,fg_color=BLUE_BG)
        self.DrinkCanvas = ctk.CTkCanvas(self.DrinkFrame,width=WIDTH,height=HEIGHT,bg=BLUE_BG,highlightthickness=0)

        #Profile
        img = ImageTk.PhotoImage(Image.open(self.profileIconPath).resize((110,110)))
        profile.append(img)
        self.DrinkCanvas.create_image(1790,20,anchor=tk.NW,image=img)
        self.DrinkCanvas.create_text(1750, 50, text=self.profileName, fill="black",anchor='e', font=('Inter 30 bold'))
        self.DrinkCanvas.create_text(1750, 100, text=self.coin, fill="black",anchor='e', font=('Inter 30 bold'))

        #Random Recipe box canvas
        self.Drink = ctk.CTkFrame(self.DrinkCanvas,width=1250,height=900,fg_color=RAND_BG,highlightthickness=0)
        self.DrinkInside = ctk.CTkCanvas(self.Drink,width=1150,height=650,bg="white",highlightthickness=0)
        self.Drink.place(x=50,y=80)
        self.DrinkInside.place(x=50, y=200)

        #button
        self.UwU_timeBtn(1400, 400, self.DrinkCanvas)
        self.button(1500, 800, "back", self.DrinkCanvas, self.DrinkFrame, "random", "#80D2FF", 200, 80)
        Drink_btn = ctk.CTkButton(self.DrinkCanvas,
                            width=250,
                            height=100,
                            text="Random again",
                            text_font=("Inter",50),
                            text_color="white",
                            corner_radius=30,
                            hover_color=("#ACACAC"),
                            fg_color="#000000",
                            command=lambda :self.change_frame_random(self.DrinkFrame, "random drink"))
        Drink_btn.place(x=1360,y=600)                    
        home_button =  ctk.CTkButton(self.DrinkCanvas, image=self.home_icon,width=5,height=5,text="",command=lambda :self.change_frame(self.DrinkFrame, "main"),
        borderwidth=0,fg_color = BLUE_BG, hover_color = BLUE_BG)
        home_button.place(x=1750,y=970)

        #Frame Label
        randomLab = ctk.CTkLabel(self.Drink,text="Random",text_font=("Inter",50,"bold"),text_color="black")
        randomLab.place(x=100,y=100)

        #draw recipe name
        randomDrinkName = ctk.CTkLabel(self.Drink,text="Random Drink",text_font=("Inter",50, "bold"),text_color="black")
        randomDrinkName.place(x=100, y=100)
        self.DrinkInside.create_text(50, 50, text = "ingredient", fill="black",anchor='w', font=('Inter 30 bold'))

        """
        ======================================
                    Create Frame
        ======================================
        """
         #Frame Creation
        self.createFrame = ctk.CTkFrame(self,width=WIDTH,height=HEIGHT,fg_color=BLUE_BG,corner_radius=0)
        self.createCanvas = ctk.CTkCanvas(self.createFrame,width=WIDTH,height=HEIGHT,bg=BLUE_BG,highlightthickness=0)
        
        #Profile
        img = ImageTk.PhotoImage(Image.open(self.profileIconPath).resize((110,110)))
        profile.append(img)
        self.createCanvas.create_image(1790,20,anchor=tk.NW,image=img)
        self.createCanvas.create_text(1750, 50, text=self.profileName, fill="black",anchor='e', font=('Inter 30 bold'))
        self.createCanvas.create_text(1750, 100, text=self.coin, fill="black",anchor='e', font=('Inter 30 bold'))

        #draw note
        noteLab = ctk.CTkLabel(self.createCanvas,text="***Note: Press 1 time = 30 mL",text_font=("Inter",30, "bold"),text_color="red")
        noteLab.place(x=50,y=980)

        #Amount of ingredient Frame
        self.createAmountFrame = ctk.CTkFrame(self.createCanvas,width=500,height=600,fg_color="white",highlightthickness=0)
        self.createAmountFrame.place(x=1370,y=300)

        #Amount of ingredient canvas
        self.createAmountCanvas= ctk.CTkCanvas(self.createAmountFrame,width=500,height=500,bg="white",highlightthickness=0)
        self.createAmountCanvas.place(x=0,y=100)

        #label ingredient
        totalLab = ctk.CTkLabel(self.createAmountFrame,text="Total",text_font=("Inter",40, "bold"),text_color="black")
        totalLab.place(x=180,y=30)
        self.createAmountCanvas.create_line(50,0,450,0, fill="black", width=5) 

        #draw total amount text
        self.createAmountCanvas.create_text(330, 100, text="/10", fill="black",anchor='e', font=('Inter 50'))
        
        #Drink List Frame
        self.createItemFrame = ctk.CTkFrame(self.createCanvas,width=1250,height=900,fg_color="white",highlightthickness=0)
        self.createItemFrame.place(x=50,y=80)

        #Drink List Canvas
        self.createItemCanvas = ctk.CTkCanvas(self.createItemFrame,width=1250,height=900,bg="white",highlightthickness=0)
        self.createItemCanvas.place(x=0,y=80)
               
        #Item list Scrollbar
        create_scrollbar = tk.Scrollbar(self.createItemFrame, orient=tk.VERTICAL, command=self.createItemCanvas.yview)
        create_scrollbar.place(x=1232,y=150,height=750)

        #Configure Canvas to scroll with mouse wheel
        self.createItemCanvas.configure(yscrollcommand=create_scrollbar.set)
        self.createItemCanvas.bind('<Configure>', lambda e: self.createItemCanvas.configure(scrollregion = self.createItemCanvas.bbox("all")))
        
        #Pack item frame inside canvas
        second_frame_create = tk.Frame(self.createItemCanvas,bg="#554994",width=1250,height=900,highlightthickness=0)
        second_frame_create.place(x=0,y=0)

        self.second_canvas = ctk.CTkCanvas(self.createItemCanvas,bg="#554994",width=1250,height=900,highlightthickness=0)
        self.second_canvas.place(x=0,y=0)

        self.createItemCanvas.create_window((0,0), window=second_frame_create, anchor="nw")

        #button
        self.UwU_timeBtn(50, 250, self.createAmountCanvas) 
        home_button =  ctk.CTkButton(self.createCanvas, image=self.home_icon,width=5,height=5,text="",command=lambda :self.change_frame(self.createFrame, "main"),
        borderwidth=0,fg_color = BLUE_BG, hover_color = BLUE_BG)
        home_button.place(x=1750,y=970)
        
        self.total_txt= self.createAmountCanvas.create_text(220, 100, text='0', fill="black",anchor='e', font=('Inter 50 bold underline'))
        self.increase_icon = ImageTk.PhotoImage(Image.open(os.path.join(ASSETS_PATH, "increase_btn.png")).resize((51,56),Image.ANTIALIAS))
        self.decrease_icon = ImageTk.PhotoImage(Image.open(os.path.join(ASSETS_PATH, "decrease_btn.png")).resize((50,63),Image.ANTIALIAS))
        x = 30
        y = 20
        y_name = 120
        y1_frame = 50
        y2_frame = 180
        altura = 0
        self.total = 0
        self.p1 = 0
        self.p2 = 0
        self.p3 = 0
        self.p4 = 0
        self.p5 = 0
        self.p6 = 0
        self.remaining_p1 = pumpData[0][1]
        self.remaining_p2 = pumpData[1][1]
        self.remaining_p3 = pumpData[2][1]
        self.remaining_p4 = pumpData[3][1]
        self.remaining_p5 = pumpData[4][1]
        self.remaining_p6 = pumpData[5][1]

        for drink in pumpData:
            altura = altura + 150
            self.second_canvas.create_rectangle(50,y1_frame, 1180, y2_frame, fill = CREATE_BG)
            #Name
            self.second_canvas.create_text(100, y_name, text=drink[0], fill="black", font=('Helvetica 40 bold'),anchor="w")
            y_name += 150
            y1_frame += 150
            y2_frame += 150

        #create increase Btn
        increaseBtnP1 = ctk.CTkButton(self.second_canvas, image=self.increase_icon,width=5,height=5,text="",command=lambda: self.increase(1),
        borderwidth=0,fg_color = CREATE_BG, hover_color = CREATE_BG)
        increaseBtnP1.place(x=1100,y=110)
        self.p1_txt = self.second_canvas.create_text(1040, 145, text=0, fill="black", font=('Helvetica 30 bold'),anchor="w")
        self.rem_p1_txt = self.second_canvas.create_text(960, 80, text="Remaining: " + str(self.remaining_p1), fill="black", font=('Helvetica 20 bold'),anchor="w") 

        increaseBtnP2 = ctk.CTkButton(self.second_canvas, image=self.increase_icon,width=5,height=5,text="",command=lambda: self.increase(2),
        borderwidth=0,fg_color = CREATE_BG, hover_color = CREATE_BG)
        increaseBtnP2.place(x=1100,y=260)
        self.p2_txt = self.second_canvas.create_text(1040, 295, text=0, fill="black", font=('Helvetica 30 bold'),anchor="w")
        self.rem_p2_txt = self.second_canvas.create_text(960, 230, text="Remaining: " + str(self.remaining_p2), fill="black", font=('Helvetica 20 bold'),anchor="w") 

        increaseBtnP3 = ctk.CTkButton(self.second_canvas, image=self.increase_icon,width=5,height=5,text="",command=lambda: self.increase(3),
        borderwidth=0,fg_color = CREATE_BG, hover_color = CREATE_BG)
        increaseBtnP3.place(x=1100,y=410)
        self.p3_txt = self.second_canvas.create_text(1040, 445, text=0, fill="black", font=('Helvetica 30 bold'),anchor="w")
        self.rem_p3_txt = self.second_canvas.create_text(960, 380, text="Remaining: " + str(self.remaining_p3), fill="black", font=('Helvetica 20 bold'),anchor="w") 

        increaseBtnP4 = ctk.CTkButton(self.second_canvas, image=self.increase_icon,width=5,height=5,text="",command=lambda: self.increase(4),
        borderwidth=0,fg_color = CREATE_BG, hover_color = CREATE_BG)
        increaseBtnP4.place(x=1100,y=560)
        self.p4_txt = self.second_canvas.create_text(1040, 595, text=0, fill="black", font=('Helvetica 30 bold'),anchor="w")
        self.rem_p4_txt = self.second_canvas.create_text(960, 550, text="Remaining: " + str(self.remaining_p4), fill="black", font=('Helvetica 20 bold'),anchor="w") 

        increaseBtnP5 = ctk.CTkButton(self.second_canvas, image=self.increase_icon,width=5,height=5,text="",command=lambda: self.increase(5),
        borderwidth=0,fg_color = CREATE_BG, hover_color = CREATE_BG)
        increaseBtnP5.place(x=1100,y=710)
        self.p5_txt = self.second_canvas.create_text(1040, 745, text=0, fill="black", font=('Helvetica 30 bold'),anchor="w")
        self.rem_p5_txt = self.second_canvas.create_text(960, 700, text="Remaining: " + str(self.remaining_p5), fill="black", font=('Helvetica 20 bold'),anchor="w") 

        increaseBtnP6 = ctk.CTkButton(self.second_canvas, image=self.increase_icon,width=5,height=5,text="",command=lambda: self.increase(6),
        borderwidth=0,fg_color = CREATE_BG, hover_color = CREATE_BG)
        increaseBtnP6.place(x=1100,y=860)
        self.p6_txt = self.second_canvas.create_text(1040, 895, text=0, fill="black", font=('Helvetica 30 bold'),anchor="w")
        self.rem_p6_txt = self.second_canvas.create_text(960, 850, text="Remaining: " + str(self.remaining_p6), fill="black", font=('Helvetica 20 bold'),anchor="w") 

        #create decrease Btn
        decreaseBtnP1 = ctk.CTkButton(self.second_canvas, image=self.decrease_icon,width=5,height=5,text="",command=lambda: self.decrease(1),
        borderwidth=0,fg_color = CREATE_BG, hover_color = CREATE_BG)
        decreaseBtnP1.place(x=950,y=106)

        decreaseBtnP2 = ctk.CTkButton(self.second_canvas, image=self.decrease_icon,width=5,height=5,text="",command=lambda: self.decrease(2),
        borderwidth=0,fg_color = CREATE_BG, hover_color = CREATE_BG)
        decreaseBtnP2.place(x=950,y=256)

        decreaseBtnP3 = ctk.CTkButton(self.second_canvas, image=self.decrease_icon,width=5,height=5,text="",command=lambda: self.decrease(3),
        borderwidth=0,fg_color = CREATE_BG, hover_color = CREATE_BG)
        decreaseBtnP3.place(x=950,y=406)

        decreaseBtnP4 = ctk.CTkButton(self.second_canvas, image=self.decrease_icon,width=5,height=5,text="",command=lambda: self.decrease(4),
        borderwidth=0,fg_color = CREATE_BG, hover_color = CREATE_BG)
        decreaseBtnP4.place(x=950,y=556)

        decreaseBtnP5 = ctk.CTkButton(self.second_canvas, image=self.decrease_icon,width=5,height=5,text="",command=lambda: self.decrease(5),
        borderwidth=0,fg_color = CREATE_BG, hover_color = CREATE_BG)
        decreaseBtnP5.place(x=950,y=706)

        decreaseBtnP6 = ctk.CTkButton(self.second_canvas, image=self.decrease_icon,width=5,height=5,text="",command=lambda: self.decrease(6),
        borderwidth=0,fg_color = CREATE_BG, hover_color = CREATE_BG)
        decreaseBtnP6.place(x=950,y=856)

        submitUwU = ctk.CTkButton(self.second_canvas, text="SUBMIT",width=50,height=50,command=lambda: self.decrease(6),
        borderwidth=0,fg_color = CREATE_BG, hover_color = CREATE_BG)
        submitUwU.place(x=950,y=856)
        second_frame_create.configure(height=altura)
        
        # btn = ctk.CTkButton(self.createAmountCanvas,
        #         width=200,
        #         height=80,
        #         text="+",
        #         text_font=("Inter",50), 
        #         text_color="black",
        #         corner_radius=30,
        #         hover_color=("#ACACAC"),
        #         fg_color="#E5E5E5",
        #         command=lambda :self.getDrink(arr))
        # btn.place(x=50,y=250)

        # UwUBtn = ctk.CTkButton(self.createAmountCanvas,
        #             width=200,
        #             height=80,
        #             text="UwU Time!!",
        #             text_font=("Inter",50), 
        #             text_color="black",
        #             corner_radius=30,
        #             hover_color=("#ACACAC"),
        #             fg_color="#E5E5E5",
        #             command=lambda :self.getDrink(arr))
        # UwUBtn.place(x=50,y=250)  
        
        #Frame Label
        settingLab = ctk.CTkLabel(self.createItemFrame,text="Create",text_font=("Inter",40, "bold"),text_color="black")
        settingLab.place(x=50,y=10)
        ctk.CTkLabel(self.createItemFrame,text="your own drink >w<",text_font=("Inter",30),text_color="black").place(x=270,y=20)
        
        """
        ======================================
                    Setting Frame
        ======================================
        """
        #Frame Creation
        self.settingFrame = ctk.CTkFrame(self,width=WIDTH,height=HEIGHT,fg_color=BLUE_BG,corner_radius=0)
        self.settingCanvas = ctk.CTkCanvas(self.settingFrame,width=WIDTH,height=HEIGHT,bg=BLUE_BG,highlightthickness=0)
        
        # #Profile
        # img = ImageTk.PhotoImage(Image.open(self.profileIconPath).resize((110,110)))
        # profile.append(img)
        # self.settingCanvas.create_image(1790,20,anchor=tk.NW,image=img)
        # self.settingCanvas.create_text(1750, 50, text=self.profileName, fill="black",anchor='e', font=('Inter 30 bold'))
        # self.settingCanvas.create_text(1750, 100, text=self.coin, fill="black",anchor='e', font=('Inter 30 bold'))

        #gear icon
        gear_icon = ImageTk.PhotoImage(Image.open(os.path.join(ASSETS_PATH, "Gear.png")).resize((297,308)))
        profile.append(gear_icon)
        self.settingCanvas.create_image(1470,300,anchor=tk.NW,image=gear_icon)
        
        #Drink List Frame
        self.settingItemFrame = ctk.CTkFrame(self.settingCanvas,width=1250,height=900,fg_color="white",highlightthickness=0)
        self.settingItemFrame.place(x=50,y=80)

        #Drink List Canvas
        self.settingItemCanvas = ctk.CTkCanvas(self.settingItemFrame,width=1250,height=900,bg="black",highlightthickness=0)
        self.settingItemCanvas.place(x=0,y=80)
               
        #Item list Scrollbar
        setting_scrollbar = tk.Scrollbar(self.settingItemFrame, orient=tk.VERTICAL, command=self.settingItemCanvas.yview)
        setting_scrollbar.place(x=1232,y=150,height=750)

        #Configure Canvas to scroll with mouse wheel
        self.settingItemCanvas.configure(yscrollcommand=setting_scrollbar.set)
        self.settingItemCanvas.bind('<Configure>', lambda e: self.settingItemCanvas.configure(scrollregion = self.settingItemCanvas.bbox("all")))
        
        #Pack item frame inside canvas
        second_frame_setting = tk.Frame(self.settingItemCanvas,bg=FAV_BG,width=1250,height=900,highlightthickness=0)
        second_frame_setting.place(x=0,y=0)

        self.settingItemCanvas.create_window((0,0), window=second_frame_setting, anchor="nw")

        #button
        self.button(1500, 700, "Accept!", self.settingCanvas, self.settingFrame, "main", "#34BD20", 200, 80)
        home_button =  ctk.CTkButton(self.settingCanvas, image=self.home_icon,width=5,height=5,text="", bg="gray",command=lambda :self.change_frame(self.settingFrame, "main"),
        borderwidth=0,fg_color = BLUE_BG, hover_color = BLUE_BG)
        home_button.place(x=1750,y=970)
        
        x = 30
        y = 20
        altura = 0
        for drink in pumpData:
            altura = altura + 150
            frame = DrinkSetting(second_frame_setting, drink, "#554994")
            frame.place(x=x,y=y)
            y += 150
        second_frame_setting.configure(height=altura)
        
        #Frame Label
        settingLab = ctk.CTkLabel(self.settingItemFrame,text="Setting",text_font=("Inter",40, "bold"),text_color="black")
        settingLab.place(x=50,y=10)

        """
        ======================================
                    Complete Frame
        ======================================
        """
        #Frame & Canvas creation
        self.completeFrame = ctk.CTkFrame(self,width=WIDTH,height=HEIGHT,fg_color=BLUE_BG)
        self.completeCanvas = ctk.CTkCanvas(self.completeFrame,width=WIDTH,height=HEIGHT,bg=BLUE_BG,highlightthickness=0)

        #Bg
        self.completeBg = ctk.CTkCanvas(self.completeCanvas,width=1000,height=900,bg="white",highlightthickness=0)
        self.completeBg.place(x=450,y=80)
        
        #Profile
        img = ImageTk.PhotoImage(Image.open(self.profileIconPath).resize((110,110)))
        profile.append(img)
        self.completeBg.create_image(500,100,anchor="center",image=img)
        self.completeBg.create_text(500, 200, text=self.profileName, fill="black",anchor="center", font=('Inter 30 bold'))
        self.completeBg.create_text(500, 250, text=self.coin, fill="black",anchor="center", font=('Inter 30 bold'))

        self.completeBg.create_text(500, 350, text="How was the Drink?", fill="black",anchor="center", font=('Inter 60 bold'))
        
        # #Frame Label
        # randomLab = ctk.CTkLabel(self.randomChoice,text="Random",text_font=("Inter",40, "bold"),text_color="black")
        # randomLab.place(x=850,y=30)

        #button
        self.button(600, 750, "discard", self.completeBg, self.completeFrame, "main", "black", 200, 80)
        
        #save button
        save_btn = ctk.CTkButton(self.completeBg,
                            width=200,
                            height=80,
                            text="Save",
                            text_font=("Inter",50),
                            text_color="black",
                            corner_radius=30,
                            hover_color=("#ACACAC"),
                            fg_color="#E5E5E5",
                            command=lambda :self.change_frame(self.completeFrame, "main"))
        save_btn.place(x=200,y=750)

        #input name bar
        entry = ctk.CTkEntry(master=self.completeBg,
                               placeholder_text="Put drink name here",
                               width=400,
                               height=60,
                               fg_color="white",
                               text_color="black",
                               border_width=2,
                               text_font=("inter", 15),
                               corner_radius=10)
        
        entry.place(x=300, y=600)

        """
        ======================================
                    Packing Main Frames
        ======================================
        """
        #Pack Frame & Canvas
        self.browseItemCanvas.bind_all("<MouseWheel>",self._on_mouse_wheel)
        self.favoriteItemCanvas.bind_all("<MouseWheel>",self._on_mouse_wheel)
        self.createItemCanvas.bind_all("<MouseWheel>",self._on_mouse_wheel)
        self.settingItemCanvas.bind_all("<MouseWheel>",self._on_mouse_wheel)
        # self.mainCanvas.pack(fill="both", expand=1)
        # self.mainFrame.pack(fill="both", expand=1)

    def button(self, x_co, y_co, name, canvas, old_frame, new_frame, color, width, height):
        Btn = ctk.CTkButton(canvas,
                            width=width,
                            height=height,
                            text=name,
                            text_font=("Inter",40),
                            text_color="black",
                            corner_radius=30,
                            hover_color= color,
                            fg_color=color,
                            command=lambda :self.change_frame(old_frame, new_frame))
        Btn.place(x=x_co,y=y_co)   
    
    def change_frame(self,oldFrame,newFrame):
        oldFrame.pack_forget()
        if newFrame == "main":
            self.mainFrame.pack(fill="both", expand=1)
            self.mainCanvas.pack(fill="both", expand=1)
        elif newFrame == "create":
            self.createFrame.pack(fill="both", expand=1)
            self.createCanvas.pack(fill="both", expand=1)
        elif newFrame == "setting":
            self.settingFrame.pack(fill="both", expand=1)
            self.settingCanvas.pack(fill="both", expand=1)
        elif newFrame == "browse":
            self.browseFrame.pack(fill="both", expand=1)
            self.browseCanvas.pack(fill="both", expand=1)
        elif newFrame == "favorite":
            self.favoriteFrame.pack(fill="both", expand=1)
            self.favoriteCanvas.pack(fill="both", expand=1)
        elif newFrame == "random":
            self.randomFrame.pack(fill="both", expand=1)
            self.randomCanvas.pack(fill="both", expand=1)
        
    def change_frame_random(self,oldFrame,newFrame):
        oldFrame.pack_forget()
        if newFrame == "random recipe":
            random_recipe = db.getRandomRecipe()
            self.preview(self.RecipeInside, random_recipe, None)
            self.RecipeFrame.pack(fill="both", expand=1)
            self.RecipeCanvas.pack(fill="both", expand=1)
        elif newFrame == "random drink":
            dd = TkinterDispenser()
            random_drink = dd.genRandomDrink(10, 1)
            self.preview(self.DrinkInside, None, random_drink)
            self.DrinkFrame.pack(fill="both", expand=1)
            self.DrinkCanvas.pack(fill="both", expand=1)

    def preview(self, preview_canvas, recipe_list, drink_list):
        preview_canvas.delete('all')
        if recipe_list != None:
            #draw recipe name
            ctk.CTkLabel(self.Recipe,text="Name: ",text_font=("Inter",40),text_color="black").place(x=100, y=120)
            ctk.CTkLabel(preview_canvas,text="Ingredient:",text_font=("Inter", 40),text_color="gray").place(x=50, y=30)
            RecipeName = ctk.CTkLabel(self.Recipe,text=recipe_list[0],text_font=("Inter",50, "bold"),text_color="black")
            RecipeName.place(x=270, y=110)
            #draw ingredient
            y = 150
            for ingredient in recipe_list[4]:
                preview_canvas.create_text(50, y, text = ingredient, fill="black",anchor='w', font=('Inter 40'))
                y += 80
            #draw amount of ingredient
            y = 150
            for amount in recipe_list[5]:
                preview_canvas.create_text(300, y, text = amount, fill="black",anchor='w', font=('Inter 40'))
                y += 80
        elif drink_list!= None:
            ctk.CTkLabel(preview_canvas,text="Ingredient:",text_font=("Inter", 40),text_color="gray").place(x=50, y=30)
            #draw ingredient
            y = 150
            i = 0
            for ingredient in pumpData:
                self.DrinkInside.create_text(50, y, text = ingredient[0], fill="black",anchor='w', font=('Inter 40'))
                y += 80
                i += 1
            #draw amount of ingredient
            y = 150
            for amount in drink_list:
                self.DrinkInside.create_text(300, y, text = amount, fill="black",anchor='w', font=('Inter 40'))
                y += 80

    def UwU_timeBtn(self, x_co, y_co, canvas):
        UwUBtn = ctk.CTkButton(canvas,
                            width=200,
                            height=80,
                            text="UwU Time!!",
                            text_font=("Inter",50),
                            text_color="black",
                            corner_radius=30,
                            hover_color=("red"),
                            fg_color="red",
                            command=lambda :self.dispense_drink())
        UwUBtn.place(x=x_co,y=y_co)
    
    def getDrink(self,arr):
        total = 0
        tempArr = []
        for item in arr:
            total += item.get_total()
            tempArr.append(item.get_total())

    def increase(self, pumpID):
        if self.total < 10:
            if pumpID == 1 and self.remaining_p1 > 0:
                self.p1 += 1
                self.remaining_p1 -= 1
                self.second_canvas.itemconfig(self.p1_txt, text = str(self.p1))
                self.second_canvas.itemconfig(self.rem_p1_txt, text = str("Remaining: " + str(self.remaining_p1)))
            if pumpID == 2 and self.remaining_p2 > 0:
                self.p2 += 1
                self.remaining_p2 -= 1
                self.second_canvas.itemconfig(self.p2_txt, text = str(self.p2))
                self.second_canvas.itemconfig(self.rem_p2_txt, text = str("Remaining: " + str(self.remaining_p2)))
            if pumpID == 3 and self.remaining_p3 > 0:
                self.p3 += 1
                self.remaining_p3 -= 1
                self.second_canvas.itemconfig(self.p3_txt, text = str(self.p3))
                self.second_canvas.itemconfig(self.rem_p3_txt, text = str("Remaining: " + str(self.remaining_p3)))
            if pumpID == 4 and self.remaining_p4 > 0:
                self.p4 += 1
                self.remaining_p4 -= 1
                self.second_canvas.itemconfig(self.p4_txt, text = str(self.p4))
                self.second_canvas.itemconfig(self.rem_p4_txt, text = str("Remaining: " + str(self.remaining_p4)))
            if pumpID == 5 and self.remaining_p5 > 0:
                self.p5 += 1
                self.remaining_p5 -= 1
                self.second_canvas.itemconfig(self.p5_txt, text = str(self.p5))
                self.second_canvas.itemconfig(self.rem_p5_txt, text = str("Remaining: " + str(self.remaining_p5)))
            if pumpID == 6 and self.remaining_p6 > 0:
                self.p6 += 1
                self.remaining_p6 -= 1
                self.second_canvas.itemconfig(self.p6_txt, text = str(self.p6))
                self.second_canvas.itemconfig(self.rem_p6_txt, text = str("Remaining: " + str(self.remaining_p6)))
            self.total = self.p1 + self.p2 + self.p3 + self.p4 + self.p5 + self.p6
            self.createAmountCanvas.itemconfig(self.total_txt, text = str(self.total))

    def decrease(self, pumpID):
        if pumpID == 1:
            if self.p1 > 0:
                self.p1 -= 1
                self.remaining_p1 += 1
                self.second_canvas.itemconfig(self.p1_txt, text = str(self.p1))
                self.second_canvas.itemconfig(self.rem_p1_txt, text = str("Remaining: " + str(self.remaining_p1)))
        if pumpID == 2:
            if self.p2 > 0:
                self.p2 -= 1
                self.remaining_p2 += 1
                self.second_canvas.itemconfig(self.p2_txt, text = str(self.p2))
                self.second_canvas.itemconfig(self.rem_p2_txt, text = str("Remaining: " + str(self.remaining_p2)))
        if pumpID == 3:
            if self.p3 > 0:
                self.p3 -= 1
                self.remaining_p3 += 1
                self.second_canvas.itemconfig(self.p3_txt, text = str(self.p3))
                self.second_canvas.itemconfig(self.rem_p3_txt, text = str("Remaining: " + str(self.remaining_p3)))
        if pumpID == 4:
            if self.p4 > 0:
                self.p4 -= 1
                self.remaining_p4 += 1
                self.second_canvas.itemconfig(self.p4_txt, text = str(self.p4))
                self.second_canvas.itemconfig(self.rem_p4_txt, text = str("Remaining: " + str(self.remaining_p4)))
        if pumpID == 5:
            if self.p5 > 0:
                self.p5 -= 1
                self.remaining_p5 += 1
                self.second_canvas.itemconfig(self.p5_txt, text = str(self.p5))
                self.second_canvas.itemconfig(self.rem_p5_txt, text = str("Remaining: " + str(self.remaining_p5)))
        if pumpID == 6:
            if self.p6 > 0:
                self.p6 -= 1
                self.remaining_p6 += 1
                self.second_canvas.itemconfig(self.p6_txt, text = str(self.p6))
                self.second_canvas.itemconfig(self.rem_p6_txt, text = str("Remaining: " + str(self.remaining_p6)))
        self.total = self.p1 + self.p2 + self.p3 + self.p4 + self.p5 + self.p6
        self.createAmountCanvas.itemconfig(self.total_txt, text = str(self.total))

    def dispense_drink(self):
        tempArr = [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6]
        uwu = DispenseDrink()
        uwu.dispenseFromArr(tempArr)
        print(tempArr)

    def signin(self):
        print("button pressed")
        
    def _on_mouse_wheel(self,event):
        self.browseItemCanvas.yview_scroll(-1 * int((event.delta / 120)), "units")
        
    def quit(self,e):
        self.destroy()
    
    def genDrink(self):
        for i in range(2):
            name = input("Drink name? >")
            ml = int(input("Drink ML? >"))
            self.drinkList[name] = ml
        json_object = json.dumps(self.drinkList, indent=4)
        with open("./src/PythonTkinter/Database/drinkList.json", "w") as outfile:
            outfile.write(json_object)
    
        


app = App()
app.mainloop()
