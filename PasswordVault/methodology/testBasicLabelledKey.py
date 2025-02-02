'''
Created on Jul 19, 2015

@author: Daniel Bruce
'''
import unittest

from methodology.clsBasicLabelledKeyGenerator import BasicLabelledKeyGenerator
from methodology.clsPasswordTuple import PasswordTuple
from methodology.clsPasswordList import PasswordList

class TestBasicLabelledKey(unittest.TestCase):

	def test_ComputeFunction(self):
		print("Running test_ComputeFunction for TestBasicLabelledKey.")
		self.subtest1()
		
	def subtest1(self):
		lclGen = BasicLabelledKeyGenerator()
		
		lclpwd1 = PasswordTuple("Facebook", "q234")
		lclpwd2 = PasswordTuple("Google", "778")
		lclpwd3 = PasswordTuple("LinkedIn", "P324")
		lclPasswordList = PasswordList([])
		
		lclPasswordList.append(lclpwd1)
		lclPasswordList.append(lclpwd2)
		
		lclKey = lclGen.generate(lclPasswordList, lclpwd3)
		
		#lclpwd4 = PasswordTuple("Quora", "Pdd324")
		#lclPasswordList.append(lclpwd4)
		
		lclComputed = lclKey.computeReturnTuple(lclPasswordList)
		print("Printed Map.")
		print(lclComputed.toString())
		self.assertEqual(lclComputed.password(), lclpwd3.password())
		
	def subtest2(self):
		# This test tries to use the key's map when the wrong password is given.
		
		lclGen = BasicLabelledKeyGenerator()
		
		lclpwd1 = PasswordTuple("Facebook", "q234")
		lclpwd2 = PasswordTuple("Google", "778")
		lclpwd3 = PasswordTuple("LinkedIn", "P324")
		lclPasswordList = PasswordList([])
		
		lclPasswordList.append(lclpwd1)
		lclPasswordList.append(lclpwd2)
		
		lclKey = lclGen.generate(lclPasswordList, lclpwd3)
		
		lclpwd4 = PasswordTuple("Quora", "Pdd324")
		lclPasswordList.append(lclpwd4)
		
		lclComputed = lclKey.computeReturnTuple(lclPasswordList)
		print("Printed Map.")
		print(lclComputed.toString())
		self.assertEqual(lclComputed.password(), lclpwd3.password())	
		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.test_ComputeFunction']
	unittest.main()