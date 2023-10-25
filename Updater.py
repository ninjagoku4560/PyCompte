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

def GetGithubAsset(dataToFind):
    global GITHUBLINK
    urlList = GITHUBLINK.split("/")
    user = urlList[3]
    repositories = urlList[4]
    # Obtenez les informations de la dernière version du référentiel
    url = f"https://api.github.com/repos/{user}/{repositories}/releases/latest"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data['assets'][0][dataToFind]

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
            file.write(GetGithubAsset("browser_download_url").split("/")[7])
        button.config(text="Vous êtes à jour!")
    else:
        print(f"Échec du téléchargement du fichier. Code de statut : {response.status_code}")


def startUpdaterApp():
    #Definie les proprieters de l'application
    app = Tk()
    app.geometry("800x600")
    app.title("PyCompte Updater")
    app.iconbitmap("logo.ico")

    frm = ttk.Frame(app, padding=10)
    frm.place(width=800, height=600, x=-75, y=0)

    #Download Button
    text = None
    if GetGithubAsset("browser_download_url").split("/")[7] != GetLatestVersionInstalled():
        text = "Nouvelle version disponible!"
    else:
        text = "Vous êtes à jour!"
    DownloadButton = ttk.Button(frm, text=text, command=lambda: Download(GetGithubAsset("browser_download_url"), DATADIRECTORY + "/LatestRelease.zip",DownloadButton))
    DownloadButton.place(x=400, y=450)

    # Texte Date Publication de la derniere version publier
    DateReleaseText = ttk.Label(app, text=f"Date de creation: {GetGithubAsset('created_at')}")
    DateReleaseText.place(x=50, y=50)
    # Texte Taille de la derniere version publier
    SizeReleaseText = ttk.Label(app, text=f"Taile de la version: {GetGithubAsset('size')} Octets")
    SizeReleaseText.place(x=50, y=25)
    # start the app
    app.mainloop()


startUpdaterApp()
