'''
Created on Jul 23, 2015

@author: Daniel Bruce
'''
import unittest
from methodology.clsSimpleVault import SimpleVault
from methodology.clsPasswordTuple import PasswordTuple
from methodology.clsPasswordList import PasswordList
from methodology.clsBasicBigIntGenerator import BasicBigIntGenerator
from functionality.clsPivotedVault import PivotedVault
from functionality.clsOpenableVault import OpenableVault
from functionality.clsProgramPasswordData import ProgramPasswordData
from methodology.clsGenericLabelledKey import GenericLabelledKey
from methodology.clsSimpleLabelledKeyGenerator import SimpleLabelledKeyGenerator
from functionality.clsFactoryProgramPasswordData import FactoryProgramPasswordData
from functionality.clsPicklingMethodology import PicklingMethodology
from testcommons.clsDefinitions import Definitions


class TestUseSavedVault(unittest.TestCase):
	def test_FullFunctionality(self):
		
		self.data = Definitions()
		self.pickler = PicklingMethodology()
		
		lclVaultXX = self.pickler.getVaultFromFile("ExampleVault.vlt")
		print(lclVaultXX.toString())
		lclResults = lclVaultXX.recover(self.data.passwordListA3)
		print(lclResults)
# 
# 	def define(self):
# 		self.gen = SimpleLabelledKeyGenerator()
# 		self.pickler = PicklingMethodology()
# 		
# 		self.lclpwd1 = PasswordTuple("Facebook", "q234")
# 		self.lclpwd2 = PasswordTuple("Google", "778")
# 		self.lclpwd3 = PasswordTuple("LinkedIn", "P324")
# 		self.lclpwd4 = PasswordTuple("Quora", "hjkhkg34")
# 		self.lclpwd5 = PasswordTuple("Foursquare", "hjkhksssssg34")
# 		self.lclpwd6 = PasswordTuple("Dutch Oven", "hjkhsddkg34")
# 
# 		self.lclpwd1d = PasswordTuple("Facebook", "q234 Duplicated")
# 		self.lclpwd2d = PasswordTuple("Google", "778 Duplicated")
# 		self.lclpwd3d = PasswordTuple("LinkedIn", "P324 Duplicated")
# 		self.lclpwd4d = PasswordTuple("Quora", "hjkhkg34 Duplicated")
# 		self.lclpwd5d = PasswordTuple("Foursquare", "hjkhksssssg34 Duplicated")
# 		self.lclpwd6d = PasswordTuple("Dutch Oven", "hjkhsddkg34 Duplicated")
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

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()