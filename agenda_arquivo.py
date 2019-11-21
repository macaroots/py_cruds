'''
anotar dados
	nome, telefone, idade, lazer, curso, semestre
'''
	
def cadastrar():
	print('Nome: ')
	nome = input()
	print('Tel: ')
	telefone = input()

	arq = open('teste.csv', 'r+')
	arq.seek(5, 0)
	arq.write('{},{}'.format(nome, telefone))
	arq.close()
	
def getLista():
	arq = open('teste.csv', 'r')
	linhas = arq.read().split('\n')
	arq.close()
	return linhas

def listar():
	linhas = getLista()
	print('Nome\t\tTelefone')
	for linha in linhas:
		nome, telefone = linha.split(',')
		print('{}\t\t{}'.format(nome, telefone))
		
def procurar():
	achou = False
	procura = input('Nome: ')
	linhas = getLista()
	print('Nome\t\tTelefone')
	for linha in linhas:
		nome, telefone = linha.split(',')
		if nome == procura:
			print('{}\t\t{}'.format(nome, telefone))
			achou = True
	if not achou:
		print('Não achou')
	
		
while True:
	print('\n\n1. Cadastrar')
	print('2. Listar')
	print('3. Procurar')
	print('4. Sair')
	opcao = int(input())
	if opcao == 1:
		cadastrar()
	elif opcao == 2:
		listar()
	elif opcao == 3:
		procurar()
	else:
		break