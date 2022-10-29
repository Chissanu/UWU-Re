import customtkinter
from typing import TypeVar

class itemBox(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 305,
                 height: int = 118,
                 name: str = TypeVar
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)
        
        self.drinkName = name
        self.drinkPrice = price