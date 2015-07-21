'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''
import unittest

from methodology.clsBasicLabelledKeyGenerator import BasicLabelledKeyGenerator
from methodology.clsPasswordTuple import PasswordTuple
from methodology.clsPasswordList import PasswordList

class TestBasicLabelledKeyGenerator(unittest.TestCase):
	def test_FullFunctionality(self):
		print("Running FullFunctionality test on TestBasicLabelledKeyGenerator.")
		
		lclpwd1 = PasswordTuple("Facebook", "q234")
		lclpwd2 = PasswordTuple("Google", "778")
		lclPasswordList = PasswordList([])
		lclPasswordList.append(lclpwd1)
		lclPasswordList.append(lclpwd2)		
		self.printAnEncoding(lclPasswordList, PasswordTuple("LinkedIn", "Stormy"))
		
	def printAnEncoding(self, pInputList, pResult):
		lclGen = BasicLabelledKeyGenerator()
		lclKey = lclGen.generate(pInputList, pResult)
		print(lclKey.encode())
		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.test_BasicKeyGenerator']
	unittest.main()