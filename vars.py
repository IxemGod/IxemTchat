from tkinter import *
import json

class Vars:

    fg,bg,theme,user,delay,sound,id = "","","","",1,"",0
    window = Tk()
    window.geometry('500x510')
    window.minsize(500,510)
    window.maxsize(500,510)
    window.title('IxemTchat')
    chemin = "http://90.27.106.197/"
    # chemin = "http://192.168.1.34/"


def DebutVar():
    db = open("db.json", "r+").read()
    data = json.loads(db)
    Vars.user = data["pseudo"]
    Vars.id = data["id"]
    Vars.theme = data["theme"]
    Vars.delay = data["delay-refresh"]
    Vars.sound = data["sound"]

    if Vars.theme == "dark":
        Vars.fg ="white"
        Vars.bg ="black"
    else:
        Vars.fg ="black"
        Vars.bg ="white"

    Vars.window.config(background=Vars.bg)
    Vars.boite = Frame(background = Vars.bg)

