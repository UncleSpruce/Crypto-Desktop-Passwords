'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''

if __name__ == '__main__':
	pass

class BasicLabelledKeyGenerator(object):
	'''
	classdocs
	'''

	def __init__(self, params):
		'''
		Constructor
		'''
		
	def toString(self, pBigInt):
		lclStringList = []
		while pBigInt != 0:
			lclStringList.append(chr(pBigInt % 128))
			pBigInt -= pBigInt % 128
			pBigInt = pBigInt / 128
		assert(pBigInt == 0)
		return ''.join(lclStringList)
		
	def toBigInt(self, pString):
		total = 0
		lclStringList = list(pString)
		for i in lclStringList:
			total += 128 ^ i.index * ord(i)
		return total	