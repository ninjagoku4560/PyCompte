import os
import Cryptage, Updater
import tkinter

FILEPATH = os.path.abspath(__file__)
FILEDIRECTORY = os.getcwd()
DATADIRECTORY = FILEDIRECTORY + "/data"
print(FILEDIRECTORY)


def init():
    # créé le dossier data
    os.makedirs(DATADIRECTORY, exist_ok=True)
    if not os.path.exists(DATADIRECTORY):
        Cryptage.writeKey(DATADIRECTORY)


def start():
    init()


start()