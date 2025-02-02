'''
Created on Jul 14, 2015

@author: Daniel Bruce
'''
from methodology.clsPasswordTuple import PasswordTuple
import copy

#obselete class

class PasswordList(object):
	'''
	classdocs
	'''

	def __init__(self, pNewList = None):
		'''
		Constructor
		'''
		if pNewList is None:
			pNewList = []
		# modify value here
		#print("Parameter list contents: ", pNewList)
		self.__list = pNewList
		#Given a vault string, this function will create a list

	def __str__(self):
		return str(self.__list)

	def __eq__(self, other): 
		return set(self.__list) == set(self.__list)

# 	def __eq__(self, other):
# 		set1 = set(self.__list)
# 		set2 = set(other.__list)
# 		return set1 == set2
	
	def append(self, pPasswordTuple):
		if not isinstance(pPasswordTuple, PasswordTuple):
			raise TypeError("Argument passed into append function for PasswordList is not a PasswordTuple.")
		self.__list.append(pPasswordTuple)
		#sorted(self.__list, key=lambda pair: pair.getTuple()[0])
	
	def pop(self, pIndex):
		return self.__list.pop(pIndex)
		
	def popByIdentifier(self, pIdentifier):
		for i, v in enumerate(self.__list):
			if v.identifier() == pIdentifier:
				return self.pop(i)
		return -1
# 		next(obj for obj in self.__list if obj.identifier==pIdentifier)
# 		x = [1, 2, 3, 4, 2, 2, 3]
# 		x[:] = (value for value in self.__list if value.identifier() != pIdentifier)
# 		>>> x
# 		list(filter((2).__ne__, x)) #[1, 3, 3, 4]
# 		matches = [x for x in self.__list if x.identifier() == pIdentifier]
	
	def getByIdentifier(self, pIdentifier):
		for i, v in enumerate(self.__list):
			if (v.identifier == pIdentifier):
				return self.__list[i]
		return -1
	
	def hasIdentifier(self, pIdentifier):
		for i in self.__list:
			if pIdentifier == i.identifer():
				return True
		return False

	def getIdentifierList(self):
		lclList = []
		for v in self.__list:
			lclList.append(v.identifier())
		return lclList
	
	def getList(self):
		return self.__list
	
	def getCopy(self):
		# This method is different from using both copy or deepcopy directly on the passwordlist:
		# It creates an identical copy of the passwordList's list member pointing to the same password tuples.
		return PasswordList(list(self.__list))
	
	def size(self):
		return len(self.__list)
		
	def toString(self):
		returnString = "["
		for i in self.__list:
			returnString += i.toString()
		return returnString + "]"