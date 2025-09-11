import os
import mysql.connector
from medicosRepository import MedicosRepository
from especialidadesRepository import EspecialidadesRepository

# print(os.environ)
# print(os.environ['host'])
# print(os.environ['user'])
# print(os.environ['password'])
# print(os.environ['database'])
host = '10.1.1.109'
user = 'admin'
password = 'admin'
database = 'BD'

medicosRepository = MedicosRepository(host, user, password, database)
especialidadesRepository = EspecialidadesRepository(host, user, password, database)

def inserir():
  nome = input('Nome: ')
  crm = int(input('CRM: '))

  conexao = mysql.connector.connect(
    host=os.environ['host'],
    user=os.environ['user'],
    password=os.environ['password'],
    database=os.environ['database']
  )

  cursor = conexao.cursor()

  sql = "INSERT INTO medicos (nome, crm) VALUES (%s, %s)"
  valores = (nome, crm)
  print(sql)
  cursor.execute(sql, valores)

  conexao.commit()

  print(cursor.rowcount, "record inserted.")
  print(f'Inserido novo registro #{cursor.lastrowid}')

def listar_medicos():

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

def listar_medicos_especialidades():
  medicos = medicosRepository.listarComEspecialidades()

  print('Médico\tEspecialidade')
  for medico, especialidade in medicos:
      print(f'{medico}\t{especialidade}')

def listar_especialidades():
  especialidades = especialidadesRepository.listar()

  print('ID\tNome')
  for id, nome in especialidades:
      print(f'{id}\t{nome}')

while True:
    print('1. Cadastrar médicos')
    print('2. Listar médicos')
    print('3. Alterar médicos')
    print('4. Apagar médicos')
    print('5. Listar médicos por nome')
    print('6. Listar médicos por id')
    print('7. Listar médicos com especialidades')
    print('8. Listar especialidades')
    print('9. Sair')
    opcao = int(input())
    if opcao == 1:
        inserir()
    elif opcao == 2:
        listar_medicos()
    elif opcao == 5:
        listar_por_nome()
    elif opcao == 6:
        listar_por_id()
    elif opcao == 3:
        listar_medicos()
        alterar()
    elif opcao == 4:
        listar_medicos()
        apagar()
    elif opcao == 7:
        listar_medicos_especialidades()
    elif opcao == 8:
        listar_especialidades()
    elif opcao == 9:
        print('tchau')
        break