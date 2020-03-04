#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Amira
#
# Created:     02/03/2020
# Copyright:   (c) Amira 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import platform
class Widget:
    def print(self): print("Widget.print")

class Edit(Widget):
    def print(self): print("Edit.print")

class Button(Widget):
    def print(self): print("Button.print")

class LinuxEdit(Edit):
    def print(self): print("LinuxEdit")

class WinEdit(Edit):
    def print(self): print("WinEdit")

class LinuxButton(Button):
    def print(self): print("LinuxButton")

class WinButton(Button):
    def print(self): print("WinButton")

class GuiFactory:
    def createGui(self):
        pass

class LinuxGuiFactory(GuiFactory):
    def createGui(self):
        if type=="Edit": return LinuxEdit()
        if type=="Button": return LinuxButton()

class WinGuiFactory(GuiFactory):
    def createGui(type):
        if type=="Edit": return WinEdit()
        if type=="Button": return WinButton()

if __name__ == '__main__':
    systeme = platform.system()
    print("Le Systeme est: "+systeme)

    if systeme =="Windows":
        for type in ("Edit","Button"):
            objet=WinGuiFactory.createGui(type)
            objet.print()

    elif systeme=="Linux":
        for type in ("Edit","Button"):
            objet=LinuxGuiFactory.createGui(type)
            objet.print()

