import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

#Color Pallete
BLUE_BG = "#859FFD"
ALL_BG = "#FFF89A"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        WIDTH = 1920
        HEIGHT = 1080
        self.title("UWU:Reborn from Ashes")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.bind('<Escape>',lambda e: quit(e))
        self.config(bg="#6482EB")
        self.attributes('-fullscreen',True)
        
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
                                    fg_color="#FFF89A",
                                    command=lambda :self.change_frame(self.mainFrame,"browse"))
        self.browseAllBtn.place(x=100,y=200)
        
        self.browseFavBtn = ctk.CTkButton(self.browseCanvas,
                                    width=500,
                                    height=140,
                                    text="Favorite",
                                    text_font=("Inter",50, 'bold'),
                                    text_color="black",
                                    corner_radius=30,
                                    hover_color=("#ACACAC"),
                                    fg_color="#E5E5E5",
                                    command=lambda :self.change_frame(self.mainFrame,"browse"))
        self.browseFavBtn.place(x=550,y=200)
        
        self.browseRandBtn = ctk.CTkButton(self.browseCanvas,
                                    width=500,
                                    height=140,
                                    text="Random",
                                    text_font=("Inter",50, 'bold'),
                                    text_color="black",
                                    corner_radius=30,
                                    hover_color=("#ACACAC"),
                                    fg_color="#E5E5E5",
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
            self.browseCanvas.pack(fill="both", expand=1)
            self.browseFrame.pack(fill="both", expand=1)
        print(newFrame)

    def button_callback(self):
        print("button pressed")
    
    def quit(self,e):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()

