import mysql.connector
from medicosRepository import MedicosRepository

medicosRepository = MedicosRepository('10.1.1.109', 'admin', 'admin', 'BD')

def inserir():
  nome = input('Nome: ')
  crm = int(input('CRM: '))

  conexao = mysql.connector.connect(
    host="10.1.1.109",
    user="admin",
    password="admin",
    database="BD"
  )

  cursor = conexao.cursor()

  sql = "INSERT INTO medicos (nome, crm) VALUES (%s, %s)"
  valores = (nome, crm)
  print(sql)
  cursor.execute(sql, valores)

  conexao.commit()

  print(cursor.rowcount, "record inserted.")
  print(f'Inserido novo registro #{cursor.lastrowid}')

def listar():

  conexao = mysql.connector.connect(
    host="10.1.1.109",
    user="admin",
    password="admin",
    database="BD"
  )

  cursor = conexao.cursor()

  cursor.execute("SELECT * FROM medicos")

  registros = cursor.fetchall()

  print('ID\tNome\tCRM')
  for id, nome, crm in registros:
    print(f'{id}\t{nome}\t{crm}')

def listar_por_nome():
  nome = input('Nome: ')

  conexao = mysql.connector.connect(
    host="10.1.1.109",
    user="admin",
    password="admin",
    database="BD"
  )

  cursor = conexao.cursor()

  cursor.execute("SELECT * FROM medicos WHERE nome like %s", [f'%{nome}%'])

  registros = cursor.fetchall()

  print('ID\tNome\tCRM')
  for id, nome, crm in registros:
    print(f'{id}\t{nome}\t{crm}')

def listar_por_id():
  id = input('ID: ')

  id, nome, crm = medicosRepository.listarPorId(id)

  print(f'{id}\t{nome}\t{crm}')

def alterar():
  id = int(input('ID: '))
  id, nome, crm = medicosRepository.listarPorId(id)
  novo_nome = input(f'Nome [{nome}]: ')
  if novo_nome == '':
     novo_nome = nome
  novo_crm = int(input(f'CRM [{crm}]: '))

  total_registros = medicosRepository.alterar(novo_nome, novo_crm, id)

  print(total_registros, "registro alterado.")

def apagar():
  id = int(input('ID: '))

  conexao = mysql.connector.connect(
    host="10.1.1.109",
    user="admin",
    password="admin",
    database="BD"
  )

  cursor = conexao.cursor()

  sql = "DELETE FROM medicos WHERE id=%s"
  valores = (id,)
  cursor.execute(sql, valores)

  conexao.commit()

  print(cursor.rowcount, "registro apagado.")

while True:
    print('1. Cadastrar')
    print('2. Listar')
    print('3. Alterar')
    print('4. Apagar')
    print('5. Listar por nome')
    print('6. Listar por id')
    print('7. Sair')
    opcao = int(input())
    if opcao == 1:
        inserir()
    elif opcao == 2:
        listar()
    elif opcao == 5:
        listar_por_nome()
    elif opcao == 6:
        listar_por_id()
    elif opcao == 3:
        listar()
        alterar()
    elif opcao == 4:
        listar()
        apagar()
    elif opcao == 7:
        print('tchau')
        break