import sqlite3 as lite

def connectDb():
    con = lite.connect('acervo.db')
    return con
#Funções que vão inserir os dados no banco de dados
def insertLivro(titulo,genero,autor,editora,ano_publicacao,isbn):
    con = connectDb()
    con.execute("INSERT INTO livros(titulo,genero,autor,editora,ano_publicacao,isbn) VALUES(?,?,?,?,?,?)",(titulo,genero,autor,editora,ano_publicacao,isbn))
    con.commit()
    con.close()

def insertQadrinhos(titulo,volume,volume_total,ano_publicacao,roteirista,desenhista,isbn):
    con = connectDb()
    con.execute("INSERT INTO quadrinhos(titulo,volume,volume_total,ano_publicacao,roteirista,desenhista,isbn) VALUES(?,?,?,?,?,?,?)",(titulo,volume,volume_total,ano_publicacao,roteirista,desenhista,isbn))
    con.commit()
    con.close()

def insert_lista_compra(titulo,volume,volume_total,ano_publicacao,roteirista,desenhista,valor_medio,isbn):
    con = connectDb()
    con.execute("INSERT INTO lista_compra(titulo,volume,volume_total,ano_publicacao,roteirista,desenhista,valor_medio,isbn) VALUES(?,?,?,?,?,?,?,?)",(titulo,volume,volume_total,ano_publicacao,roteirista,desenhista,valor_medio,isbn))
    con.commit()
    con.close()

#funções para consultar os itens nas tabelas
def consultar_livros():
    con = connectDb()
    livros = con.execute("SELECT * FROM livros").fetchall()
    con.close()

    if not livros:
        print("Não existe nenhum livro em seu acervo")
        return
    
    for livro in livros:
        print(f"id:{livro[0]}")
        print(f"titulo:{livro[1]}")
        print(f"genero:{livro[2]}")
        print(f"autor:{livro[3]}")
        print(f"editora:{livro[4]}")
        print(f"ano publicação:{livro[5]}")
        print(f"isbn:{livro[6]}")

def consultar_quadrinhos():
    con = connectDb()
    quadrinhos = con.execute("SELECT * FROM quadrinhos").fetchall()

    if not quadrinhos:
        print("nenhum quadrinho adicionado")
        return
    
    for quadrinho in quadrinhos:
        print(f"ID:{quadrinho[0]}")
        print(f"titulo:{quadrinho[1]}")
        print(f"volume:{quadrinho[2]}")
        print(f"volume total:{quadrinho[3]}")
        print(f"ano de publicação:{quadrinho[4]}")
        print(f"roteirista:{quadrinho[5]}")
        print(f"desenhista:{quadrinho[6]}")
        print(f"isbn:{quadrinho[7]}")

def consultar_lista_compra():
    con = connectDb()
    lista_compras = con.execute("SELECT * FROM lista_compra").fetchall()

    if not lista_compras:
        print("nenhuma intenção de compra")
        return
    
    for lista_compra in lista_compras:
        print(f"ID:{lista_compra[0]}")
        print(f"titulo:{lista_compra[1]}")
        print(f"volume:{lista_compra[2]}")
        print(f"volume total:{lista_compra[3]}")
        print(f"ano de publicação:{lista_compra[4]}")
        print(f"roteirista:{lista_compra[5]}")
        print(f"desenhista:{lista_compra[6]}")
        print(f"valor medio:{lista_compra[7]}")
        print(f"isbn:{lista_compra[8]}")
    
consultar_livros()
consultar_quadrinhos()
consultar_lista_compra()

def deletar_livros(id):
    con = connectDb()
    con.execute("DELETE * FROM livros WHERE id = ?", (id))
    con.commit()
    con.close()
