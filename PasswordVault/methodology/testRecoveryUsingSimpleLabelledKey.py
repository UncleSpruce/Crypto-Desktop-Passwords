'''
Created on Jul 20, 2015
@author: Daniel Bruce
'''

import unittest
import copy
from methodology.clsSimpleLabelledKeyGenerator import SimpleLabelledKeyGenerator
from methodology.clsPasswordTuple import PasswordTuple
from methodology.clsPasswordList import PasswordList
from methodology.clsSimpleVault import SimpleVault
from testcommons.clsDefinitions import Definitions

class testRecoveryUsingSimpleLabelledKey(unittest.TestCase):
	def test_FullFunctionality(self):
		print("Running FullFunctionality test for testRecoveryUsingSimpleLabelledKey.")
		self.data = Definitions()
		
		self.sample1()
		self.sample2()
		self.sample3()
		self.sample4()
		self.sample5()
		return

	def sampleOutcome(self, pVault, pInputList, pExpected = -1):
		lclRecoveredList = pVault.recover(pInputList)
		
		print(lclRecoveredList)
		if pExpected != -1:
			self.assertEqual(lclRecoveredList, pExpected)
		return
	
	def sample1(self):
		vault = SimpleVault()
		print(vault.toString())
		vault.append(self.data.key12t3)
		vault.append(self.data.key123t4)
		vault.append(self.data.key123t4)
		#print(vault.toString())
		self.sampleOutcome(vault, self.data.passwordListA2, self.data.passwordListA4)	
		return
	
	def sample2(self):
		vault = SimpleVault()
		print(vault.toString())
		vault.append(self.data.key123t4)
		#print(vault.toString())
		self.sampleOutcome(vault, self.data.passwordListA2, self.data.passwordListA2)
		return
	
	def sample3(self):
		vault = SimpleVault()
		print(vault.toString())
		vault.append(self.data.key12t3)
		#print(vault.toString())
		self.sampleOutcome(vault, self.data.passwordListA0, self.data.passwordListA0)
		return
	
	def sample4(self):
		vault = SimpleVault()
		print(vault.toString())
		vault.append(self.data.key12t3)
		vault.append(self.data.key12t5)
		#print(vault.toString())
		self.sampleOutcome(vault, self.data.passwordListA2, self.data.passwordListX)
		return

	def sample5(self):
		vault = SimpleVault()
		print(vault.toString())
		vault.append(self.data.key12t3)
		vault.append(self.data.key12t5)
		#print(vault.toString())
		self.sampleOutcome(vault, self.data.passwordListA1, self.data.passwordListA1)
		return
			
# 	def defineInputs(self):
# 		self.gen = SimpleLabelledKeyGenerator()
# 		
# 		self.lclpwd1 = PasswordTuple("Facebook", "q234")
# 		self.lclpwd2 = PasswordTuple("Google", "778")
# 		self.lclpwd3 = PasswordTuple("LinkedIn", "P324")
# 		self.lclpwd4 = PasswordTuple("Quora", "hjkhkg34")
# 		self.lclpwd5 = PasswordTuple("Foursquare", "hjkhksssssg34")
# 		self.lclpwd6 = PasswordTuple("Dutch Oven", "hjkhsddkg34")
# 		
# 		self.passwordListA0 = PasswordList([])
# 		
# 		self.passwordListA1 = PasswordList([])
# 		self.passwordListA1.append(self.lclpwd1)
# 		
# 		self.passwordListA2 = PasswordList([])
# 		self.passwordListA2.append(self.lclpwd1)
# 		self.passwordListA2.append(self.lclpwd2)
# 		
# 		self.passwordListA3 = PasswordList([])
# 		self.passwordListA3.append(self.lclpwd1)
# 		self.passwordListA3.append(self.lclpwd2)
# 		self.passwordListA3.append(self.lclpwd3)
# 		
# 		self.passwordListA4 = PasswordList([])
# 		self.passwordListA4.append(self.lclpwd1)
# 		self.passwordListA4.append(self.lclpwd2)
# 		self.passwordListA4.append(self.lclpwd3)
# 		self.passwordListA4.append(self.lclpwd4)
# 		
# 		self.passwordListA5 = PasswordList([])
# 		self.passwordListA5.append(self.lclpwd1)
# 		self.passwordListA5.append(self.lclpwd2)
# 		self.passwordListA5.append(self.lclpwd3)
# 		self.passwordListA5.append(self.lclpwd4)
# 		self.passwordListA5.append(self.lclpwd5)
# 		
# 		self.passwordListA6 = PasswordList([])
# 		self.passwordListA6.append(self.lclpwd1)
# 		self.passwordListA6.append(self.lclpwd2)
# 		self.passwordListA6.append(self.lclpwd3)
# 		self.passwordListA6.append(self.lclpwd4)
# 		self.passwordListA6.append(self.lclpwd5)
# 		self.passwordListA6.append(self.lclpwd6)
# 		
# 		self.passwordListB4 = PasswordList([])
# 		self.passwordListB4.append(self.lclpwd4)
# 		self.passwordListB4.append(self.lclpwd5)
# 		
# 		self.passwordListB5 = PasswordList([])
# 		self.passwordListB5.append(self.lclpwd4)
# 		
# 		self.passwordListX = PasswordList([])
# 		self.passwordListX.append(self.lclpwd1)
# 		self.passwordListX.append(self.lclpwd2)
# 		self.passwordListX.append(self.lclpwd3)
# 		self.passwordListX.append(self.lclpwd5)
# 		
# 		self.key12t3 = self.gen.generate(self.passwordListA2, self.lclpwd3)
# 		self.key123t4 = self.gen.generate(self.passwordListA3, self.lclpwd4)
# 		self.key12t5 = self.gen.generate(self.passwordListA2, self.lclpwd5)
	

	
# 	def sample1(self):
# 		
# 		lclPasswordList1 = PasswordList([])
# 		lclPasswordList1.append(self.lclpwd1)
# 		lclPasswordList1.append(self.lclpwd2)
# 		
# 		
# 		lclKey = self.gen.generate(lclPasswordList1, self.lclpwd3)
# 		print(lclKey)
# 		print(lclKey.toString())
# 		lclVault.append(lclKey)
# 		
# 		#lclPasswordList2 = copy.copy(lclPasswordList1)
# 		lclKey2 = self.gen.generate(lclPasswordList1, self.lclpwd4)
# 		lclVault.append(lclKey2)
# 		
# 		lclRecoveredList1 = lclVault.recover(lclPasswordList1)#lclRecover.recoverList(lclVault, lclPasswordList1)
# 		print(lclRecoveredList1.toString())
# 		
# 		lclPasswordList1.popByIdentifier("Facebook")
# 		lclRecoveredList2 = lclVault.recover(lclPasswordList1)#lclRecover.recoverList(lclVault, lclPasswordList1)
# 		print(lclRecoveredList2.toString())

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()