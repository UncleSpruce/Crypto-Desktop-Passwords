'''
Created on Jul 21, 2015

@author: Daniel Bruce
'''
import unittest

class TestList(unittest.TestCase):
	def test_FullFunctionality(self):
		print("List Test")
		lt = list()
		print(lt)

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()