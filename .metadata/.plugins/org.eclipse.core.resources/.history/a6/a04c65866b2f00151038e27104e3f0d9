'''
Created on Jul 17, 2015

@author: Owner
'''
import unittest
from methodology.clsPasswordTuple import PasswordTuple
from methodology.clsPasswordList import PasswordList


class TestPasswordList(unittest.TestCase):


	def test_FullFunctionality(self):
		print("Running test Full Functionality in TestPasswordList")
		pwd1 = PasswordTuple("Facebook", "224")
		pwd2 = PasswordTuple("Google", "onion32")
		plist = PasswordList()
		plist.append(pwd1)
		plist.append(pwd2)
		assert(plist.popByIdentifier("Google").password() == "onion32")


if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.test_FullFunctionality']
	unittest.main()