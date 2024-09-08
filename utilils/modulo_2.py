from datetime import datetime
import psycopg2 as ps2
from dotenv import load_dotenv
import os

load_dotenv() # OK!

DB_DATA = os.getenv('DB_DATA')
DB_USER = os.getenv('DB_USER')
DB_PASSW = os.getenv('DB_PASSW')
DB_LOCAL = os.getenv('DB_LOCAL')
BD_PORT = os.getenv('BD_PORT')

# Funcao pegar hora do login
def pegar_hora(user):
    hora = datetime.now()
    f_hora = hora.strftime('%H:%M:%S')

    dma = datetime.now()
    f_dma = dma.strftime('%d/%m/%Y')

    try:
        conn = ps2.connect(
            database= DB_DATA,
            user= DB_USER,
            password= DB_PASSW,
            host= DB_LOCAL ,
            port= BD_PORT
        )

        cursor = conn.cursor()

        comamndSQL = "INSERT INTO login (nome, hora, dia) VALUES (%s, %s, %s)"
        cursor.execute(comamndSQL, (user, f_hora, f_dma))

        conn.commit()
        conn.close()

    except Exception as er3:
        return er3

# Teste de conexao
def teste_conect():
    conn = ps2.connect(
            database= DB_DATA,
            user= DB_USER,
            password= DB_PASSW,
            host= DB_LOCAL ,
            port= BD_PORT
        )
    
    if conn.status == 1:
        return True
    else:
        return False

# Acesso ao sistema
def acesso_ao_sistema(user, passw):
    try:
        load_dotenv()
        USER_NAME = os.getenv('USER_NAME')
        USER_PASSWORD = os.getenv('USER_PASSWORD')

        if user == USER_NAME and passw == USER_PASSWORD:
            return True
        else:
            return False
                
    except Exception as er:
        return er

# Adicionar novo cliente
class Cliente:
    def __init__(self, nome, email, senha, tell):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tell = tell

    def add_cliente(self):
            conn = ps2.connect(
                database= DB_DATA,
                user= DB_USER,
                password= DB_PASSW,
                host= DB_LOCAL ,
                port= BD_PORT
            )
    
            try: 
                cursor = conn.cursor()

                comamndSQL = "INSERT INTO clientes (nome, email, senha, tell) VALUES (%s, %s, %s, %s)"

                cursor.execute(comamndSQL, (self.nome, self.email, self.senha, self.tell))

                conn.commit()
                conn.close()

                res = f'{self.nome}, adicioonado com sucesso!'
                return res

            except Exception as er:
                return er
        

# Procurar Clientes
def procuar_clientes(id):
    conn = ps2.connect(
                database= DB_DATA,
                user= DB_USER,
                password= DB_PASSW,
                host= DB_LOCAL ,
                port= BD_PORT
            )
    
    cursor = conn.cursor()
    comamndSQL = "SELECT * FROM clientes WHERE id_cliente = %s"
    try:
        cursor.execute(comamndSQL, (id,))
        cliente =  cursor.fetchone()
        if cliente:
            return cliente
        else:
            conn.close()
            return False
    except:
        conn.close()
        return False

# Deletar Cliente
def deletar_cliente(id):
    conn = ps2.connect(
                database= DB_DATA,
                user= DB_USER,
                password= DB_PASSW,
                host= DB_LOCAL ,
                port= BD_PORT
            )
    
    cursor = conn.cursor()

    comamndSQL = "DELETE FROM clientes WHERE id_cliente = %s;"
    try:
        cursor.execute(comamndSQL,(id))
        
        conn.commit()
        conn.close()
        return True
    
    except Exception as erx:
        conn.close()
        return erx

# Atualizar Cliente
def atualizar_cliente(id, nome, email, senha, tell):
    conn = ps2.connect(
                database= DB_DATA,
                user= DB_USER,
                password= DB_PASSW,
                host= DB_LOCAL ,
                port= BD_PORT
            )
    
    cursor = conn.cursor()

    comamndSQL = "UPDATE clientes SET nome = %s, email = %s, senha = %s, tell = %s WHERE id_cliente = %s;"

    try:
        cursor.execute(comamndSQL,(nome, email, senha, tell, id))

        conn.commit()
        conn.close()
        return True
    except Exception as er:
        conn.close()
        return er
