import tkinter as tk

root = tk.Tk()
root.title("Ejercicio 10")
root.geometry("300x150")

scroll = tk.Scrollbar(root)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

texto = tk.Text(root, yscrollcommand=scroll.set)
texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scroll.config(command=texto.yview)

texto.insert(tk.END, "yujhieofnslnfslcohsdlelsouhefushcskjhhfshfolfhewlofhslofhslfhsleuhwolfhsufhlfhewloihfwoihfwlhflohwoiwfiowhndsjkfwjkhsffnlsefnlknfskjnfslkgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggnfslkfnsjkfnsjfnsjfnslkfsdjkslnfsknf.snflsknfdsknskjfsçbfhjskbfjskbfskjfbskjfksfksfksfksbfksjbfsjkfbskjbfsjbfskjhfskjbfkbsjfsbfiabfewbhfsakowhefufhufisfsufhsuifhsfhsiufsilfhsaiufhsiudfsiufdsilhdsufhsluhflsidhfsiulhfsluifslfslfsllfshadlshfd")

root.mainloop()
