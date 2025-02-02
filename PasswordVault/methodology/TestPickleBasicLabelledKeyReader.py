'''
Created on Jul 18, 2015

@author: Daniel Bruce
'''
import unittest
import pickle
import pprint
from methodology.clsPasswordList import PasswordList

class TestPickleBasicLabelledKeyReader(unittest.TestCase):
	def test_FullFunctionality(self):
		print("Running FullFunctionality test for the TestPickleBasicLabelledKeyReader.")
		
		pkl_file = open('sampleKey.pkl', 'rb')

		key1 = pickle.load(pkl_file)
		print(key1.encode())
		print(key1.compute(PasswordList([])))
		#pprint.pprint(data1)
		
		
		pkl_file.close()
	
	


if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.test_FullFunctionality']
	unittest.main()