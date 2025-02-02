'''
Created on Jul 19, 2015

@author: Daniel Bruce
'''
import unittest
from methodology.clsBasicLabelledKeyGenerator import BasicLabelledKeyGenerator
from methodology.clsPasswordTuple import PasswordTuple
from methodology.clsPasswordList import PasswordList
from methodology.clsVault import Vault
from methodology.clsBasicLabelledKey import BasicLabelledKey

class TestVault(unittest.TestCase):
	def test_FullFunctionality(self):
		print("Running FullFunctionality Test For TestVault.")
		self.sample1()

	def sample1(self):
		lclVault = Vault()
		lclGen = BasicLabelledKeyGenerator()
		
		lclpwd1 = PasswordTuple("Facebook", "q234")
		lclpwd2 = PasswordTuple("Google", "778")
		lclpwd3 = PasswordTuple("LinkedIn", "P324")
		lclpwd4 = PasswordTuple("Quora", "hjkhkg34")
		
		lclPasswordList1 = PasswordList([])
		lclPasswordList1.append(lclpwd1)
		lclPasswordList1.append(lclpwd2)

		lclPasswordList2 = PasswordList([])
		lclPasswordList2.append(lclpwd1)

		lclPasswordList3 = PasswordList([])
		lclPasswordList3.append(lclpwd4)
		
		lclKey1 = lclGen.generate(lclPasswordList1, lclpwd3)
		lclKey2 = lclGen.generate(lclPasswordList2, lclpwd4)
		
		lclVault.append(lclKey1)
		lclVault.append(lclKey2)

		print("Vault contents: ")
		print(lclVault.toString())
		
		#assert(isinstance(lclKey2, BasicLabelledKey))
		lclResultList1 = lclVault.recover(lclPasswordList2)
		lclResultList2 = lclVault.recover(lclPasswordList1)
		
		print("Recovery from Google Password: ")
		print(lclResultList1.toString())
		#print("Recovery from Facebook Password: ")
		#print(lclVault.recover(lclPasswordList2).toString())
		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()