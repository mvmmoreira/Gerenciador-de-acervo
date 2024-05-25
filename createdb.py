#importando o sqlite como banco de dados
import sqlite3 as lite

#criando o banco e criando a conexão com o bando de dados acervo
def connectDb():
    con = lite.connect('acervo.db')
    return con

def cria_tabela_quadrinhos():
    con = connectDb()
    con.execute("CREATE TABLE quadrinhos(\
                    id INTEGER PRIMARY KEY AUTOINCREMENT,\
                    titulo VARCHAR(50) NOT NULL,\
                    volume INT NOT NULL,\
                    volume_total INT NOT NULL,\
                    ano_publicacao DATE NOT NULL,\
                    roteirista VARCHAR(50) NOT NULL,\
                    desenhista VARCHAR(50) NOT NULL,\
                    isbn VARCHAR(13) NOT NULL)")
    con.commit()
    con.close()

def cria_tabela_livros():
    con = connectDb()
    con.execute("CREATE TABLE livros(\
                    id INTEGER PRIMARY KEY AUTOINCREMENT,\
                    titulo VARCHAR(50) NOT NULL,\
                    genero VARCHAR(50) NOT NULL,\
                    autor VARCHAR(50) NOT NULL,\
                    editora VARCHAR(50) NOT NULL,\
                    ano_publicacao DATE NOT NULL,\
                    isbn VARCHAR(13) NOT NULL)")
    con.commit()
    con.close()


def cria_Lista_Crompra():
    con = connectDb()
    con.execute("CREATE TABLE lista_Compra(\
                    id INTEGER PRIMARY KEY AUTOINCREMENT,\
                    titulo VARCHAR(50) NOT NULL,\
                    volume INT NOT NULL,\
                    volume_total INT NOT NULL,\
                    ano_publicacao DATE NOT NULL,\
                    roteirista VARCHAR(50) NOT NULL,\
                    desenhista VARCHAR(50) NOT NULL,\
                    valor_medior DECIMAL,\
                    isbn VARCHAR(13) NOT NULL)")
    con.commit()
    con.close()

cria_tabela_quadrinhos()
cria_tabela_livros()
cria_Lista_Crompra()



