import mysql.connector

class MedicosRepository:
    def __init__(self, host, usuario, senha, banco):
        self.host = host
        self.usuario = usuario
        self.senha = senha
        self.banco = banco

    def conectar(self):
        conexao = mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.senha,
            database=self.banco
        )
        return conexao
    
    def listarPorId(self, id):
        conexao = self.conectar()

        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM medicos WHERE id = %s", [id])

        registro = cursor.fetchone()

        return registro
    
    def alterar(self, nome, crm, id):
        conexao = self.conectar()

        cursor = conexao.cursor()

        sql = "UPDATE medicos SET nome=%s, crm=%s WHERE id=%s"
        valores = (nome, crm, id)
        cursor.execute(sql, valores)

        conexao.commit()

        return cursor.rowcount