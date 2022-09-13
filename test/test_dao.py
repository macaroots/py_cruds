import unittest
#import dao
from importlib import import_module
		
class TestDAO(unittest.TestCase):
	def __init__(self, testName):
		super(TestDAO, self).__init__(testName) 
		#unittest.TestCase.__init__(self, testName)
		self.candidato = self.getClasse()
		print('Testando {}'.format(self.candidato))
		
	def getClasse(self, class_str='dao.dao.DAOPessoasAbstrato'):
		try:
			module_path, class_name = class_str.rsplit('.', 1)
			module = import_module(module_path)
			return getattr(module, class_name)
		except (ImportError, AttributeError) as e:
			raise ImportError(class_str)
			
	def setUp(self):
		self.dao = self.candidato()
		self.dao.criaDB()

	def tearDown(self):
		self.dao.apagaDB()
		del self.dao
		
	def test_list(self):
		lista = self.dao.lista()
		self.assertIsInstance(lista, [].__class__)
	
	def test_insert_list(self):		
		lista = self.dao.lista()
		p = ['Ana', '123']
		novoId = self.dao.insere(p)
		listaDepois = self.dao.lista()
		self.assertIsInstance(novoId, int)
		self.assertTrue(len(listaDepois) > len(lista))
		self.assertIn(p, listaDepois)
		#print(p, listaDepois, p in listaDepois)
		
	def test_get_id(self):
		pessoas = [['Bela', '321'], ['Carla', '123']]
		ids = []
		for p in pessoas:
			id = self.dao.insere(p)
			ids.append(id)
			
		#print(self.dao.lista())
		for j, id in enumerate(ids):
			p = pessoas[j]
			p2 = self.dao.getById(id)
		
			#print(p, p2, p == p2)
			self.assertEqual(p, p2)
			for i, v in enumerate(p):
				self.assertEqual(p[i], p2[i])

if __name__ == '__main__':	
	unittest.main()
