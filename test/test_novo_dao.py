import unittest
import test.test_crud

class CrudPessoasBD:
	def __init__(self):
		pass
		
	def criaDB(self, nome=None):
		pass
		
	def apagaDB(self):
		pass
		
	def lista(self):
		pass
		
	def insere(self, pessoa):
		pass
		
	def getById(self, id):
		return self.lista()[id]

class TestNovo(test.test_crud.TestCrud):
	def getClasse(self):
		return CrudPessoasBD
				