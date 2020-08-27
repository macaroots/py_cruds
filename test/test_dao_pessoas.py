import test.test_dao
class TestDAOPessoas(test.test_dao.TestDAO):
	def getClasse(self):
		return test.test_dao.TestDAO.getClasse(self, 'dao.dao.DAOPessoasAbstrato')
