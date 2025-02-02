'''
Created on Jul 22, 2015

@author: Daniel Bruce
'''
import unittest
from functionality.clsProgramState import ProgramState

class TestProgramStateLoading(unittest.TestCase):

	def test_FullFunctionality(self):
		print("Running the FullFunctionality test for the TestProgramStateLoading.")
		
		self.define()
		
		mainState = ProgramState()
		mainState.openPickledVault("LocalVault.vlt")
		
		
		mainState.vault.toString()

	def define(self):
		self.lclpwd1 = PasswordTuple("Facebook", "q234")
		self.lclpwd2 = PasswordTuple("Google", "778")
		self.lclpwd3 = PasswordTuple("LinkedIn", "P324")
		self.lclpwd4 = PasswordTuple("Quora", "hjkhkg34")
		self.lclpwd5 = PasswordTuple("Foursquare", "hjkhksssssg34")
		self.lclpwd6 = PasswordTuple("Dutch Oven", "hjkhsddkg34")
		
		self.passwordListA0 = PasswordList([])
		
		self.passwordListA1 = PasswordList([])
		self.passwordListA1.append(self.lclpwd1)
		
		self.passwordListA2 = PasswordList([])
		self.passwordListA2.append(self.lclpwd1)
		self.passwordListA2.append(self.lclpwd2)
		
		self.passwordListA3 = PasswordList([])
		self.passwordListA3.append(self.lclpwd1)
		self.passwordListA3.append(self.lclpwd2)
		self.passwordListA3.append(self.lclpwd3)
		
		self.passwordListA4 = PasswordList([])
		self.passwordListA4.append(self.lclpwd1)
		self.passwordListA4.append(self.lclpwd2)
		self.passwordListA4.append(self.lclpwd3)
		self.passwordListA4.append(self.lclpwd4)
		
		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()