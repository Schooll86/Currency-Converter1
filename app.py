import tkinter as tk, requests, json, os

file="cur.json"; hist=[]

def convert():
    s=float(e.get())
    fr,to=v1.get(),v2.get()
    r=requests.get(f"https://api.exchangerate-api.com/v4/latest/{fr}").json()
    res=s*r["rates"][to]
    lb.insert(tk.END,f"{s} {fr} = {res:.2f} {to}")
    hist.append(res)

root=tk.Tk()
e=tk.Entry(root); e.pack()

v1=tk.StringVar(value="USD")
v2=tk.StringVar(value="EUR")

tk.OptionMenu(root,v1,"USD","EUR","RUB").pack()
tk.OptionMenu(root,v2,"USD","EUR","RUB").pack()

tk.Button(root,text="Конвертировать",command=convert).pack()
lb=tk.Listbox(root); lb.pack()

root.mainloop()
