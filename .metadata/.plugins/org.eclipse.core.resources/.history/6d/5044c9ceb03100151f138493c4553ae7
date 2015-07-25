'''
Created on Jul 22, 2015

@author: Owner
'''
import unittest
from functionality.clsProgramState import ProgramState
from methodology.clsPasswordTuple import PasswordTuple
from methodology.clsPasswordList import PasswordList
from methodology.clsBasicBigIntGenerator import BasicBigIntGenerator

class TestProgramStateSaving(unittest.TestCase):
	def test_MainFunctionality(self):
		print("Running the MainFunctionality test for the TestProgramStateSaving.")
		mainState = ProgramState()
		self.define()
		print("Variables defined.")
		print("1:" + mainState.vault.toString())
		mainState.vault.addOutput(self.lclpwd6)
		print("2:" + mainState.vault.toString())
		mainState.vault.addOutput(self.lclpwd5)
		print("3:" + mainState.vault.toString())
		mainState.vault.addInputList(self.passwordListA1)
		print("4:" + mainState.vault.toString())
		mainState.vault.addInputList(self.passwordListA2)
		print("5:" + mainState.vault.toString())
		mainState.vault.addInputList(self.passwordListA3)
		print("6:" + mainState.vault.toString())
		mainState.vault.addInputList(self.passwordListA4)
		print("7:" + mainState.vault.toString())
		mainState.vault.removeOutput(self.lclpwd5)
		print("8:" + mainState.vault.toString())
		mainState.vault.removeOutput(self.lclpwd2)
		print("9:" + mainState.vault.toString())
		mainState.vault.removeInputList(self.passwordListA1)
		print("10:" + mainState.vault.toString())
		mainState.vault.removeInputList(self.passwordListA1)
		print("11:" + mainState.vault.toString())
		mainState.savePickledVault("LocalVault.vlt")
	
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
	#import sys;sys.argv = ['', 'Test.testProgramState']
	unittest.main()