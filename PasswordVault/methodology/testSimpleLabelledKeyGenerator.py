'''
Created on Jul 20, 2015

@author: Daniel Bruce
'''
import unittest
from methodology.clsSimpleKeyGenerator import SimpleKeyGenerator
from methodology.clsBasicLabelledKeyGenerator import BasicLabelledKeyGenerator
from methodology.clsPasswordTuple import PasswordTuple
from methodology.clsPasswordList import PasswordList
from methodology.clsSimpleLabelledKeyGenerator import SimpleLabelledKeyGenerator

class testSimpleLabelledKeyGenerator(unittest.TestCase):

	def test_FullTest(self):
		print("Running FullTest on testSimpleLabelledKeyGenerator.")
		self.gen = SimpleLabelledKeyGenerator()
		
		lclpwd1 = PasswordTuple("Facebook", "q234")
		lclpwd2 = PasswordTuple("Google", "778")
		lclpwd3 = PasswordTuple("LinkedIn", "Stormy")
		lclpwd4 = PasswordTuple("Dutch Oven", "Stsssormy")
		lclpwd5 = PasswordTuple("", "Sdsdsdtormy")
		lclpwd6 = PasswordTuple("Lawrence's Password", "Sdsdsdtormy")
		
		lclPasswordList1 = PasswordList([])
		lclPasswordList1.append(lclpwd1)
		lclPasswordList1.append(lclpwd2)
				
		self.tryBasicMapping(lclPasswordList1, lclpwd3)
		self.tryBasicMapping(lclPasswordList1, lclpwd4)
		self.tryBasicMapping(lclPasswordList1, lclpwd5)
		self.tryBasicMapping(lclPasswordList1, lclpwd6)
		
		self.sampleWrongInput1()
		#self.tryCombo(lclPasswordList1, "Stormy")
		#self.tryCombo(lclPasswordList1, "Dutch Oven")
		#self.tryCombo(lclPasswordList1, "Sdsdsdtormy")
		#self.tryCombo(lclPasswordList1, "")
		
	def tryBasicMapping(self, pInputList, pResult):
		lclKey = self.gen.generate(pInputList, pResult)
		print(lclKey.toString())
		self.assertEqual(pResult.password(), lclKey.compute(pInputList))		

	def sampleWrongInput1(self):
		lclpwd1 = PasswordTuple("Facebook", "q234")
		lclpwd2 = PasswordTuple("Google", "778")
		lclpwd3 = PasswordTuple("LinkedIn", "Stormy")
		lclpwd4 = PasswordTuple("Dutch Oven", "Stsssormy")
		
		lclPasswordList1 = PasswordList([])
		lclPasswordList1.append(lclpwd1)
		lclPasswordList1.append(lclpwd2)
		
		lclKey = self.gen.generate(lclPasswordList1, lclpwd4)
		
		lclPasswordList1.popByIdentifier(lclpwd1)
		lclResult = lclKey.compute(lclPasswordList1)
		print(lclResult)
		
		self.assertEqual(lclResult, -1)
		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()