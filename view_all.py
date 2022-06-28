import tkinter as tk
import os

# Création de la fenêtre de gestionnaire
fenetre = tk.Tk()
fenetre.geometry("250x80")
fenetre.title("Gestionnaire")

# Fonction affichant la fenêtre pour la concaténation
def appelConcat():
    os.system("python3.9 view_concat.py")

# Fonction affichant la fenêtre pour la création de nuages de mots
def appelNuage():
    os.system("python3.9 view_double.py")

# Fonction de fermeture de la fenêtre
def closeFenetre():
    fenetre.destroy()

# Création des différents boutons contenus dans la fenêtre
tk.Button(text="Concatener Fichiers", command=appelConcat).grid(row=0, column=0)

tk.Button(text="Créer Nuage", command=appelNuage).grid(row=1, column=0)

tk.Button(text="Fermer", command=closeFenetre).grid(row=2, column=0)

fenetre.mainloop()
