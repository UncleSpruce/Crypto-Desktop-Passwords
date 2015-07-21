'''
Created on Jul 18, 2015

@author: Daniel Bruce
'''
import unittest
import pickle

from methodology.clsBasicLabelledKeyGenerator import BasicLabelledKeyGenerator
# from methodology.clsBasicLabelledKey import BasicLabelledKey
from methodology.clsPasswordList import PasswordList
from methodology.clsPasswordTuple import PasswordTuple

def save_object(obj, filename):
	with open(filename, 'wb') as output:
		pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

class TestPickleWriter(unittest.TestCase):
	def test_FullFunctionality(self):
		print("Running FullFunctionality test for the TestPickleWriter.")
		
		x = BasicLabelledKeyGenerator()
		y = x.generate(PasswordList([]), PasswordTuple("RIdentifier", "RPassword"))		
		# sample usage
		save_object(y, 'sampleKey.pkl')
		
		
		

		
		
		print(y.encode())
		#lclJSON = json.decoder() 
		#lclJSON.decode("['foo', {'bar': ('baz', None, 1.0, 2)}]".encode('utf-8'))
		#print(lclJSON[0])


if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()