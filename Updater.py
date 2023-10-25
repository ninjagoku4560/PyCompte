import time
import requests
import os
from tkinter import ttk
from tkinter import *


FILEDIRECTORY = os.getcwd()
DATADIRECTORY = FILEDIRECTORY + "/data"
VERSIONFILE = FILEDIRECTORY+"/version.txt"
GITHUBLINK = "https://github.com/ninjagoku4560/PyCompte"


def GetLatestVersionInstalled():
    if not os.path.exists(VERSIONFILE):
        print("Le fichier 'version.txt' n'existe pas")
        print("Installation de la derniere version disponible...")
        Download(GITHUBLINK,DATADIRECTORY)
    else:
        with open(VERSIONFILE) as file:
            versionfile = file.read()
        print(f"La derniere version installé est {versionfile}")
    return versionfile


def GetLinkLatestRelease(urlRep):
    urlList = urlRep.split("/")
    user = urlList[3]
    repositories = urlList[4]
    # Obtenez les informations de la dernière version du référentiel
    url = f"https://api.github.com/repos/{user}/{repositories}/releases/latest"
    response = requests.get(url)
    data = response.json()

    # Vérifiez si la requête a réussi
    if response.status_code == 200:
        # Obtenez le lien de téléchargement de l'actif de la dernière version
        if 'assets' in data and len(data['assets']) > 0:
            download_link = data['assets'][0]['browser_download_url']
            print(f"Le lien de téléchargement de la dernière version de {repositories} est : {download_link}")
            return download_link
        else:
            print(f"Aucun actif trouvé pour la dernière version de {repositories}.")
    else:
        print(f"Échec de la requête. Code de statut : {response.status_code}")


def GetTagLatestRelease(urlRep):
    urlList = urlRep.split("/")
    user = urlList[3]
    repositories = urlList[4]
    # Obtenez les informations de la dernière version du référentiel
    url = f"https://api.github.com/repos/{user}/{repositories}/releases/latest"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        browser_download_url = data['assets'][0]['browser_download_url']
        BDUList = browser_download_url.split("/")
        print(f"Le tag de la derniere version est {BDUList[7]}")
        return BDUList[7]


def Download(url, destination_path,button):
    # Effectuez la requête de téléchargement
    response = requests.get(url)

    # Vérifiez si la requête a réussi
    if response.status_code == 200:
        # Enregistrez le contenu du fichier téléchargé dans le chemin de destination spécifié
        with open(destination_path, 'wb') as file:
            file.write(response.content)
        print(f"Le fichier a été téléchargé avec succès à l'emplacement : {destination_path}")
        with open(VERSIONFILE, "w") as file:
            file.write(GetTagLatestRelease(GITHUBLINK))
        button.config(text="Vous êtes à jour!")
    else:
        print(f"Échec du téléchargement du fichier. Code de statut : {response.status_code}")


def startUpdaterApp():
    app = Tk(screenName="PyCompte Updater")
    app.geometry("800x600")

    frm = ttk.Frame(app, padding=10)
    frm.place(width=800, height=600, x=-75, y=0)
    text = None
    if GetTagLatestRelease(GITHUBLINK) != GetLatestVersionInstalled():
        text = "Nouvelle version disponible!"
    else:
        text = "Vous êtes à jour!"
    DownloadButton = ttk.Button(frm, text=text, command=lambda: Download(GetLinkLatestRelease(GITHUBLINK), DATADIRECTORY + "/LatestRelease.zip",DownloadButton))
    DownloadButton.place(x=400, y=450)
    app.mainloop()


startUpdaterApp()
