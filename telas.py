from tkinter .ttk import *
from tkinter import *
from PIL import Image, ImageTk

#cores que estão sendo utilizadas na janela 
C_Azul = "#6e8faf"
C_Branco = "#feffff"
#configurando o titulo o tamanho e cor de fundo da janela
janela = Tk()
janela.title("Meu Acervo")
janela.geometry("800x360")
janela.configure(background=C_Branco)

style = Style(janela)
style.theme_use("clam")

cabecalho = Frame(janela, width=800, height=60, background=C_Azul, relief="flat")
cabecalho.grid(row=0, column=0, columnspan=2, sticky=NSEW)

janela.mainloop()
