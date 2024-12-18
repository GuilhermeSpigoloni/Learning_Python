import tkinter as tk
from tkinter import ttk

raiz = tk.Tk()
raiz.title("Primeira Janela")
raiz.geometry("720x550")
quadro = ttk.Frame(raiz)
texto = ttk.Label(quadro, text="Olá")
texto.pack()

botao = ttk.Button(quadro, text="SAIR", command=raiz.destroy)
botao.pack()
quadro.pack(expand=True)
raiz.mainloop()