import subprocess

dependance = ["tk","requests","cryptography"]


def InstallModule(Module):
    subprocess.run(['pip', 'install', Module])


def InstallAllModule():
    print("Début de installation des modules requis")
    for i in dependance:
        InstallModule(i)
        print(f"Module {i} à été installer")
