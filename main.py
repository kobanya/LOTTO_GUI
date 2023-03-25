'''

NB-2023.03.22
LOtto számgenerátor , grafikai változat
'''
import tkinter as tk
import random


def fogadas():
    te_szamaid = []
    for i in range(5):
        te_szamaid.append(int(entries[i].get()))
    print(te_szamaid)

    # ----------------- véletlen szám generátor ---------------------------------

    nyeroszamok = []

    while len(nyeroszamok) < 5:
        rand_num = random.randint(1, 90)
        if rand_num not in nyeroszamok:
            nyeroszamok.append(rand_num)
    print(nyeroszamok)

    a=len(set(te_szamaid).intersection(set(nyeroszamok)))

    if len(set(te_szamaid).intersection(set(nyeroszamok))) > 0:
        label2_result.config(text=f"Gratulálok, eltaláltál {a} számot", bg='goldenrod')
    else:
        label2_result.config(text=f"Sajnos nem nyertél!", bg='goldenrod')

    label1_result.config(text=f"A kisorsolt nyerőszámok: {' '.join(map(str, nyeroszamok))}", bg='goldenrod')


# ----------------------- GUI kód ------------------------------

root = tk.Tk()
root.title("LOTTO 5/90 fogadás")
root.geometry("500x250")
root.configure(bg='Goldenrod')

entries = []
for i in range(5):
    entry = tk.Entry(root, width=3, borderwidth=2, justify="center", font=('Arial', 30))
    entry.grid(row=0, column=i, padx=5, pady=5)
    entries.append(entry)

button = tk.Button(root, text="\u2714  FOGADÁS", command=fogadas)
button.grid(row=1, column=3, padx=5, pady=5)

exit_button = tk.Button(root, text="\u274c  Kilépés", command=root.quit)
exit_button.grid(row=1, column=1, padx=5, pady=5)


label1_result = tk.Label(root, text="",bg='Goldenrod',font=('Arial', 15))
label1_result.grid(row=3, column=0, columnspan=5, padx=10, pady=5 )

label2_result = tk.Label(root, text="",bg='Goldenrod',font=('Arial', 15))
label2_result.grid(row=4, column=0, columnspan=5, padx=10, pady=5 )

root.mainloop()
