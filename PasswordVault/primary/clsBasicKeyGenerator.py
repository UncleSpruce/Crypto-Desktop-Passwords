'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''


class BasicKeyGenerator(iKeyGenerator):
	'''
	classdocs
	'''

	def __init__(self, pJoiner, pGenerator, pHasher, pCombiner, pFirstDifferenceMethod, pLastDifferenceMethod):
		'''
		Constructor
		'''
		self.generator = pGenerator
		self.joiner = pJoiner
		self.hasher = pHasher
		self.combiner = pCombiner
		self.firstDifferenceMethod = pFirstDifferenceMethod
		self.lastDifferenceMethod = pLastDifferenceMethod
		
	def generateKey(self, pPasswordList, pResultPassword):
		# Generate a large BigInt.
		lclBigInt = self.generator.generate()
		
		# Record a difference between the generated number and the result.
		lclLastDifference = self.generateDataForRandomToResult(lclBigInt, pPasswordList)
		
		# Record a difference between the generated number and the input.
		lclFirstDifference = self.generateDataForInputToRandom(lclBigInt, pPasswordList)
		
		# Return the key which includes the two differences generated.
		return [lclFirstDifference, lclLastDifference]
	
	def generateDataForInputToRandom(self, pRandom, pPasswordList):
		# Combine the pPassword list into a BigInt using the joiner and combiner specified.
		lclIntList = []
		for i in pPasswordList:
			lclIntList.append(self.joiner(i.identifier, i.password))
		# Assertion: lclIntList has been constructed and it is now time to combine
		lclCombinedInt = self.combiner(lclIntList)
		
		# Calculate the difference between the the combined output and the generated bigInt.
		lclFirstDifference = self.firstDifferenceMethod.calculateDifference(lclCombinedInt, pRandom)
		
		return lclFirstDifference
	
	def generateDataForRandomToResult(self, pRandom, pResultPassword):
		# Calculate the hash of the bigInt.
		lclHashResult = self.hasher.compute(pRandom)
		
		# Calculate the difference between the hash result and pResult to be stored.
		lclLastDifference = self.lastDifferenceMethod.calculateDifference(lclHashResult, pResultPassword)
		
		return lclLastDifference
	
	def useKey(self, pPasswordList):
		return ("", "")