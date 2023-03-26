'''

NB-2023.03.22
LOtto számgenerátor , grafikai változat
'''
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import random

def rejtett_felirat():              #megjeleníteshez szükséges
    label_sorsolas.grid(row=0,column=0,columnspan=5, padx=10, pady=5)
    elvalaszto_vonal.grid(row=3, column=0, columnspan=5, padx=10, pady=5,sticky="ew") # elválasztó vonal helyének  meghatározása


def fogadas():
    te_szamaid = []
    for i in range(5):
        try:
            szam = int(entries[i].get())
            if szam < 1 or szam > 90:
                raise ValueError    #  HIBÁS éerék
            if szam in te_szamaid:   # megézi, hogy a SZAM érték megtalálható-e TE_SZAMAID halmazban
                raise ValueError
            te_szamaid.append(szam)  # ha igen Hibás értéket ad
        except ValueError:
            messagebox.showerror("Hiba", "Kérem, adjon meg 1 és 90 közötti egész számot, amely nem ismétlődik!")
            return

    print(te_szamaid)  # ellenőrzésként a terminálja is kiírja

    # ----------------- véletlen szám generátor ---------------------------------

    nyeroszamok = []   # nyerőszámok halmazának generálása

    while len(nyeroszamok) < 5:
        rand_num = random.randint(1, 90)
        if rand_num not in nyeroszamok:
            nyeroszamok.append(rand_num)
    print(nyeroszamok)

    a = len(set(te_szamaid).intersection(set(nyeroszamok)))

    if len(set(te_szamaid).intersection(set(nyeroszamok))) > 0:
        label2_result.config(text=f"Gratulálok, eltaláltál {a} számot", bg='goldenrod',fg="#006400")
    else:
        label2_result.config(text=f"Sajnos nem nyertél!", bg='goldenrod', fg='red')

    label5_result.config(text=f"A kisorsolt nyerőszámok: {' '.join(map(str, nyeroszamok))}", bg='goldenrod')


# ----------------------- GUI kód ------------------------------

root = tk.Tk()
root.title("LOTTO 5/90 fogadás")
root.geometry("500x250")          # Az ablak mérete
root.configure(bg='Goldenrod')   # A felület háttérszíne

label1_result = tk.Label(root, text="Adj meg 5 számot , 1 és 90 között", bg='Goldenrod', font=('Arial', 15))
label1_result.grid(row=0, column=0, columnspan=5, padx=10, pady=5)

entries = []
for i in range(5):
    entry = tk.Entry(root, width=3, borderwidth=2, justify="center", font=('Arial', 30))
    entry.grid(row=1, column=i, padx=5, pady=5)
    entries.append(entry)

button = tk.Button(root, text="\u2714  SORSOLÁS", command=lambda: [ fogadas() , rejtett_felirat() ])
button.grid(row=2, column=3, padx=5, pady=5)

exit_button = tk.Button(root, text="\u274c  Kilépés", command=root.quit)
exit_button.grid(row=2, column=1, padx=5, pady=5)

label_sorsolas = tk.Label(root, text="             S O R S O L Á S            ", bg='Goldenrod', font=('Arial', 15))

elvalaszto_vonal = ttk.Separator(root, orient='horizontal')


label2_result = tk.Label(root, text="", bg='Goldenrod', font=('Arial', 15))
label2_result.grid(row=4, column=0, columnspan=5, padx=10, pady=5)

label3_result = tk.Label(root, text="", bg='Goldenrod', font=('Arial', 15))
label3_result.grid(row=5, column=0, columnspan=5, padx=10, pady=5)

label5_result = tk.Label(root, text="", bg='Goldenrod', font=('Arial', 15))
label5_result.grid(row=5, column=0, columnspan=5, padx=10, pady=5)

root.mainloop()
