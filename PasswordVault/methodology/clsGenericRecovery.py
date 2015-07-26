'''
Created on Jul 20, 2015

@author: Daniel Bruce
'''
import copy

class GenericRecovery(object):
	'''
	classdocs
	'''
	def __init__(self):
		'''
		Constructor
		'''
	def __str__(self):
		return str(self.__dict__)

	def __eq__(self, other): 
		return self.__dict__ == other.__dict__
	
	def recover(self, pVault, pInputList):
		lclResultList = copy.copy(pInputList)
		flag = False
# 		print("Vault contents:")
# 		print(pVault.toString())
		while not flag:
			flag = True
# 			print("The password list is " + lclResultList.toString())
			#testVar = input("Ask user for something outer loop.")
			for key in pVault.getList():
				lclResult = key.computeReturnTuple(lclResultList)
				lclIdList = list(lclResultList.keys())# lclResultList.getIdentifierList() # get keys or whatever
# 				print("Key case:")
# 				print(key.toString())
				#print(lclResultList.toString(), lclIdList, lclResult.toString())
				if not lclResult == -1:
					if not (lclResult[0] in lclIdList):
	# 				print(lclResultList.toString(), lclIdList, lclResult.toString(), condition1, condition2)
					#testVar = input("Ask user for something.")
						flag = False
						lclResultList[lclResult[0]] = lclResult[1]
						#print(lclResultList.toString())
						break
			print()
# 		print("finish")			
		return lclResultList