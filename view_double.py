from glob import glob
import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog, ttk
import new_nuage as nn
import os

# Création de la fenêtre contenant les paramètres à entrer
fenetre = tk.Tk()
fenetre.geometry("310x190")
fenetre.title("Analyseur de Texte")

# Définition de deux variables globale qui contiendront les deux fichier d'entré
nameFile1 = ""
nameFile2 = ""

# Fonction affichant le nom du premier fichier sur l'interface graphique et affectation à la variable nameFile1
def showFile1():
    name = filedialog.askopenfilename(filetypes=[("Texte File", "*.txt")])
    aux = name.split(os.sep)
    aux1 = os.path.join(aux[0])
    x = aux1.split("/")
    newName = x[len(x)-1]
    tk.Label(text=newName).grid(row=5, column=1)
    global nameFile1
    nameFile1 = name

# Fonction affichant le nom du premier fichier sur l'interface graphique et affectation à la variable nameFile2
def showFile2():
    name = filedialog.askopenfilename(filetypes=[("Texte File", "*.txt")])
    aux = name.split(os.sep)
    aux1 = os.path.join(aux[0])
    x = aux1.split("/")
    newName = x[len(x)-1]
    tk.Label(text=newName).grid(row=6, column=1)
    global nameFile2
    nameFile2 = name

# Fonction de création du wordcloud après clic sur le bouton executer 
def executeProg():
    try:
        global nameFile1
        global nameFile2

        firstfile = nn.all_part_file(nameFile1)
        secondfile = nn.all_part_file(nameFile2)

        traitement_ff = []
        traitement_sf = []

        valeur = type_sortie.get()

        if (valeur == "Noms"):
                traitement_ff = nn.return_nouns(firstfile)
                traitement_sf = nn.return_nouns(secondfile)
        else:
                if (valeur == "Verbes"):
                        traitement_ff = nn.return_verbs(firstfile)
                        traitement_sf = nn.return_verbs(secondfile)
                else:
                        traitement_ff = nn.return_token(firstfile)
                        traitement_sf = nn.return_token(secondfile)

        clean1_ff = nn.cleaner(traitement_ff, nn.stopWords)
        clean2_ff = nn.cleaner(clean1_ff, nn.stoppeur)
        clean3_ff = nn.cleaner(clean2_ff, nn.last_stopwords)

        clean1_sf = nn.cleaner(traitement_sf, nn.stopWords)
        clean2_sf = nn.cleaner(clean1_sf, nn.stoppeur)
        clean3_sf = nn.cleaner(clean2_sf, nn.last_stopwords)

        fileff = "Texte/firstfile.txt"
        filesf = "Texte/secondfile.txt"

        nn.writer(fileff, clean3_ff)
        nn.writer(filesf, clean3_sf)

        r1 = nn.reader(fileff)
        r2 = nn.reader(filesf)

        nn.cloud_creator(r1, r2, int(nb_mots.get()), format_nuage.get(), forme_mots.get())
    
    except ValueError:
        tkinter.messagebox.showerror(
            'Erreur',
            f'Il y a un erreur dans les paramètres'
        )

# Création des différents bouton et label de l'interface graphique
tk.Label(text="Choisissez vos paramètres ci-dessous").grid(row=0, columnspan=2)

tk.Label(text="Nombre de mots maximum : ").grid(row=1, column=0)
nb_mots = tk.Entry()
nb_mots.insert(0,100)
nb_mots.grid(row=1, column=1)

tk.Label(text="Type de sortie : ").grid(row=2, column=0)
liste_sortie = ["Tout", "Noms", "Verbes"]
type_sortie = ttk.Combobox(fenetre, values=liste_sortie)
type_sortie.current(0)
type_sortie.grid(row=2, column=1)

tk.Label(text="Forme du nuage : ").grid(row=3, column=0)
liste_nuage = ["None", "feuille", "heart", "Papillion", "twitter"]
format_nuage = ttk.Combobox(fenetre, values=liste_nuage)
format_nuage.current(0)
format_nuage.grid(row=3, column=1)

tk.Label(text="Format des mots : ").grid(row=4, column=0)
liste_text = ["None", "HeyComic"]
forme_mots = ttk.Combobox(fenetre, values=liste_text)
forme_mots.current(0)
forme_mots.grid(row=4, column=1)

tk.Button(text="Choix premier fichier", command=showFile1).grid(row=5, column=0)

tk.Button(text="Choix second fichier", command=showFile2).grid(row=6, column=0)

tk.Button(text="Exécuter", command=executeProg).grid(row=7, columnspan=2)

fenetre.mainloop()
