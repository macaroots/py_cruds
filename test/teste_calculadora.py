import unittest

class Calculadora():
	def sum(self, numeros):
		soma = 0
		for n in numeros:
			soma += n
		return soma


class TestSum(unittest.TestCase):
	def setUp(self):
		self.calculadora = Calculadora()

	def tearDown(self):
		#
		# tearDown is called once after each test
		#
		print('tearDown')
		
	def test_operacoes(self):
		with self.subTest(operacao=1):
			self.assertEqual(self.calculadora.sum([1, 2, 43]), 6, "Should be 6")
		with self.subTest(operacao=2):
			self.assertEqual(self.calculadora.sum([1, 2, 2]), 6, "Should be 6")
			
		
		
	def test_sum(self):
		self.assertEqual(self.calculadora.sum([1, 2, 3]), 6, "Should be 6")

	def test_sum_tuple(self):
		self.assertEqual(self.calculadora.sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
	unittest.main()