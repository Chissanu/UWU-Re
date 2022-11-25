import tkinter as tk
import customtkinter as ctk
import os
import json
from pathlib import Path
from PIL import ImageTk, Image
from Classes.DrinkFrame import DrinkFrame
from Database.DB import Database

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

db = Database()
browseData = list(db.queryDrinkDB())

#To do open user.json and send userID to a function
#favData = db.getFavData(userID)


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
        self.profileIconPath = str(os.path.normpath(os.getcwd() + os.sep)) + "/src/PyThonTkinter/assets/profilePic.png"
        # self.profileName = name
        # self.coin = coin
        self.profileName = "Chissanu"
        self.coin = "Coins:" + str(1000)
        self.drinkList = {}
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
        # #Frame & Canvas creation
        # self.mainFrame = ctk.CTkFrame(self,width=WIDTH,height=HEIGHT,fg_color=BLUE_BG)
        # self.mainCanvas = ctk.CTkCanvas(self.mainFrame,width=WIDTH,height=HEIGHT,bg=BLUE_BG,highlightthickness=0)
        
        # #Logo Label
        # self.nameLabel1 = ctk.CTkLabel(self.mainCanvas,text="UwU:",text_font=("Inter",180),text_color="white")
        # self.nameLabel1.place(x=550,y=350)
        # self.nameLabel2 = ctk.CTkLabel(self.mainCanvas,text="Re",text_font=("Inter",180),text_color="black")
        # self.nameLabel2.place(x=1180,y=350)
        # self.nameLine = self.mainCanvas.create_line(200,315,840,315, fill="white", width=10)
        
        # #Buttons
        # self.browseBtn = ctk.CTkButton(self.mainCanvas,
        #                             width=500,
        #                             height=140,
        #                             text="Browse",
        #                             text_font=("Inter",50, 'bold'),
        #                             text_color="black",
        #                             corner_radius=30,
        #                             hover_color=("#2F8C3D"),
        #                             fg_color="#4BD960",
        #                             command=lambda :self.change_frame(self.mainFrame,"browse"))
        # self.browseBtn.place(x=100,y=700)

        # self.createBtn = ctk.CTkButton(self.mainCanvas,
        #                             width=500,
        #                             height=140,
        #                             text="Create",
        #                             text_font=("Inter",50, 'bold'),
        #                             text_color="black",
        #                             corner_radius=30,
        #                             hover_color=("#79A439"),
        #                             fg_color="#A1D94B",
        #                             command=lambda :self.change_frame(self.mainFrame,"browse"))
        # self.createBtn.place(x=700,y=700)

        # self.settingBtn = ctk.CTkButton(self.mainCanvas,
        #                             width=500,
        #                             height=140,
        #                             text="Setting",
        #                             text_font=("Inter",50, 'bold'),
        #                             text_color="black",
        #                             corner_radius=30,
        #                             hover_color=("#ACACAC"),
        #                             fg_color="#E5E5E5",
        #                             command=lambda :self.change_frame(self.mainFrame,"browse"))
        # self.settingBtn.place(x=1300,y=700)
        
        # #Pack Frame & Canvas
        # self.mainCanvas.pack(fill="both", expand=1)
        # self.mainFrame.pack(fill="both", expand=1)
              
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
        
        #Item List Frame
        self.browseItemFrame = ctk.CTkFrame(self.browseCanvas,width=1250,height=900,fg_color=ALL_BG,highlightthickness=0)
        self.browseItemFrame.place(x=50,y=80)
        
        #Item List Canvas
        self.browseItemCanvas = ctk.CTkCanvas(self.browseItemFrame,width=1250,height=750,bg=ALL_BG,highlightthickness=0)
        self.browseItemCanvas.place(x=0,y=150)
        
        #Item list Scrollbar
        my_scrollbar = tk.Scrollbar(self.browseItemFrame, orient=tk.VERTICAL, command=self.browseItemCanvas.yview)
        my_scrollbar.place(x=1232,y=150,height=750)

        #Configure Canvas to scroll with mouse wheel
        self.browseItemCanvas.configure(yscrollcommand=my_scrollbar.set)
        self.browseItemCanvas.bind('<Configure>', lambda e: self.browseItemCanvas.configure(scrollregion = self.browseItemCanvas.bbox("all")))
        
        #Pack item frame inside canvas
        second_frame = tk.Frame(self.browseItemCanvas,bg=ALL_BG,width=1250,height=900,highlightthickness=0)
        second_frame.place(x=0,y=0)

        self.browseItemCanvas.create_window((0,0), window=second_frame, anchor="nw")

        #button
        self.button(400, 80, "Favorite", self.browseCanvas, self.browseFrame, "favorite")
        self.button(800, 80, "Random", self.browseCanvas, self.browseFrame, "random")

        self.browseFrame.pack(fill="both", expand=1)
        self.browseCanvas.pack(fill="both", expand=1)
        
        
        x = 30
        y = 20
        altura = 0
        for drink in browseData:
            altura = altura + 150
            frame = DrinkFrame(second_frame,drink, "#FF8787").place(x=x,y=y)
            y += 150
        print(altura)
        second_frame.configure(height=altura)
        
        #Frame Label
        allLab = ctk.CTkLabel(self.browseItemFrame,text="All",text_font=("Inter",40),text_color="black")
        allLab.place(x=100,y=30)
        
        #Search bar
        entry = ctk.CTkEntry(master=self.browseItemFrame,
                               placeholder_text="Search",
                               width=300,
                               height=40,
                               fg_color="white",  
                               text_color="black",
                               border_width=2,
                               text_font=("inter", 15),
                               corner_radius=10)
        
        entry.place(x=30, y=100)
        

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
        
        #Item List Frame
        self.favoriteItemFrame = ctk.CTkFrame(self.favoriteCanvas,width=1250,height=900,fg_color=FAV_BG,highlightthickness=0)
        self.favoriteItemFrame.place(x=50,y=80)
        
        #Item List Canvas
        self.favoriteItemCanvas = ctk.CTkCanvas(self.favoriteItemFrame,width=1250,height=750,bg=FAV_BG,highlightthickness=0)
        self.favoriteItemCanvas.place(x=0,y=150)
        
        #Item list Scrollbar
        my_scrollbar = tk.Scrollbar(self.favoriteItemFrame, orient=tk.VERTICAL, command=self.favoriteItemCanvas.yview)
        my_scrollbar.place(x=1232,y=150,height=750)

        #Configure Canvas to scroll with mouse wheel
        self.favoriteItemCanvas.configure(yscrollcommand=my_scrollbar.set)
        self.favoriteItemCanvas.bind('<Configure>', lambda e: self.favoriteItemCanvas.configure(scrollregion = self.favoriteItemCanvas.bbox("all")))
        
        #Pack item frame inside canvas
        second_frame_fav = tk.Frame(self.favoriteItemCanvas,bg=FAV_BG,width=1250,height=900,highlightthickness=0)
        second_frame_fav.place(x=0,y=0)

        self.favoriteItemCanvas.create_window((0,0), window=second_frame_fav, anchor="nw")

        #button
        self.button(200, 80, "All", self.favoriteCanvas, self.favoriteFrame, "browse")
        self.button(800, 80, "Random", self.favoriteCanvas, self.favoriteFrame, "random")
        
        x = 30
        y = 20
        altura = 0
        for drink in browseData:
            altura = altura + 150
            frame = DrinkFrame(second_frame_fav,drink, "#554994").place(x=x,y=y)
            y += 150
        print(altura)
        second_frame_fav.configure(height=altura)
        
        #Frame Label
        favoriteLab = ctk.CTkLabel(self.favoriteItemFrame,text="Favorite",text_font=("Inter",40),text_color="black")
        favoriteLab.place(x=450,y=30)

        # Search bar
        entry = ctk.CTkEntry(master=self.favoriteItemFrame,
                               placeholder_text="Search",
                               width=300,
                               height=40,
                               fg_color="white",
                               text_color="black",
                               border_width=2,
                               text_font=("inter", 15),
                               corner_radius=10)
        
        entry.place(x=30, y=100)

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
       
        #Item List Frame
        self.randomItemFrame = ctk.CTkFrame(self.randomCanvas,width=1250,height=900,fg_color=RAND_BG,highlightthickness=0)
        self.randomItemFrame.place(x=50,y=80)
        
        #button
        self.button(200, 80, "All", self.randomCanvas, self.randomFrame, "browse")
        self.button(500, 80, "Favorite", self.randomCanvas, self.randomFrame, "favorite")

        #Frame Label
        favoriteLab = ctk.CTkLabel(self.favoriteItemFrame,text="Random",text_font=("Inter",40),text_color="black")
        favoriteLab.place(x=800,y=30)

        """
        ======================================
                    Packing Main Frames
        ======================================
        """
        #Pack Frame & Canvas
        self.browseItemCanvas.bind_all("<MouseWheel>",self._on_mouse_wheel)
        self.favoriteItemCanvas.bind_all("<MouseWheel>",self._on_mouse_wheel)
        # self.mainCanvas.pack(fill="both", expand=1)
        # self.mainFrame.pack(fill="both", expand=1)
        
        
    
    def change_frame(self,oldFrame,newFrame):
        oldFrame.pack_forget()
        if newFrame == "browse":
            self.browseFrame.pack(fill="both", expand=1)
            self.browseCanvas.pack(fill="both", expand=1)
        elif newFrame == "favorite":
            self.favoriteFrame.pack(fill="both", expand=1)
            self.favoriteCanvas.pack(fill="both", expand=1)
        elif newFrame == "random":
            self.randomFrame.pack(fill="both", expand=1)
            self.randomCanvas.pack(fill="both", expand=1)
        print(newFrame)

    def button(self, x_co, y_co, name, canvas, old_frame, new_frame):
        Btn = ctk.CTkButton(canvas,
                            width=200,
                            height=80,
                            text=name,
                            text_font=("Inter",50, 'bold'),
                            text_color="black",
                            corner_radius=30,
                            hover_color=("#ACACAC"),
                            fg_color="#E5E5E5",
                            command=lambda :self.change_frame(old_frame, new_frame))
        Btn.place(x=x_co,y=y_co)

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
        print(self.drinkList)
        json_object = json.dumps(self.drinkList, indent=4)
        with open("./src/PythonTkinter/Database/drinkList.json", "w") as outfile:
            outfile.write(json_object)
    
        


app = App()
app.mainloop()