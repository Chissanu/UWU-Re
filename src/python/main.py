import tkinter as tk
import customtkinter as ctk
import os
from pathlib import Path
from PIL import ImageTk, Image

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

class App(ctk.CTk):
    # def __init__(self,name,coin):
    def __init__(self):
        super().__init__()
        WIDTH = 1920
        HEIGHT = 1080
        global img,img1
        self.title("UWU:Reborn from Ashes")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.bind('<Escape>',lambda e: quit(e))
        self.config(bg="#6482EB")
        self.attributes('-fullscreen',True)
        self.profileIconPath = str(os.path.normpath(os.getcwd() + os.sep)) + "\\src\\assets\\profilePic.png"
        # self.profileName = name
        # self.coin = coin
        self.profileName = "Chissanu"
        self.coin = 1000
        
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
        self.nameLabel1.place(x=550,y=350)
        self.nameLabel2 = ctk.CTkLabel(self.mainCanvas,text="Re",text_font=("Inter",180),text_color="black")
        self.nameLabel2.place(x=1180,y=350)
        self.nameLine = self.mainCanvas.create_line(200,315,840,315, fill="white", width=10)
        
        #Buttons
        self.browseBtn = ctk.CTkButton(self.mainCanvas,
                                    width=500,
                                    height=140,
                                    text="Browse",
                                    text_font=("Inter",50, 'bold'),
                                    text_color="black",
                                    corner_radius=30,
                                    hover_color=("#2F8C3D"),
                                    fg_color="#4BD960",
                                    command=lambda :self.change_frame(self.mainFrame,"browse"))
        self.browseBtn.place(x=100,y=700)

        self.createBtn = ctk.CTkButton(self.mainCanvas,
                                    width=500,
                                    height=140,
                                    text="Create",
                                    text_font=("Inter",50, 'bold'),
                                    text_color="black",
                                    corner_radius=30,
                                    hover_color=("#79A439"),
                                    fg_color="#A1D94B",
                                    command=lambda :self.change_frame(self.mainFrame,"browse"))
        self.createBtn.place(x=700,y=700)

        self.settingBtn = ctk.CTkButton(self.mainCanvas,
                                    width=500,
                                    height=140,
                                    text="Setting",
                                    text_font=("Inter",50, 'bold'),
                                    text_color="black",
                                    corner_radius=30,
                                    hover_color=("#ACACAC"),
                                    fg_color="#E5E5E5",
                                    command=lambda :self.change_frame(self.mainFrame,"browse"))
        self.settingBtn.place(x=1300,y=700)
        
        """
        ======================================
                    All FRAME
        ======================================
        """
        #Frame Creation
        self.browseFrame = ctk.CTkFrame(self,width=WIDTH,height=HEIGHT,fg_color=BLUE_BG,corner_radius=0)
        self.browseCanvas = ctk.CTkCanvas(self.browseFrame,width=WIDTH,height=HEIGHT,bg=BLUE_BG,highlightthickness=0)
        
        #Profile
        img1 = ImageTk.PhotoImage(Image.open(self.profileIconPath).resize((110,110)))
        self.browseCanvas.create_image(1790,20,anchor=tk.NW,image=img1)
        self.browseCanvas.create_text(1650, 50, text=self.profileName, fill="black", font=('Inter 30 bold'))
        self.browseCanvas.create_text(1700, 100, text=self.coin, fill="black", font=('Inter 30 bold'))
        
        #All Background  
        self.browseCanvas.create_rectangle(100,340,1550,1000,fill=ALL_BG,outline="")
        
        #Buttons  
        self.browseAllBtn = ctk.CTkButton(self.browseCanvas,
                                    width=500,
                                    height=140,
                                    text="All",
                                    text_font=("Inter",50, 'bold'),
                                    text_color="black",
                                    corner_radius=0,
                                    borderwidth=0,
                                    hover_color=("#ACACAC"),
                                    fg_color=ALL_BG,
                                    command=lambda :self.change_frame(self.mainFrame,"browse"))
        self.browseAllBtn.place(x=100,y=200)
        
        self.browseFavBtn = ctk.CTkButton(self.browseCanvas,
                                    width=500,
                                    height=140,
                                    text="Favorite",
                                    text_font=("Inter",50, 'bold'),
                                    text_color="black",
                                    corner_radius=0,
                                    hover_color=("#ACACAC"),
                                    fg_color=FAV_BG,
                                    command=lambda :self.change_frame(self.browseFrame,"favorite"))
        self.browseFavBtn.place(x=550,y=200)
        
        self.browseRandBtn = ctk.CTkButton(self.browseCanvas,
                                    width=500,
                                    height=140,
                                    text="Random",
                                    text_font=("Inter",50, 'bold'),
                                    text_color="black",
                                    corner_radius=0,
                                    hover_color=("#ACACAC"),
                                    fg_color=RAND_BG,
                                    command=lambda :self.change_frame(self.mainFrame,"random"))
        self.browseRandBtn.place(x=1050,y=200)
        
        """
        ======================================
                    Favorite Frames
        ======================================
        """
        #Frame Creation
        self.favoriteFrame = ctk.CTkFrame(self,width=WIDTH,height=HEIGHT,fg_color=BLUE_BG,corner_radius=0)
        self.favoriteCanvas = ctk.CTkCanvas(self.favoriteFrame,width=WIDTH,height=HEIGHT,bg=BLUE_BG,highlightthickness=0)
        
        #Profile
        img = ImageTk.PhotoImage(Image.open(self.profileIconPath).resize((110,110)))
        self.favoriteCanvas.create_image(1790,20,anchor=tk.NW,image=img)
        self.favoriteCanvas.create_text(1650, 50, text=self.profileName, fill="black", font=('Inter 30 bold'))
        self.favoriteCanvas.create_text(1700, 100, text=self.coin, fill="black", font=('Inter 30 bold'))
        
                #All Background  
        self.favoriteCanvas.create_rectangle(100,340,1550,1000,fill=FAV_BG,outline="")
        
        #Buttons  
        self.browseAllBtn = ctk.CTkButton(self.favoriteCanvas,
                                    width=500,
                                    height=140,
                                    text="All",
                                    text_font=("Inter",50, 'bold'),
                                    text_color="black",
                                    corner_radius=0,
                                    borderwidth=0,
                                    hover_color=("#ACACAC"),
                                    fg_color=ALL_BG,
                                    command=lambda :self.change_frame(self.favoriteFrame,"browse"))
        self.browseAllBtn.place(x=100,y=200)
        
        self.browseFavBtn = ctk.CTkButton(self.favoriteCanvas,
                                    width=500,
                                    height=140,
                                    text="Favorite",
                                    text_font=("Inter",50, 'bold'),
                                    text_color="black",
                                    corner_radius=0,
                                    hover_color=("#ACACAC"),
                                    fg_color=FAV_BG,
                                    command=lambda :self.change_frame(self.favoriteFrame,"favorite"))
        self.browseFavBtn.place(x=550,y=200)
        
        self.browseRandBtn = ctk.CTkButton(self.favoriteCanvas,
                                    width=500,
                                    height=140,
                                    text="Random",
                                    text_font=("Inter",50, 'bold'),
                                    text_color="black",
                                    corner_radius=0,
                                    hover_color=("#ACACAC"),
                                    fg_color=RAND_BG,
                                    command=lambda :self.change_frame(self.favoriteFrame,"random"))
        self.browseRandBtn.place(x=1050,y=200)
        
        
        """
        ======================================
                    Random Frames
        ======================================
        """
        #Frame Creation
        self.randomFrame = ctk.CTkFrame(self,width=WIDTH,height=HEIGHT,fg_color=BLUE_BG,corner_radius=0)
        self.randomCanvas = ctk.CTkCanvas(self.randomFrame,width=WIDTH,height=HEIGHT,bg=BLUE_BG,highlightthickness=0)
        
        #Profile
        img = ImageTk.PhotoImage(Image.open(self.profileIconPath).resize((110,110)))
        self.randomCanvas.create_image(1790,20,anchor=tk.NW,image=img)
        self.randomCanvas.create_text(1650, 50, text=self.profileName, fill="black", font=('Inter 30 bold'))
        self.randomCanvas.create_text(1700, 100, text=self.coin, fill="black", font=('Inter 30 bold'))
        
                #All Background  
        self.randomCanvas.create_rectangle(100,340,1550,1000,fill=RAND_BG,outline="")
        
        #Buttons  
        self.browseAllBtn = ctk.CTkButton(self.randomCanvas,
                                    width=500,
                                    height=140,
                                    text="All",
                                    text_font=("Inter",50, 'bold'),
                                    text_color="black",
                                    corner_radius=0,
                                    borderwidth=0,
                                    hover_color=("#ACACAC"),
                                    fg_color=ALL_BG,
                                    command=lambda :self.change_frame(self.randomFrame,"browse"))
        self.browseAllBtn.place(x=100,y=200)
        
        self.browseFavBtn = ctk.CTkButton(self.randomCanvas,
                                    width=500,
                                    height=140,
                                    text="Favorite",
                                    text_font=("Inter",50, 'bold'),
                                    text_color="black",
                                    corner_radius=0,
                                    hover_color=("#ACACAC"),
                                    fg_color=FAV_BG,
                                    command=lambda :self.change_frame(self.randomFrame,"favorite"))
        self.browseFavBtn.place(x=550,y=200)
        
        self.browseRandBtn = ctk.CTkButton(self.randomCanvas,
                                    width=500,
                                    height=140,
                                    text="Random",
                                    text_font=("Inter",50, 'bold'),
                                    text_color="black",
                                    corner_radius=0,
                                    hover_color=("#ACACAC"),
                                    fg_color=RAND_BG,
                                    command=lambda :self.change_frame(self.mainFrame,"browse"))
        self.browseRandBtn.place(x=1050,y=200)
        
        
        
        """
        ======================================
                    Packing Main Frames
        ======================================
        """
        #Pack Frame & Canvas
        self.mainCanvas.pack(fill="both", expand=1)
        self.mainFrame.pack(fill="both", expand=1)
        
    
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

    def button_callback(self):
        print("button pressed")
    
    def quit(self,e):
        self.destroy()


app = App()
app.mainloop()