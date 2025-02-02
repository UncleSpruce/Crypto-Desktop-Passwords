'''
Created on Jul 19, 2015

@author: Daniel Bruce
'''
import unittest
import copy
from methodology.clsBasicLabelledKeyGenerator import BasicLabelledKeyGenerator
from methodology.clsPasswordTuple import PasswordTuple
from methodology.clsPasswordList import PasswordList
from methodology.clsVault import Vault
from methodology.clsBasicRecovery import BasicRecovery

class TestRecoveryList(unittest.TestCase):

	def test_FullFunctionality(self):
		print("Running FullFunctionality test for TestRecoveryList.")
		self.sample1()

	def sample1(self):
		lclVault = Vault()
		lclRecover = BasicRecovery()
		
		lclpwd1 = PasswordTuple("Facebook", "q234")
		lclpwd2 = PasswordTuple("Google", "778")
		lclpwd3 = PasswordTuple("LinkedIn", "P324")
		lclpwd4 = PasswordTuple("Quora", "hjkhkg34")
		
		lclPasswordList1 = PasswordList([])
		lclPasswordList1.append(lclpwd1)
		lclPasswordList1.append(lclpwd2)
		
		lclGen = BasicLabelledKeyGenerator()
		lclKey = lclGen.generate(lclPasswordList1, lclpwd3)
		lclVault.append(lclKey)
		
		lclPasswordList2 = copy.copy(lclPasswordList1)
		lclKey2 = lclGen.generate(lclPasswordList2, lclpwd4)
		lclVault.append(lclKey2)
		
		lclRecoveredList1 = lclVault.recover(lclPasswordList1)#lclRecover.recoverList(lclVault, lclPasswordList1)
		print(lclRecoveredList1.toString())
		
		lclPasswordList1.popByIdentifier("Facebook")
		lclRecoveredList2 = lclVault.recover(lclPasswordList1)#lclRecover.recoverList(lclVault, lclPasswordList1)
		print(lclRecoveredList2.toString())
		
		#self.assertEqual(lclComputed.password(), lclpwd3.password())		
		
		#lclComputed = lclKey.computeReturnTuple(lclPasswordList, lclPasswordList)
		
		
		
		#print(lclComputed.password())
		#self.assertEqual(lclComputed.password(), lclpwd3.password())
		#pass
	
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()