import requests
import os
from tk import *
from tkinter import ttk
from tkinter import *


FILEDIRECTORY = os.getcwd()
DATADIRECTORY = FILEDIRECTORY + "/data"


def GetLatestRelease(urlRep):
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


def Download(url, destination_path):
    # Effectuez la requête de téléchargement
    response = requests.get(url)

    # Vérifiez si la requête a réussi
    if response.status_code == 200:
        # Enregistrez le contenu du fichier téléchargé dans le chemin de destination spécifié
        with open(destination_path, 'wb') as file:
            file.write(response.content)
        print(f"Le fichier a été téléchargé avec succès à l'emplacement : {destination_path}")
    else:
        print(f"Échec du téléchargement du fichier. Code de statut : {response.status_code}")


def startUpdaterApp():
    app = Tk()
    frm = ttk.Frame(app, padding=10)
    frm.grid()
    ttk.Button(frm, text="Quit", command=Download(GetLatestRelease("https://github.com/ninjagoku4560/PyCompte"),
                                                  DATADIRECTORY + "/LatestRelease.zip")).grid(column=1, row=0)
    app.mainloop()


startUpdaterApp()
