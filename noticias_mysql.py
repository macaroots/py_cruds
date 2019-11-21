import mysql.connector

def getConexao():
	conexao = mysql.connector.connect(
		host='localhost',
		user='root',
		password='admin',
		database='noticias'
	)
	return conexao

def cadastrarCategoria():
	nome = input('Categoria: ')
	conexao = getConexao()
	cursor = conexao.cursor()
	sql = 'insert into categorias (nome) values (%s)'
	cursor.execute(sql, (nome,))
	id = cursor.lastrowid
	conexao.commit()
	cursor.close()
	conexao.close()
	print('Cadastro realizado com sucesso!')
	return id

def alterarCategoria():
	listarCategorias()
	id = int(input('Id: '))
	conexao = getConexao()
	cursor = conexao.cursor()
	sql = 'select * from categorias where id=%s'
	cursor.execute(sql, (id, ))
	id, nome = cursor.fetchone()
	novoNome = input('Categoria [{}]: '.format(nome))
	if novoNome == '':
		novoNome = nome
	sql = 'update categorias set nome=%s where id=%s'
	cursor.execute(sql, (novoNome, id))
	conexao.commit()
	cursor.close()
	conexao.close()
	print('Alteração realizada com sucesso!')

def listarCategorias():
	conexao = getConexao()
	cursor = conexao.cursor()
	sql = 'select * from categorias;'
	cursor.execute(sql)
	linhas = cursor.fetchall()
	cursor.close()
	conexao.close()
	print('Categorias:')
	for id, nome in linhas:
		print('{}: {}'.format(id, nome))
	
def cadastrarNoticia():
	listarCategorias()
	try:
		conexao = getConexao()
		cursor = conexao.cursor()
		id = int(input('Categoria: '))
		if id == 0:
			nome = input()
			sql = 'insert into categorias (nome) values (%s)'
			# como não tem commit, se der erro ao incluir a notícia, cancela a categoria
			cursor.execute(sql, (nome,))
			id = cursor.lastrowid
		titulo = input('Título: ')
		sql = 'insert into noticias (titulo, categorias_id) values (%s, %s)'
		cursor.execute(sql, (titulo, id))
		conexao.commit()
		print('Cadastro realizado com sucesso!')
	except Exception as e:
		print('Erro: {}!'.format(e))
	finally:
		cursor.close()
		conexao.close()
	
def listarNoticias():
	conexao = getConexao()
	cursor = conexao.cursor()
	sql = '''select n.*, c.nome from noticias n
 join categorias c on c.id=n.categorias_id'''
	cursor.execute(sql)
	linhas = cursor.fetchall()
	cursor.close()
	conexao.close()
	print('Notícias:')
	for id, titulo, texto, data, idCategoria, categoria in linhas:
		print('{}: ({}) {}'.format(id, categoria, titulo))

while True:
	print('1. Cadastrar categoria')
	print('2. Listar categorias')
	print('3. Cadastrar notícia')
	print('4. Listar notícias')
	print('5. Alterar categoria')
	print('6. Sair')
	opcao = int(input())
	if opcao == 6:
		break
	elif opcao == 1:
		cadastrarCategoria()
	elif opcao == 2:
		listarCategorias()
	elif opcao == 3:
		cadastrarNoticia()
	elif opcao == 4:
		listarNoticias()
	elif opcao == 5:
		alterarCategoria()