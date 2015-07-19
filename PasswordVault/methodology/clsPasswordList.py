'''
Created on Jul 14, 2015

@author: Daniel Bruce
'''
from methodology.clsPasswordTuple import PasswordTuple

class PasswordList(object):
	'''
	classdocs
	'''

	def __init__(self):
		'''
		Constructor
		'''
		self.list = []
		#Given a vault string, this function will create a list
	
	def append(self, pPasswordTuple):
		if not isinstance(pPasswordTuple, PasswordTuple):
			raise TypeError("Argument passed into append function for PasswordList is not a PasswordTuple.")
		self.list.append(pPasswordTuple)
		
	def popByIdentifier(self, pIdentifier):
		for i, v in enumerate(self.list):
			if (v.identifier == pIdentifier):
				break
		return self.list.pop(i)
# 		next(obj for obj in self.list if obj.identifier==pIdentifier)
# 		x = [1, 2, 3, 4, 2, 2, 3]
# 		x[:] = (value for value in self.list if value.identifier() != pIdentifier)
# 		>>> x
# 		list(filter((2).__ne__, x)) #[1, 3, 3, 4]
# 		matches = [x for x in self.list if x.identifier() == pIdentifier]

	def hasIdentifier(self, pIdentifier):
		for i in self.list:
			if pIdentifier == i.identifer():
				return True
		return False

	def getIdentifierList(self):
		lclList = []
		for v in self.list:
			lclList.append(v.identifier())
		return lclList