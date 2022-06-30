import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog, ttk
import concat

# Création de la fenêtre de l'interface graphique
fenetre = tk.Tk()
fenetre.geometry("280x120")
fenetre.title("Concaténer")

# Tableau global qui contiendra tous les fichiers à traiter
tabFiles = []

# Fonction de sélection des fichiers à traiter
def openAllFiles():
    name = filedialog.askopenfilenames(filetypes=[("Texte File", "*.txt")])
    global tabFiles
    tabFiles = name

# Fonction appelant la fonction de concaténation du fichier concat.py pour aasembler les fichiers sélectionnés 
def concatAll():
    try:
        global tabFiles
        concat.concatenation(tabFiles, nom_sortie.get()) # Appel de la fonction concatenation du fichier concat pour assembler les fichiers
        tkinter.messagebox.showinfo(
            'Succès',
            f'La concaténation a bien été réalisé. Vous trouverez le fichier '+nom_sortie.get()+'.txt dans le répertoire Fichier_concat'
        )
    except ValueError:
        tkinter.messagebox.showerror(
            'Erreur',
            f'Un ou plusieurs fichier(s) sélectionné(s) n\'est pas traitable.'
        )

# Création des différents bouton et label contenu dans la fenêtre d'affichage
tk.Button(text="Choix fichiers", command=openAllFiles).grid(row=0, column=0)

tk.Label(text="Nom fichier sortie : ").grid(row=1, column=0)
nom_sortie = tk.Entry()
nom_sortie.insert(0,"Concatenation")
nom_sortie.grid(row=1, column=1)

tk.Button(text="Concaténer", command=concatAll).grid(row=2, column=0)

fenetre.mainloop()
