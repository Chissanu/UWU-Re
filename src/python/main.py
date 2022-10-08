import tkinter as tk
import requests

root = tk.Tk()

#Screen Config
SCREEN_WIDTH = "1920"
SCREEN_HEIGHT = "1080"
# SCREEN_WIDTH = "1650"
# SCREEN_HEIGHT = "1050"
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
root.title("UWU:RE")
root.config(bg="light blue")
root.grid_columnconfigure(0,weight=1)
root.attributes('-fullscreen', True)
root.bind('<Escape>',lambda e: quit(e))

def quit(e):
    global root
    root.destroy()

def mainScreen():
    global root
    mainFrame = tk.Frame(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT,bg='light blue')
    mainFrame.pack(fill='both',expand=True)

    #Project Name
    name = tk.Label(mainFrame,text="UWU:RE",font=("Ariel",70),bg='light blue').pack(pady=50)

    #Make Drink Button
    makeDrinkBtn = tk.Button(mainFrame,font=("Ariel",20),text="Make Drink").pack(padx=150,pady=150,anchor='w')

mainScreen()
root.mainloop()