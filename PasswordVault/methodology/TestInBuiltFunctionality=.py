'''
Created on Jul 18, 2015

@author: Daniel Bruce
'''
import unittest

class TestInBuiltFunctionality(unittest.TestCase):


	def test_Doctorb(self):
		print("d" + chr(32) + "d")
		print(ord(" "))
		assert(ord(chr(32)) == 32)

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()