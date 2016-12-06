'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''
import hashlib
from methodology.iHashMethodology import iHashMethodology
from methodology.clsBasicStringIntConverter import BasicStringIntConverter

class BasicHash(iHashMethodology):
	'''
	classdocs
	'''
	def __init__(self, pSalt = 0, pStringIntConverter = BasicStringIntConverter()):
		'''
		Constructor
		'''
		self.salt = pSalt
		self.converter = pStringIntConverter
		
	def compute(self, pArgument):
		#return pArgument
		lclTempString = self.converter.toString(pArgument)
		#print ("Hash computing:")
		#print(lclTempString)
		lclTempUtf = lclTempString.encode('utf-8') #self.stringIntConverter.toString(pArgument + self.salt)
		#lclTempString = lclTempString.encode('utf-8')
		#print(lclTempUtf)
		lclHash = hashlib.sha512(lclTempUtf)
		#print(lclHash)
		lclTempHex = lclHash.hexdigest()
		#print(lclTempResult)
		lclTempInt = int(lclTempHex, base=16)
		return lclTempInt
		
		#print(lclTempInt)
# 		lclTemp = lclTemp.decode('utf-8') 
# 		lclTempInt = self.converter.toInt(lclTemp)
# 		
# 		lclHashFunction = SHA512.new()
# 		lclString = str(pArgument)
# 		lclHashValue = lclHashFunction.update(lclString)
# 		lclHashDigest = lclHashValue.hexDigest()
# 		lclHash = int(lclHashDigest)
		#return lclHash