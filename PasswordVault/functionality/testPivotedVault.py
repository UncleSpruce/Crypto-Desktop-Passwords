'''
Created on Jul 22, 2015
@author: Daniel Bruce 
'''

import unittest
from methodology.clsSimpleVault import SimpleVault
from methodology.clsPasswordTuple import PasswordTuple
from methodology.clsPasswordList import PasswordList
from methodology.clsBasicBigIntGenerator import BasicBigIntGenerator
from functionality.clsPivotedVault import PivotedVault
from testcommons.clsDefinitions import Definitions

class TestPivotedVault(unittest.TestCase):
	def test_FullFunctionality(self):
		print("Running the FullFunctionality test for the TestPivotedVault.")
		self.data = Definitions()
		
		print("Variables defined.")
		vault = PivotedVault()
		print("1:" + vault.toString())
		vault.addOutput(self.data.lclpwd6)
		print("2:" + vault.toString())
		vault.addOutput(self.data.lclpwd5)
		print("3:" + vault.toString())
		vault.addInputList(self.data.passwordListA1)
		print("4:" + vault.toString())
		vault.addInputList(self.data.passwordListA2)
		print("5:" + vault.toString())
		vault.addInputList(self.data.passwordListA3)
		print("6:" + vault.toString())
		vault.addInputList(self.data.passwordListA4)
		print("7:" + vault.toString())
		vault.removeOutput(self.data.lclpwd5)
		print("8:" + vault.toString())
		vault.removeOutput(self.data.lclpwd2)
		print("9:" + vault.toString())
		vault.removeInputList(self.data.passwordListA1)
		print("10:" + vault.toString())
		vault.removeInputList(self.data.passwordListA1)
		print("11:" + vault.toString())	

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()