import tkinter as tk
import requests

root = tk.Tk()

#Screen Config
SCREEN_WIDTH = "1024"
SCREEN_HEIGHT = "600"

root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
root.title("UWU:RE")
root.config(bg="light blue")
root.grid_columnconfigure(0,weight=1)
#root.attributes('-fullscreen', True)
root.bind('<Escape>',lambda e: quit(e))

def quit(e):
    global root
    root.destroy()
    
def changeScreen(oldFrame,screen):
    oldFrame.pack_forget()
    if screen == "select":
        selectScreen()
    
def selectScreen():
    newFrame = tk.Frame(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT,bg='red')
    newFrame.pack(fill='both',expand=True)

def mainScreen():
    global root
    mainFrame = tk.Frame(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT,bg='light blue')
    mainFrame.pack(fill='both',expand=True)

    #Project Name
    name = tk.Label(mainFrame,text="UWU:RE",font=("Ariel",70),bg='light blue').pack(pady=50)

    #Make Drink Button
    makeDrinkBtn = tk.Button(mainFrame,font=("Ariel",20),text="Make Drink",command=  lambda : changeScreen(mainFrame,"select")).pack(padx=150,pady=150,anchor='w')

mainScreen()
root.mainloop()