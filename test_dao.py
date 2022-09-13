import unittest
import test.test_dao_pessoas
suite = unittest.TestLoader().loadTestsFromModule(test.test_dao_pessoas)
unittest.TextTestRunner().run(suite) 
