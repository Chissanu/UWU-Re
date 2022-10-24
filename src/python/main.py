from cgitb import text
import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        WIDTH = 1024
        HEIGHT = 600
        self.title("UWU:Reborn from Ashes")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.bind('<Escape>',lambda e: quit(e))
        self.config(bg="#6482EB")
        self.resizable(False, False) 
        
        """
        ======================================
                    SELECT FRAME
        ======================================
        """
        #Frame & Canvas creation
        self.mainFrame = ctk.CTkFrame(self,width=WIDTH,height=HEIGHT,fg_color="#6482EB")
        self.mainCanvas = ctk.CTkCanvas(self.mainFrame,width=WIDTH,height=HEIGHT,bg="#6482EB",highlightthickness=0)
        
        #Logo Label
        self.nameLabel1 = ctk.CTkLabel(self.mainCanvas,text="UwU:",text_font=("Inter",130))
        self.nameLabel1.place(x=200,y=123)
        self.nameLabel2 = ctk.CTkLabel(self.mainCanvas,text="Re",text_font=("Inter",130),text_color="black")
        self.nameLabel2.place(x=620,y=123)
        self.nameLine = self.mainCanvas.create_line(200,315,840,315, fill="white", width=10)
        
        #Buttons
        self.browseBtn = ctk.CTkButton(self.mainCanvas,width=248,
                                       height=70,
                                       text="Browse",
                                       text_font=("Inter",30, 'bold'),
                                       text_color="black",
                                       corner_radius=30,
                                       hover_color=("#2F8C3D"),
                                       fg_color="#4BD960",
                                       command=lambda :self.change_frame(self.mainFrame,"browse"))
        self.browseBtn.place(x=98,y=380)
        
        """
        ======================================
                    Browse FRAME
        ======================================
        """
        #Frame Creation
        self.test = ctk.CTkFrame(self,width=WIDTH,height=HEIGHT,fg_color="red",corner_radius=0)
        
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
            self.test.pack()
        print(newFrame)

    def button_callback(self):
        print("button pressed")
    
    def quit(self,e):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()

