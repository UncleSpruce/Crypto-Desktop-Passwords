'''
Created on Jul 24, 2015

@author: Daniel Bruce
'''

from methodology.clsPasswordList import PasswordList
from methodology.clsSimpleLabelledKeyGenerator import SimpleLabelledKeyGenerator

class Definitions(object):
	'''
	classdocs
	'''
	def __init__(self):
		'''
		Constructor
		'''
		self.define1()
		
	def define1(self):
		self.gen = SimpleLabelledKeyGenerator()
		
		self.lclpwd1 = ("Facebook", "q234")
		self.lclpwd2 = ("Google", "778")
		self.lclpwd3 = ("LinkedIn", "P324")
		self.lclpwd4 = ("Quora", "hjkhkg34")
		self.lclpwd5 = ("Foursquare", "hjkhksssssg34")
		self.lclpwd6 = ("Dutch Oven", "hjkhsddkg34")

		self.lclpwd1d = ("Facebook", "q234 Duplicated")
		self.lclpwd2d = ("Google", "778 Duplicated")
		self.lclpwd3d = ("LinkedIn", "P324 Duplicated")
		self.lclpwd4d = ("Quora", "hjkhkg34 Duplicated")
		self.lclpwd5d = ("Foursquare", "hjkhksssssg34 Duplicated")
		self.lclpwd6d = ("Dutch Oven", "hjkhsddkg34 Duplicated")
		
		self.passwordListA0 = {}
		
		self.passwordListA1 = {}
		self.passwordListA1[self.lclpwd1[0]] = self.lclpwd1[1] 
		
		self.passwordListA2 = {}
		self.passwordListA2[self.lclpwd1[0]] = self.lclpwd1[1]
		self.passwordListA2[self.lclpwd2[0]] = self.lclpwd2[1]
		
		self.passwordListA3 = {}
		self.passwordListA3[self.lclpwd1[0]] = self.lclpwd1[1]
		self.passwordListA3[self.lclpwd2[0]] = self.lclpwd2[1]
		self.passwordListA3[self.lclpwd3[0]] = self.lclpwd3[1]
		
		self.passwordListA4 = {}
		self.passwordListA4[self.lclpwd1[0]] = self.lclpwd1[1]
		self.passwordListA4[self.lclpwd2[0]] = self.lclpwd2[1]
		self.passwordListA4[self.lclpwd3[0]] = self.lclpwd3[1]
		self.passwordListA4[self.lclpwd4[0]] = self.lclpwd4[1]

		self.passwordListA5 = {}
		self.passwordListA5[self.lclpwd1[0]] = self.lclpwd1[1]
		self.passwordListA5[self.lclpwd2[0]] = self.lclpwd2[1]
		self.passwordListA5[self.lclpwd3[0]] = self.lclpwd3[1]
		self.passwordListA5[self.lclpwd4[0]] = self.lclpwd4[1]
		self.passwordListA5[self.lclpwd5[0]] = self.lclpwd5[1]
		
		self.passwordListA6 = {}
		self.passwordListA6[self.lclpwd1[0]] = self.lclpwd1[1]
		self.passwordListA6[self.lclpwd2[0]] = self.lclpwd2[1]
		self.passwordListA6[self.lclpwd3[0]] = self.lclpwd3[1]
		self.passwordListA6[self.lclpwd4[0]] = self.lclpwd4[1]
		self.passwordListA6[self.lclpwd5[0]] = self.lclpwd5[1]
		self.passwordListA6[self.lclpwd6[0]] = self.lclpwd6[1]

		self.passwordListB6 = {}
		self.passwordListB6[self.lclpwd6[0]] = self.lclpwd6[1]
		
		self.passwordListB5 = {}
		self.passwordListB5[self.lclpwd5[0]] = self.lclpwd5[1]
		self.passwordListB5[self.lclpwd6[0]] = self.lclpwd6[1]

		self.passwordListB4 = {}
		self.passwordListB4[self.lclpwd4[0]] = self.lclpwd4[1]
		self.passwordListB4[self.lclpwd5[0]] = self.lclpwd5[1]
		self.passwordListB4[self.lclpwd6[0]] = self.lclpwd6[1]

		self.passwordListB3 = {}
		self.passwordListB3[self.lclpwd3[0]] = self.lclpwd3[1]
		self.passwordListB3[self.lclpwd4[0]] = self.lclpwd4[1]
		self.passwordListB3[self.lclpwd5[0]] = self.lclpwd5[1]
		self.passwordListB3[self.lclpwd6[0]] = self.lclpwd6[1]
		
		self.passwordListB2 = {}
		self.passwordListB2[self.lclpwd2[0]] = self.lclpwd2[1]
		self.passwordListB2[self.lclpwd3[0]] = self.lclpwd3[1]
		self.passwordListB2[self.lclpwd4[0]] = self.lclpwd4[1]
		self.passwordListB2[self.lclpwd5[0]] = self.lclpwd5[1]
		self.passwordListB2[self.lclpwd6[0]] = self.lclpwd6[1]
		
		self.passwordListX = {}
		self.passwordListX[self.lclpwd1[0]] = self.lclpwd1[1]
		self.passwordListX[self.lclpwd2[0]] = self.lclpwd2[1]
		self.passwordListX[self.lclpwd3[0]] = self.lclpwd3[1]
		self.passwordListX[self.lclpwd5[0]] = self.lclpwd5[1]
		
		self.key1t1 = self.gen.generate(self.passwordListA1, self.lclpwd1)
		self.key1t2 = self.gen.generate(self.passwordListA1, self.lclpwd2)
		self.key1t3 = self.gen.generate(self.passwordListA1, self.lclpwd3)
		self.key1t4 = self.gen.generate(self.passwordListA1, self.lclpwd4)
		self.key1t5 = self.gen.generate(self.passwordListA1, self.lclpwd5)
		self.key1t6 = self.gen.generate(self.passwordListA1, self.lclpwd6)
		
		self.key12t3 = self.gen.generate(self.passwordListA2, self.lclpwd3)
		self.key123t4 = self.gen.generate(self.passwordListA3, self.lclpwd4)
		self.key1234t5 = self.gen.generate(self.passwordListA4, self.lclpwd5)
		self.key12345t6 = self.gen.generate(self.passwordListA5, self.lclpwd6)
		
		self.key6t1 = self.gen.generate(self.passwordListB6, self.lclpwd1)
		self.key6t2 = self.gen.generate(self.passwordListB6, self.lclpwd2)
		self.key6t3 =  self.gen.generate(self.passwordListB6, self.lclpwd3)
		self.key6t4 =  self.gen.generate(self.passwordListB6, self.lclpwd4)
		self.key6t5 =  self.gen.generate(self.passwordListB6, self.lclpwd5)
		self.key6t6 =   self.gen.generate(self.passwordListB6, self.lclpwd6)
		
		self.key12t5 = self.gen.generate(self.passwordListA2, self.lclpwd5)	