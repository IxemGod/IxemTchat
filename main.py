from tkinter import *
import requests
from bs4 import BeautifulSoup
import threading
import time
import sys
import warnings
from playsound import playsound
import json
from vars import *
from setting import *


warnings.filterwarnings("ignore")

"""
----------------------- IxemTchat -----------------------
Salut à toi jeune entrepreuneur ! Bienvenu(e) dans IxemTchat !
Ceci est un client fait en Python. Vous avez la possibilité de
modifié vos paramêtre selon vos envie ^^. Bonne discussion !

- IxemGod
"""

# On initialise les varriable global
DebutVar()




def clear():
    Vars.ChampsRetour.delete("1.0",END)



def affichage_chat():
    Vars.boite.destroy()
    Vars.boite = Frame(background=Vars.bg)

    Vars.ChampsRetour = Text(Vars.window, bg=Vars.bg, fg=Vars.fg)
    Vars.ChampsEnvoie = Entry(Vars.boite,width=40)
    Vars.BtnRefresh = Button(Vars.boite, text="clear",command=clear)
    Vars.BtnEnvoyer = Button(Vars.boite, text="Envoyer",command=sends)
    Vars.BtnSettings = Button(Vars.window, text="Paramêtre", command=settings)

    Vars.ChampsRetour.pack(expand=True, fill="both")
    Vars.ChampsEnvoie.grid( column=1,columnspan=3,row=0)
    Vars.BtnRefresh.grid(column=5,row=0)
    Vars.BtnEnvoyer.grid(column=6,row=0)
    Vars.boite.pack(fill=X)
    Vars.BtnSettings.pack(fill=X)
    Vars.window.update()


def MsgInsert(msg,id,user):
    Vars.id = int(id)
    if user == Vars.user:
        user = "Vous"
    phrase = f"{user} > {msg}\n"
    Vars.ChampsRetour.insert(END,phrase)


def commands(msg):
    if msg == "online" or msg == "Online":
        #On récupère les valeurs de la page web
        url = Vars.chemin+"tchat/tchat.php?task=online"
        response = requests.get(url)
        Vars.ChampsRetour.insert(END,"\n Utilisateur connecté(e) :\n")
        if response.ok:
            links = []
            soup = BeautifulSoup(response.text)
            divs = soup.findAll('div')
            for div in divs:
                links.append(div)
            for lien in links:
                lien = str(lien)
                lien = lien.split("£")
                del lien[-1]
                for item in lien:
                    if "<div>" in item:
                        item = item+"s"
                        Vars.ChampsRetour.insert(END,"[*] - "+item[5:-1]+"\n")
                    else:
                        Vars.ChampsRetour.insert(END,"[*] - "+item+"\n")
        return True
    else:
        return False


def send(event):
    Message = Vars.ChampsEnvoie.get()
    if commands(Message) == False:
        Vars.ChampsEnvoie.delete(0, END)
        url = Vars.chemin+"tchat/tchat.php?task=send&user="+Vars.user+"&content="+Message
        response = requests.get(url)

def sends():
    Message = Vars.ChampsEnvoie.get()
    if commands(Message) == False:
        Vars.ChampsEnvoie.delete(0, END)
        url = Vars.chemin+"tchat/tchat.php?task=send&user="+Vars.user+"&content="+Message
        response = requests.get(url)

def prints():
    Vars.ChampsRetour.insert("end","		*--Connexion Effectué !--*\n")
    while True:
        time.sleep(Vars.delay)
        try:
            contenue = Vars.ChampsRetour.get("1.0", END)
            contenue = contenue.split("\n")
            if  len(contenue) > 25:
                Vars.ChampsRetour.delete("1.0",END)
                posi = 9
                for i in range(1,8):
                    posi-=1
                    Vars.ChampsRetour.insert("end",str(contenue[posi*(-1)])+"\n")

            #On récupère les valeurs de la page web
            url = Vars.chemin+"tchat/tchat.php?task=print&id="+str(Vars.id)+"&user="+Vars.user
            response = requests.get(url)
            if response.ok:
                links = []
                soup = BeautifulSoup(response.text)
                divs = soup.findAll('div')
                for div in divs:
                    links.append(div)
                for lien in links:
                    lien = str(lien)
                    lien = lien.split("£")
                    MsgInsert(lien[1],lien[2],lien[3])
                    if Vars.sound and lien[3] != Vars.user:
                        playsound("song.mp3")
        except:
            #On enregistre les id dans un fichier txt
            jsonString = "{"+f"""
            "theme":"{Vars.theme}",
            "delay-refresh":{Vars.delay},
            "sound":{str(Vars.sound).lower()},
            "id":{Vars.id},
            "pseudo":"{Vars.user}" """+"}"
            jsonString = json.loads(jsonString)

            file = open("db.json", "w+")
            json.dump(jsonString, file)
            file.close()
            sys.exit()

# On définit la première fenêtre
def start():
    affichage_chat()
    t1 = threading.Thread(target = prints)
    t1.start()
    Vars.window.bind('<Return>',send)

start()
Vars.window.mainloop()
