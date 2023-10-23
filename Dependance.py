import subprocess


def InstallModule(Module):
    subprocess.check_call(['pip', 'install', Module])
