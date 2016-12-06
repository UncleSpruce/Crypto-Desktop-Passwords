'''
Created on Jul 17, 2015

@author: Daniel Bruce
'''
import unittest
from methodology.clsBasicHash import BasicHash
from methodology.clsBasicStringIntConverter import BasicStringIntConverter

class TestHash(unittest.TestCase):

	# 2015-07-17 http://www.convertstring.com/Hash/SHA512 states HashSHA512("") = 64D24560970CA14D349BEA0E7D2526D4754BF3283568AB4DD602BD79EB454DC3657D5BB6F9A30C90EA98D9600EBD0FB45D582F4CAE3F8E3C50B0E8FB18059892
	def test_BasicCase(self):
		#lclTempString = self.stringIntConverter.toString(pArgument + self.salt)
		#print(lclTempString)
		
		lclHash = BasicHash()
		lclConverter = BasicStringIntConverter()
		lclInt = lclConverter.toInt("")
		lclResultInt = lclHash.compute(hex(lclInt))
		print(lclResultInt)
		
		#assert()
		#lclHash = BasicHash()
		#print(lclHash.compute(0))

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main() 