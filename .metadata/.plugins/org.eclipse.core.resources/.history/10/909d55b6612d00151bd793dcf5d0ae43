'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''

if __name__ == '__main__':
	pass

class BasicStringIntConverter(object):
	'''
	classdocs
	'''

	def __init__(self):
		'''
		Constructor
		'''
		
	def toString(self, pBigInt):
		assert(pBigInt >= 0)
		lclStringList = []
		while pBigInt != 0:
			#print(pBigInt)
			lclStringList.append(chr(pBigInt % 128))
			pBigInt -= pBigInt % 128
			assert(int(pBigInt) == pBigInt)
			pBigInt = int(pBigInt / 128)
		assert(pBigInt == 0)
		return ''.join(lclStringList)
		
	def toInt(self, pString):
		total = 0
		#print(pString)
		lclStringList = list(pString)
		for index, value in enumerate(lclStringList):
			#print((128**index), ord(value))
			total += ((128 ** (index)) * ord(value))
		return total	