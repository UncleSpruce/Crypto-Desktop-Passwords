'''
Created on Jul 19, 2015

@author: Daniel Bruce
'''
import unittest
from methodology.clsSimpleKeyGenerator import SimpleKeyGenerator
from methodology.clsBasicLabelledKeyGenerator import BasicLabelledKeyGenerator
from methodology.clsPasswordTuple import PasswordTuple
from methodology.clsPasswordList import PasswordList

class testSimpleKeyGenerator(unittest.TestCase):

	def test_FullFunctionality(self):
		print("Running test_FullFunctionality test on test_SimpleKeyGenerator.")
		self.gen = SimpleKeyGenerator()
		
		lclpwd1 = PasswordTuple("Facebook", "q234")
		lclpwd2 = PasswordTuple("Google", "778")
		
		lclPasswordList1 = PasswordList([])
		lclPasswordList1.append(lclpwd1)
		lclPasswordList1.append(lclpwd2)
		
		#self.tryCombo(lclPasswordList1, PasswordTuple("LinkedIn", "Stormy"))
		#self.tryCombo(lclPasswordList1, PasswordTuple("Dutch Oven", "Stsssormy"))
		#self.tryCombo(lclPasswordList1, PasswordTuple("", "Sdsdsdtormy"))
		#self.tryCombo(lclPasswordList1, PasswordTuple("", "Sdsdsdtormy"))
		
		self.tryCombo(lclPasswordList1, "Stormy")
		self.tryCombo(lclPasswordList1, "Dutch Oven")
		self.tryCombo(lclPasswordList1, "Sdsdsdtormy")
		self.tryCombo(lclPasswordList1, "")
		
	def tryCombo(self, pInputList, pResult):
		lclKey = self.gen.generate(pInputList, pResult)
		print(lclKey.toString())
		self.assertEqual(pResult, lclKey.compute(pInputList))		
	
	def printAnEncoding(self, pInputList, pResult):
		lclKey = self.gen.generate(pInputList, pResult)
		print(lclKey.toString())

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.test_FullFunctionality']
	unittest.main()