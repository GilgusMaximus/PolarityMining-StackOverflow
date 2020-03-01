import tkinter as tk
from random import randint
from random import seed
from datetime import datetime
import csv as csv
from tkinter import ttk

rows = []
nameFile = open("./presentation.csv", "r", encoding="utf8")

reader = csv.reader(nameFile, delimiter=',')

for row in reader:
    c = row[0].replace("$", "\n")
    row[0] = c
    rows.append(row)

seed(datetime.now())

user_values = []
vader_values_all = []
vader_values_avg = []

#create window
window = tk.Tk()
greeting = tk.Label(text=rows[0][0],
                    width = 100,
                    height = 30,
                    font=("Arial", 15))
greeting.pack()

entry = tk.Entry( width=10, font=("Arial", 15))
entry.pack()

padding = tk.Label(width = 80,
                    height = 2)
padding.pack()

button = tk.Button(
    text="Submit",
    width=25,
    height=5
)
button.pack()

#padding3 = tk.Label(width = 80,
       #             height = 2)
#padding3.pack()



#pressing submit button
def handle_click(event):
    if len(rows) != 0:
        print("The button was clicked!")
        user_values.append(float(entry.get()))
        vader_values_all.append(rows[0][16])
        vader_values_avg.append(rows[0][12])
        entry.config(text='')
        entry.delete(0, len(entry.get()))
        rows.pop(0)
    if len(rows) != 0:
        greeting.config(text=rows[0][0])
    else:
        style = ttk.Style()
        style.configure("Treeview", font=("Arial, 15"))
        style.configure("Treeview.Heading", font=("Arial, 15"))
        treeview = ttk.Treeview(window, columns=["id", "our", "all", "avg"])
        treeview.heading("id", text="TextId")
        treeview.heading("our", text="Our estimation")
        treeview.heading("all", text="Vader All")
        treeview.heading("avg", text="Vader Avg")

        treeview.pack()
        button.destroy()
        greeting.destroy()
        entry.destroy()
        for i in range(len(vader_values_avg)-1, -1, -1):
            treeview.insert('', '0', "item12"+str(i), values=(str(i), str(user_values[i]), str(vader_values_all[i]), str(vader_values_avg[i])))



button.bind("<Button-1>", handle_click)
window.mainloop()