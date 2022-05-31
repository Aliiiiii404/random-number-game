# importer le module random
import random

# on import le module time pour gerer le temps
import time

# on import le module tikenter
import tkinter as tk
from random import randint, choice
from tkinter import *
from tkinter import Button, Label

# compteur de tentative
tentatives = 6

#recuperer le temps

temps = time.time()

color = "#900C3F"

color_2 = "#000"


# choisir un nombre entre 1 et 100
nombre_hasard=random.randint(1, 100)


#cree la fentre
fenetre = tk.Tk()
fenetre.title("Ali jeu de Chifre")
fenetre.geometry("1080x720")
fenetre.config(bg=color)

# boite frame
frame= tk.Frame(fenetre, bg="#900C3F")
frame.pack(expand=True)

while tentatives != 0 :
    # afficher le message de bienvenu
    def essai(event=None):

        global entree_proposition, nombre_hasard, tentatives, tentativestxtvar, infovar
        # reculter la proposition
        proposition = entree_proposition.get()
        #verefecation
        if proposition.isdigit():
                # transform de poroposition en entier
                # cast
                nombre_proposistion = int(proposition)

                # verifier si le numero est plus petit ou plus grands
                if nombre_proposistion < nombre_hasard:
                    infovar.set("C'est Plus")
                    nombre_proposistion = " "
                elif nombre_proposistion > nombre_hasard:
                    infovar.set("C'est Moins")
                    nombre_proposistion = " "
                elif nombre_proposistion == nombre_hasard:
                    infovar.set("Bravo ! Vous Avez gagner")

                tentatives -= 1
                tentativestxtvar.set(f"ATTENTION !! Vous avez :{tentatives}")

        else:
            infovar.set("Tu dois Entrer un Nombre!!")

        if tentatives == 0:
            infovar.set("C'est perdu ! trop de tentative, le nombre été :"f"{nombre_hasard}")
            time.sleep(1)
    # ajouter le button
    bouton = tk.Button(frame, text="Valider", font=("Arial", 25), command=essai, bg="purple", activebackground='royalblue', fg="white")
    bouton.pack()


    # ajouter une entrer pour ecrire
    entree_proposition = tk.Entry(frame)
    entree_proposition.bind('<Return>', essai)
    entree_proposition.focus()
    entree_proposition.pack()

    # afficher des information
    infovar = tk.StringVar(fenetre)
    infovar.set("Bonne chance")
    info = tk.Label(fenetre, textvariable=infovar,  font=("Arial", 25),fg=color_2)
    info.place(x=850, y=600)

    # variable stoker le nombre de tentative
    tentativestxtvar = tk.StringVar()
    tentativestxtvar.set("ATTENTION !! Vous avez :"f"{tentatives}")

    # afficher le nombre de tentatives
    tentativestxt = tk.Label(fenetre, textvariable=tentativestxtvar, bg=color_2, fg="white")
    tentativestxt.place(x=1000, y=20)

    #afficher la barre de menu
    menu_bar = Menu(fenetre)
    #premiere menu
    file_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_command(label="Exit", command=fenetre.quit, font=(50))
    menu_bar.add_command(label="Redemarer", font=(50))
    # confegurer la fenetre pour le menu bar
    fenetre.config(menu=menu_bar)

    # afficher la fentre
    fenetre.mainloop()
