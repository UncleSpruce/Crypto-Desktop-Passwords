'''
Created on Jul 15, 2015

@author: Daniel Bruce
'''
from methodology.clsBasicKey import BasicKey
from methodology.iKeyGenerator import iKeyGenerator
from methodology.clsBasicBigIntGenerator import BasicBigIntGenerator
from methodology.clsBasicMapInputToIntermediate import BasicMapInputToIntermediate
from methodology.clsBasicMapIntermediateToResult import BasicMapIntermediateToResult

# Obselete Class

class BasicKeyGenerator(iKeyGenerator):
	'''
	classdocs
	'''

# 		print("Running test FullFunctionality on TestMapFromIntermediateToResult.")
# 		
# 		lclpwd1 = PasswordTuple("Facebook", "q234")
# 		lclpwd2 = PasswordTuple("Google", "778")
# 		lclPasswordList = PasswordList([])
# 		lclPasswordList.append(lclpwd1)
# 		lclPasswordList.append(lclpwd2)
# 		
# 		lclIntermediate = 77823465
# 		
# 		lclStringIntConverter = BasicStringIntConverter()
# 		lclStringJoiner = BasicStringJoiner(lclStringIntConverter)
# 		lclCombiner = BasicCombiner()
# 		lclJoinerAndCombiner = BasicStringJoinerAndCombiner(lclStringJoiner, lclCombiner)
# 		
# 		lclCombinedInput = lclJoinerAndCombiner.joinAndCombine(lclPasswordList)
# 		
# 		lclDifferenceMapper = BasicDifferenceMapper()
# 		lclDifferenceMapper.defineMapper(lclCombinedInput, lclIntermediate)
# 		
# 		lclMapInputToIntermediate = BasicMapInputToIntermediate(lclDifferenceMapper, lclJoinerAndCombiner)
# 		lclMapInputToIntermediate.defineMap(lclPasswordList, lclIntermediate)
# 		
# 		self.assertEqual(lclMapInputToIntermediate.compute(lclPasswordList), lclIntermediate)

	def __init__(self, pGenerator = BasicBigIntGenerator(), pMapInputToIntermediate = BasicMapInputToIntermediate(), pMapIntermediateToResult = BasicMapIntermediateToResult()):#pConverter, pStringJoiner, pCombiner):
		'''
		Constructor
		'''
		self.generator = pGenerator
		
		self.mapInputToIntermediate = pMapInputToIntermediate
		self.mapIntermediateToResult = pMapIntermediateToResult
		
# 		self.converter
# 		
# 		self.stringJoiner = pStringJoiner
# 		
# 		self.combiner = pCombiner	
		
	def generateKey(self, pInputPasswordList, pResult):
		# Generate a large BigInt.
		lclIntermediate = self.generator.generate()
		
		self.mapInputToIntermediate.defineMap(pInputPasswordList, lclIntermediate)
		self.mapIntermediateToResult.defineMap(lclIntermediate, pResult)
		
		return BasicKey(self.mapInputToIntermediate, self.mapIntermediateToResult)
		#lclStringIntConverter = BasicStringIntConverter()
		#lclStringJoiner = BasicStringJoiner(lclStringIntConverter)
# 		lclCombiner = BasicCombiner()
# 		lclJoinerAndCombiner = BasicStringJoinerAndCombiner(lclStringJoiner, lclCombiner)
# 		
# 		lclCombinedInput = lclJoinerAndCombiner.joinAndCombine(lclPasswordList)
# 		
# 		lclDifferenceMapper = BasicDifferenceMapper()
# 		lclDifferenceMapper.defineMapper(lclCombinedInput, lclIntermediate)
# 		
# 		lclMapInputToIntermediate = BasicMapInputToIntermediate(lclDifferenceMapper, lclJoinerAndCombiner)
# 		lclMapInputToIntermediate.defineMap(lclPasswordList, lclIntermediate)
# 		
# 		self.assertEqual(lclMapInputToIntermediate.compute(lclPasswordList), lclIntermediate)
		
		# Record a difference between the generated number and the result.
		#lclLastDifference = self.generateDataForRandomToResult(lclIntermediate, pResultPassword)
		
		# Record a difference between the generated number and the input.
		#lclFirstDifference = self.generateDataForInputToRandom(pPasswordList, lclIntermediate)
		
		# Return the key which includes the two differences generated.
		#return [lclFirstDifference, lclLastDifference]
	
# 	def generateDataForInputToRandom(self, pIntermediate, pPasswordList):
# 		# Combine the pPassword list into a BigInt using the joiner and combiner specified.
# 		lclJoinedAndCombined = self.stringJoinerAndCombiner.joinAndCombine(pPasswordList)
# 		
# 		
# 		lclIntList = []
# 		for i in pPasswordList:
# 			lclIntList.append(self.joiner(i.identifier, i.password))
# 		# Assertion: lclIntList has been constructed and it is now time to combine
# 		lclCombinedInt = self.combiner(lclIntList)
# 		
# 		# Calculate the difference between the the combined output and the generated bigInt.
# 		lclFirstDifference = self.firstDifferenceMethod.calculateDifference(lclCombinedInt, pRandom)
# 		
# 		return lclFirstDifference
# 	
# 	def generateDataForRandomToResult(self, pRandom, pResultPassword):
# 		# Calculate the hash of the bigInt.
# 		lclHashResult = self.hasher.compute(pRandom)
# 		
# 		# Calculate the difference between the hash result and pResult to be stored.
# 		lclLastDifference = self.lastDifferenceMethod.calculateDifference(lclHashResult, pResultPassword)
# 		
# 		return lclLastDifference