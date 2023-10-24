from tkinter import *
from creational.singleton import Singleton



class Window(Tk,Singleton):
    def __init__(self):
        super().__init__()