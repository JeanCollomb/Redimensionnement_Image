"""
Script Python permettant de redimensionner l'ensemble des images
présentes dans le dossier de travail.

@author: Jean Collomb
"""

###############################################################################
###----> Importation packages

from os import getcwd, listdir
from os.path import isfile, join, splitext
from PIL import Image

###############################################################################
###----> Methode

resize_method = Image.ANTIALIAS
    #Image.NEAREST)  # use nearest neighbour
    #Image.BILINEAR) # linear interpolation in a 2x2 environment
    #Image.BICUBIC) # cubic spline interpolation in a 4x4 environment
    #Image.ANTIALIAS) # best down-sizing filter

###############################################################################
###----> Parametres
    
max_hauteur     = 1080                                                          # Hauteur maximal de l'image finale
max_largeur     = 1920                                                          # Largeur maximal de l'image finale
extensions      = ['JPG', 'PNG', 'BMP']                                        # Extensions des images à modifier (mettre en MAJUSCULE)
ajout_nom       = '_500px'                                                     # Ajout d'une info pour renommer le fichier

###############################################################################
###----> Fonction

#dossier= os.path.abspath(".")
dossier         = getcwd()                                                     # Chemin du dossier de travail
liste_fichiers  = listdir(dossier)                                             # Liste des fichiers dans le dossier

def adjustement_taille(largeur,hauteur):
    
    if largeur>max_largeur or hauteur>max_hauteur:
        if largeur>hauteur:
            return max_largeur, int (max_largeur * hauteur/ largeur)
        else:
            return int (max_hauteur*largeur/hauteur), max_hauteur
    else:
        return largeur,hauteur

###############################################################################
###----> Programme
        
if __name__ == "__main__":
    
    for fichier in liste_fichiers:                                             # Boucle sur les fichiers du dossier
        
        if isfile(join(dossier,fichier)):                                      # Si le "fichier" est bien un fichier (et non un temporaire ...)
            f_text, f_ext= splitext(fichier)                                   # Récupération du nom et de l'extension du fichier
            f_ext = f_ext[1:].upper()                                          # Mise en majuscule de l'extension du fichier et retrait du point
            
            if f_ext in extensions:
                nouveau_nom = f_text + ajout_nom + '.' + f_ext

                image = Image.open(join(dossier,fichier))                      # Ouverture de l'image
                largeur, hauteur= image.size                                   # Récupération des dimensions
                
                if largeur > max_largeur and hauteur > max_hauteur:            # Si le fichier est à redimensionner
                    image = image.resize(adjustement_taille(largeur, hauteur)) # Redimensionnement
                    image.save(join(dossier,nouveau_nom))                      # Sauvegarde
                    print ('Fichier :', nouveau_nom, ': Done !')

###############################################################################
###############################################################################