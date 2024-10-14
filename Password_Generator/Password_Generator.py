import random
import string
import tkinter as tk
from tkinter import messagebox

def generer_adgangskode(min_længde, inkluder_tal=True, inkluder_specialtegn=True):
    # Definerer mulige tegn til adgangskoden
    bogstaver = string.ascii_letters
    cifre = string.digits
    specialtegn = string.punctuation

    # Opretter en samling af tegn baseret på brugerens valg
    tegnsamling = bogstaver
    if inkluder_tal:
        tegnsamling += cifre
    if inkluder_specialtegn:
        tegnsamling += specialtegn

    adgangskode = ""
    krav_opfyldt = False
    har_tal = False
    har_specialtegn = False

    # Genererer adgangskoden, indtil kravene er opfyldt
    while not krav_opfyldt or len(adgangskode) < min_længde:
        nyt_tegn = random.choice(tegnsamling)
        adgangskode += nyt_tegn

        # Tjekker om der er inkluderet tal og specialtegn
        if nyt_tegn in cifre:
            har_tal = True
        elif nyt_tegn in specialtegn:
            har_specialtegn = True
        
        # Opdaterer kravstatus
        krav_opfyldt = True
        if inkluder_tal:
            krav_opfyldt = har_tal
        if inkluder_specialtegn:
            krav_opfyldt = krav_opfyldt and har_specialtegn

    return adgangskode

def generer():
    try:
        # Henter brugerens input og genererer en adgangskode
        min_længde = int(entry_længde.get())
        har_tal = var_tal.get()
        har_specialtegn = var_special.get()
        adgangskode = generer_adgangskode(min_længde, har_tal, har_specialtegn)
        
        # Viser den genererede adgangskode i indtastningsfeltet
        entry_adgangskode.delete(0, tk.END)
        entry_adgangskode.insert(0, adgangskode)
    except ValueError:
        # Håndterer fejl, hvis input ikke er et gyldigt tal
        messagebox.showerror("Fejl", "Indtast venligst et gyldigt tal for længden.")

def kopier():
    # Kopierer den genererede adgangskode til udklipsholderen
    adgangskode = entry_adgangskode.get()
    if adgangskode:
        root.clipboard_clear()
        root.clipboard_append(adgangskode)
        messagebox.showinfo("Kopieret", "Adgangskoden er kopieret til udklipsholderen.")
    else:
        messagebox.showwarning("Ingen adgangskode", "Generer venligst en adgangskode først.")

# Opretter hovedvinduet for applikationen
root = tk.Tk()
root.title("Adgangskode Generator")

# Sætter vinduets størrelse og gør det ikke resizable
root.geometry("300x300")
root.resizable(False, False)

# Indtastningsfelter og kontroller
tk.Label(root, text="Indtast minimum længde:").pack(pady=5)
entry_længde = tk.Entry(root)
entry_længde.pack(pady=5)

var_tal = tk.BooleanVar()
tk.Checkbutton(root, text="Inkluder tal", variable=var_tal).pack(pady=5)

var_special = tk.BooleanVar()
tk.Checkbutton(root, text="Inkluder specialtegn", variable=var_special).pack(pady=5)

# Knap til at generere adgangskoden
tk.Button(root, text="Generer Adgangskode", command=generer).pack(pady=10)

# Viser den genererede adgangskode
tk.Label(root, text="Genereret adgangskode:").pack(pady=5)
entry_adgangskode = tk.Entry(root)
entry_adgangskode.pack(pady=5)

# Knap til at kopiere adgangskoden
tk.Button(root, text="Kopier Adgangskode", command=kopier).pack(pady=10)

# Starter Tkinter-hovedløkken
root.mainloop()
