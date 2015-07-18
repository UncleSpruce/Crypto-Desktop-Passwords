'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''

import copy
import math

if __name__ == '__main__':
	pass

class BasicStringIntConverter(object):
	'''
	classdocs
	'''

	def __init__(self, pBase = 256):
		'''
		Constructor
		'''
		self.base = pBase
		
	def toString(self, pBigInt):
		assert(pBigInt >= 0)
		lclStringList = []
		lclBigInt = copy.deepcopy(pBigInt)
		while lclBigInt != 0:
			#print(pBigInt)
			lclTemp = lclBigInt
			lclMod = lclBigInt % self.base #- int(lclBigInt / self.base)# lclBigInt % self.base does not seem to work
			lclStringList.append(chr(lclMod))
			lclTemp -= lclMod
			assert(int(int(lclTemp) / int(self.base)) == int(lclTemp) / int(self.base))
			lclBigInt = copy.deepcopy(int(int(lclTemp) / int(self.base)))
			print(lclMod, lclBigInt, lclStringList)
		assert(lclBigInt == 0)
		return ''.join(lclStringList)
		
	def toInt(self, pString):
		total = 0
		lclStringList = list(pString)
		print(lclStringList)
		for index, value in enumerate(lclStringList):
			#print((128**index), ord(value))			
			total += ((int(self.base) ** int(index)) * ord(value))
			print(ord(value), total)
		return total	