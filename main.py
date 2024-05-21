import os
import glob

def nettoyer_fichiers_temp(dossier_temp):
    fichiers = glob.glob(os.path.join(dossier_temp, '*'))
    for fichier in fichiers:
        os.remove(fichier)
    print(f'{len(fichiers)} fichiers temporaires supprimés de {dossier_temp}')

dossier_temp = '/chemin/vers/dossier/temp'
nettoyer_fichiers_temp(dossier_temp)
