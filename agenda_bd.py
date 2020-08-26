import mysql.connector
	
def getConexao():
	conexao = mysql.connector.connect(user='root', password='admin', database='agenda2')
	return conexao

def cadastrar():
	nome = input('Digite o nome: ')
	telefone = input('Digite o telefone: ')
	
	hobbies = []
	id_hobbies = []
	while True:
		novoHobby = input('Novo hobby? (S/n)')
		if novoHobby == 'n':
			break
		listarHobbies()
		id_hobby = int(input('Informe o ID do Hobby ou 0 para novo: '))
		if id_hobby == 0:
			hobbies.append(input('Hobby: '))
		else:		
			id_hobbies.append(id_hobby)
			
	try:
		sql = 'INSERT INTO contatos (nome, telefone) VALUES (%s, %s)'
		sqlHobby = 'INSERT INTO hobbies (nome) VALUES (%s)'
		sqlRelacao = 'INSERT INTO contatos_has_hobbies (contatos_id, hobbies_id) VALUES (%s, %s)'
		
		conexao = getConexao()
		cursor = conexao.cursor()
		
		cursor.execute(sql, (nome, telefone))
		id_contato = cursor.lastrowid
		
		for hobby in hobbies:
			cursor.execute(sqlHobby, (hobby,))
			id_hobbies.append(cursor.lastrowid)
		
		for id_hobby in id_hobbies:
			cursor.execute(sqlRelacao, (id_contato, id_hobby))
		
		conexao.commit()
	except Exception as e:
		print('Error: {}'.format(e))
	finally:
		cursor.close()
		conexao.close()
	
def listar():
	print('\nLista de contatos: ')
	conexao = getConexao()
	cursor = conexao.cursor()

	sql = 'select * from contatos';
	cursor.execute(sql)
	for (id, nome, telefone) in cursor:
		print('{} - {}: {}'.format(id, nome, telefone))

	cursor.close()
	conexao.close()

def listarHobbies():
	print('Lista de hobbies: ')
	conexao = getConexao()
	cursor = conexao.cursor()

	sql = 'select * from hobbies';
	cursor.execute(sql)
	for (id, nome) in cursor:
		print('{} - {}'.format(id, nome))

	cursor.close()
	conexao.close()

	
def atualizar():
	while True:
		listar()
		id = input('Informe o ID a ser editado: ')
		
		conexao = getConexao()
		cursor = conexao.cursor()
		
		sql = 'SELECT * FROM contatos WHERE id=%s'
		cursor.execute(sql, (id,))
		try:
			id, nomeAntigo, telefoneAntigo = cursor.fetchone()
			break
		except:
			print('Registro não encontrado!')
		
	nome = input('Digite o novo nome [{}]: '.format(nomeAntigo))
	telefone = input('Digite o novo telefone [{}]: '.format(telefoneAntigo))
	if nome == '':
		nome = nomeAntigo
	if telefone == '':
		telefone = telefoneAntigo
		
	sqlUpdate = 'UPDATE contatos SET nome=%s, telefone=%s WHERE id=%s'
	try:
		cursor.execute(sqlUpdate, (nome, telefone, id))
		conexao.commit()
	except Exception as e:
		print('Error: {}'.format(e))
	finally:
		cursor.close()
		conexao.close()
	
def apagar():
	listar()
	id = input('Informe o ID a ser editado: ')
	
	conexao = getConexao()
	cursor = conexao.cursor()
	
	try:
		sql = 'DELETE FROM contatos WHERE id=%s'
		cursor.execute(sql, (id,))
		conexao.commit()
	except Exception as e:
		print('Erro! {}'.format(e))
	finally:
		cursor.close()
		conexao.close()
	
def detalhes():
	listar()
	id = input('Informe o ID para ver detalhes: ')

	conexao = getConexao()
	cursor = conexao.cursor()
	sql = 'SELECT * FROM contatos WHERE id=%s'
	sqlHobbies = 'SELECT h.* FROM hobbies h JOIN contatos_has_hobbies c ON c.hobbies_id=h.id WHERE contatos_id=%s'
	try:
		cursor.execute(sql, (id,))
		id, nome, telefone = cursor.fetchone()
		print('{} - {}: {}'.format(id, nome, telefone))
		print('Hobbies: ')
		cursor.execute(sqlHobbies, (id,))
		for idHobby, hobby in cursor:
			print('{} - {}'.format(idHobby, hobby))
	except Exception as e:
		print('Registro não encontrado! {}'.format(e))
	finally:
		cursor.close()
		conexao.close()
		
while True:
	print('\n1. Cadastrar')
	print('2. Listar')
	print('3. Atualizar')
	print('4. Apagar')
	print('5. Ver detalhes')
	print('6. Listar hobbies')
	print('7. Sair')
	opcao = int(input())
	if opcao == 1:
		cadastrar()
	elif opcao == 2:
		listar()
	elif opcao == 3:
		atualizar()
	elif opcao == 4:
		apagar()
	elif opcao == 5:
		detalhes()
	elif opcao == 6:
		listarHobbies()
	elif opcao == 7:
		break