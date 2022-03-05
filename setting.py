from tkinter import *
from vars import *
import json


def SetPseudo():
    result = Vars.InputPseudo.get()
    jsonString = "{"+f"""
    "theme":"{Vars.theme}",
    "delay-refresh":{Vars.delay},
    "sound":{str(Vars.sound).lower()},
    "id":{Vars.id},
    "pseudo":"{result}" """+"}"
    jsonString = json.loads(jsonString)

    file = open("db.json", "w+")
    json.dump(jsonString, file)
    file.close()

    Vars.boite.destroy()
    DebutVar()
    Vars.window.update()
    settings()

def SetThemeDark():
    SetTheme("dark")

def SetThemeClair():
    SetTheme("clair")



def SetTheme(var):
    jsonString = "{"+f"""
    "theme":"{var}",
    "delay-refresh":{Vars.delay},
    "sound":{str(Vars.sound).lower()},
    "id":{Vars.id},
    "pseudo":"{Vars.user}" """+"}"
    jsonString = json.loads(jsonString)

    file = open("db.json", "w+")
    json.dump(jsonString, file)
    file.close()
    Vars.boite.destroy()
    DebutVar()
    Vars.window.update()
    settings()


def SetDelay():
    delay = Vars.InputDelay.get()
    try:
        delay = int(delay)
        jsonString = "{"+f"""
        "theme":"{Vars.theme}",
        "delay-refresh":{delay},
        "sound":{str(Vars.sound).lower()},
        "id":{Vars.id},
        "pseudo":"{Vars.user}" """+"}"
        jsonString = json.loads(jsonString)

        file = open("db.json", "w+")
        json.dump(jsonString, file)
        file.close()
        Vars.boite.destroy()
        DebutVar()
        Vars.window.update()
        settings()
    except:
        return


def SetSoundYes():
    SetSound(True)

def SetSoundNo():
    SetSound(False)



def SetSound(var):
    jsonString = "{"+f"""
    "theme":"{Vars.theme}",
    "delay-refresh":{Vars.delay},
    "sound":{str(var).lower()},
    "id":{Vars.id},
    "pseudo":"{Vars.user}" """+"}"
    jsonString = json.loads(jsonString)

    file = open("db.json", "w+")
    json.dump(jsonString, file)
    file.close()
    Vars.boite.destroy()
    DebutVar()
    Vars.window.update()
    settings()

    

# Fenêtre de paramêtre
def settings():
    Vars.boite.destroy()
    Vars.ChampsRetour.destroy()
    Vars.ChampsEnvoie.destroy()
    Vars.BtnSettings.destroy()

    Vars.boite = Frame(Vars.window,bg=Vars.bg)
    Vars.FrPseudo = Frame(Vars.boite,bg=Vars.bg)
    Vars.FrSound = Frame(Vars.boite,bg=Vars.bg)
    Vars.FrDelay = Frame(Vars.boite,bg=Vars.bg)
    Vars.FrTheme = Frame(Vars.boite,bg=Vars.bg)

    Vars.separation = Frame(Vars.boite)
    Vars.separationBis = Frame(Vars.boite)
    Vars.TSeparation = Label(Vars.separation, text="    ",font=('Input Player', 40), bg=Vars.bg,fg=Vars.bg)
    Vars.TSeparationBis = Label(Vars.separationBis, text="A",font=('Input Player', 40), bg=Vars.bg,fg=Vars.bg)

    Vars.TPseudo = Label(Vars.FrPseudo,text="Pseudonyme :",font=( 20),fg=Vars.fg,bg=Vars.bg)
    Vars.InputPseudo = Entry(Vars.FrPseudo,bg=Vars.bg,fg=Vars.fg)
    Vars.BtnPseudo = Button(Vars.FrPseudo, text="Valider",fg=Vars.fg, bg=Vars.bg, command=SetPseudo)

    Vars.InputPseudo.insert(0,Vars.user)

    Vars.TSound = Label(Vars.FrSound,text="Notification :",font=( 20),fg=Vars.fg,bg=Vars.bg)
    if Vars.sound:
        Vars.BtnSoundYes = Button(Vars.FrSound,fg=Vars.fg, text="Activer",bg="green",command=SetSoundYes)
        Vars.BtnSoundNo = Button(Vars.FrSound, fg=Vars.fg,text="Désactiver",bg=Vars.bg,command=SetSoundNo)
    else:
        Vars.BtnSoundYes = Button(Vars.FrSound,fg=Vars.fg, text="Activer",bg=Vars.bg,command=SetSoundYes)
        Vars.BtnSoundNo = Button(Vars.FrSound, fg=Vars.fg,text="Désactiver", bg="red",command=SetSoundNo)


    Vars.TDelay = Label(Vars.FrDelay,text="Intervale d'actualisation :",font=( 20),bg=Vars.bg,fg=Vars.fg)
    Vars.InputDelay = Entry(Vars.FrDelay,fg=Vars.fg,bg=Vars.bg)
    Vars.BtnDelay = Button(Vars.FrDelay,fg=Vars.fg,bg=Vars.bg, text="Valider", command=SetDelay)

    Vars.InputDelay.insert(0,Vars.delay)

    Vars.TTheme = Label(Vars.FrTheme,text="Thême :",bg=Vars.bg,font=( 20),fg=Vars.fg)
    if Vars.theme == "dark":
        Vars.BtnThemeYes = Button(Vars.FrTheme, fg=Vars.fg,text="Sombre",bg="green", command=SetThemeDark)
        Vars.BtnThemeNo = Button(Vars.FrTheme, fg=Vars.fg,text="Clair",bg=Vars.bg, command=SetThemeClair)
    else:
        Vars.BtnThemeYes = Button(Vars.FrTheme,fg=Vars.fg, text="Sombre",bg=Vars.bg, command=SetThemeDark)
        Vars.BtnThemeNo = Button(Vars.FrTheme, fg=Vars.fg,text="Clair", bg="green", command=SetThemeClair)


    Vars.TPseudo.pack(fill=X)
    Vars.InputPseudo.pack(fill=X)
    Vars.BtnPseudo.pack(fill=X)

    Vars.TSeparation.pack(fill=X)
    Vars.TSeparationBis.pack(fill=X)

    Vars.TSound.pack(fill=X)
    Vars.BtnSoundYes.pack(fill=X)
    Vars.BtnSoundNo.pack(fill=X)

    Vars.TDelay.pack(fill=X)
    Vars.InputDelay.pack(fill=X)
    Vars.BtnDelay.pack(fill=X)

    Vars.TTheme.pack(fill=X)
    Vars.BtnThemeYes.pack(fill=X)
    Vars.BtnThemeNo.pack(fill=X)

    Vars.FrPseudo.grid(column=1, row=1)
    Vars.separation.grid(column=2,row=1)
    Vars.FrSound.grid(column=3, row=1)

    Vars.separationBis.grid(column=0,row=2)

    Vars.FrDelay.grid(column=1, row=3)
    Vars.separation.grid(column=2,row=3)
    Vars.FrTheme.grid(column=3, row=3)

    Vars.boite.pack()
    Vars.window.update()
    
