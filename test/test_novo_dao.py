import test.test_dao
import dao.mongo

class TestNovo(test.test_dao.TestDAO):
	def getClasse(self):
		return dao.mongo.DAOPessoasMongo
				
