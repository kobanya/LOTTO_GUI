'''

NB-2023.03.22
LOtto számgenerátor , grafikai változat
'''

import tkinter as tk
import random


def get_numbers():
    numbers = []
    for i in range(5):
        numbers.append(int(entries[i].get()))
    print(numbers)

    # ----------------- véletlen szám generátor ---------------------------------

    nyeroszamok = []

    while len(nyeroszamok) < 5:
        rand_num = random.randint(1, 90)
        if rand_num not in nyeroszamok:
            nyeroszamok.append(rand_num)
    print(nyeroszamok)
    label1_result.config(text=f"A kisorsolt nyerőszámok: {nyeroszamok}", bg='goldenrod')

root = tk.Tk()
root.title("LOTTO 5/90 fogadás")
root.geometry("450x250")
root.configure(bg='Goldenrod')

entries = []
for i in range(5):
    entry = tk.Entry(root, width=3, borderwidth=2, justify="center", font=('Arial', 30))
    entry.grid(row=0, column=i, padx=5, pady=5)
    entries.append(entry)

button = tk.Button(root, text="FOGADÁS", command=get_numbers)
button.grid(row=1, column=2, padx=5, pady=5)


label1_result = tk.Label(root, text="",bg='Goldenrod',font=('Arial', 15))
label1_result.grid(row=3, column=0, columnspan=5, padx=10, pady=5 ) # columnspan 5-re állítása megakadályozza, hogy a kiírásnál elmozduljon a sor.

root.mainloop()
