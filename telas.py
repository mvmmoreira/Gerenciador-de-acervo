from tkinter .ttk import *
from tkinter import *
from PIL import Image, ImageTk

#cores que estão sendo utilizadas na janela 
C_Azul = "#6e8faf"
C_Branco = "#feffff"
#configurando o titulo o tamanho e cor de fundo da janela
janela = Tk()
janela.title("Meu Acervo")
janela.geometry("770x330")
janela.configure(background = C_Branco)

style = Style(janela)
style.theme_use("clam")

#configurando as imagens
#imagem do logo
logo_img = Image.open("icons/logo.jpg")
logo_img = logo_img.resize((40,40))
logo_img = ImageTk.PhotoImage(logo_img)

#imagem botão adicionar livro
add_livro_img = Image.open("icons/lotr.jpg")
add_livro_img = add_livro_img.resize(18,18)
add_livro_img = ImageTk.PhotoImage(add_livro_img)

#imagem botão adicionar quadrinho
add_quadrinho_img = Image.open("icons/lanterna.jpg")
add_quadrinho_img = add_quadrinho_img.resize(18,18)
add_quadrinho_img = ImageTk.PhotoImage(add_quadrinho_img)

#imagem botão deletar livro
del_livro_img = Image.open("icons/naruto.jpg")
del_livro_img = add_livro_img.resize(18,18)
del_livro_img = ImageTk.PhotoImage(add_livro_img)

#configurando as partes da tela 
cabecalho = Frame(janela, width=770, height=50, background=C_Azul, relief="flat")
cabecalho.grid(row=0, column=0, columnspan=2, sticky=NSEW)

#menu
menu_lateral = Frame(janela, width=150, height=265, background=C_Azul, relief="solid")
menu_lateral.grid(row = 1, column=0, sticky=NSEW)

principal = Frame(janela, width=600, height=265, background=C_Branco, relief="raised")
principal.grid(row=1, column=1, sticky=NSEW)

app_logo = Label(cabecalho, image=logo_img, width=1000, compound=LEFT, padx=5, anchor=NW, background=C_Azul, fg=C_Branco)
app_logo.place(x=5, y=0)

app_logo_texto = Label(cabecalho, text="Acerco", compound=LEFT, padx=5, anchor=NW, font="Verdana 15 bold",background=C_Azul, fg=C_Branco)
app_logo_texto.place(x=50, y=7)

#botões do menu

janela.mainloop()
