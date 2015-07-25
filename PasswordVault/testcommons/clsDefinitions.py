'''
Created on Jul 24, 2015

@author: Daniel Bruce
'''
from methodology.clsPasswordTuple import PasswordTuple
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
		
		self.lclpwd1 = PasswordTuple("Facebook", "q234")
		self.lclpwd2 = PasswordTuple("Google", "778")
		self.lclpwd3 = PasswordTuple("LinkedIn", "P324")
		self.lclpwd4 = PasswordTuple("Quora", "hjkhkg34")
		self.lclpwd5 = PasswordTuple("Foursquare", "hjkhksssssg34")
		self.lclpwd6 = PasswordTuple("Dutch Oven", "hjkhsddkg34")

		self.lclpwd1d = PasswordTuple("Facebook", "q234 Duplicated")
		self.lclpwd2d = PasswordTuple("Google", "778 Duplicated")
		self.lclpwd3d = PasswordTuple("LinkedIn", "P324 Duplicated")
		self.lclpwd4d = PasswordTuple("Quora", "hjkhkg34 Duplicated")
		self.lclpwd5d = PasswordTuple("Foursquare", "hjkhksssssg34 Duplicated")
		self.lclpwd6d = PasswordTuple("Dutch Oven", "hjkhsddkg34 Duplicated")
		
		self.passwordListA0 = PasswordList()
		
		self.passwordListA1 = PasswordList()
		self.passwordListA1.append(self.lclpwd1)
		
		self.passwordListA2 = PasswordList()
		self.passwordListA2.append(self.lclpwd1)
		self.passwordListA2.append(self.lclpwd2)
		
		self.passwordListA3 = PasswordList()
		self.passwordListA3.append(self.lclpwd1)
		self.passwordListA3.append(self.lclpwd2)
		self.passwordListA3.append(self.lclpwd3)
		
		self.passwordListA4 = PasswordList()
		self.passwordListA4.append(self.lclpwd1)
		self.passwordListA4.append(self.lclpwd2)
		self.passwordListA4.append(self.lclpwd3)
		self.passwordListA4.append(self.lclpwd4)

		self.passwordListA5 = PasswordList()
		self.passwordListA5.append(self.lclpwd1)
		self.passwordListA5.append(self.lclpwd2)
		self.passwordListA5.append(self.lclpwd3)
		self.passwordListA5.append(self.lclpwd4)
		self.passwordListA5.append(self.lclpwd5)
		
		self.passwordListA6 = PasswordList()
		self.passwordListA6.append(self.lclpwd1)
		self.passwordListA6.append(self.lclpwd2)
		self.passwordListA6.append(self.lclpwd3)
		self.passwordListA6.append(self.lclpwd4)
		self.passwordListA6.append(self.lclpwd5)
		self.passwordListA6.append(self.lclpwd6)

		self.passwordListB6 = PasswordList()
		self.passwordListB6.append(self.lclpwd6)
		
		self.passwordListB5 = PasswordList()
		self.passwordListB5.append(self.lclpwd5)
		self.passwordListB5.append(self.lclpwd6)

		self.passwordListB4 = PasswordList()
		self.passwordListB4.append(self.lclpwd4)
		self.passwordListB4.append(self.lclpwd5)
		self.passwordListB4.append(self.lclpwd6)

		self.passwordListB3 = PasswordList()
		self.passwordListB3.append(self.lclpwd3)
		self.passwordListB3.append(self.lclpwd4)
		self.passwordListB3.append(self.lclpwd5)
		self.passwordListB3.append(self.lclpwd6)
		
		self.passwordListB2 = PasswordList()
		self.passwordListB2.append(self.lclpwd2)
		self.passwordListB2.append(self.lclpwd3)
		self.passwordListB2.append(self.lclpwd4)
		self.passwordListB2.append(self.lclpwd5)
		self.passwordListB2.append(self.lclpwd6)
		
		self.passwordListX = PasswordList()
		self.passwordListX.append(self.lclpwd1)
		self.passwordListX.append(self.lclpwd2)
		self.passwordListX.append(self.lclpwd3)
		self.passwordListX.append(self.lclpwd5)
		
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