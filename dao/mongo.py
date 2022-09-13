import dao.dao
import copy

class DAOPessoasMongo(dao.dao.DAOPessoasAbstrato):
	def __init__(self):
		pass
		
	def criaDB(self):
		self.pessoas = []
		
	def apagaDB(self):
		del self.pessoas
		
	def lista(self):
		return copy.deepcopy(self.pessoas)
		
	def insere(self, pessoa):
		self.pessoas.append(pessoa)
		return len(self.pessoas) - 1
		
	def getById(self, id):
		return self.lista()[id]
