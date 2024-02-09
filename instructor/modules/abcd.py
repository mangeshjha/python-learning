# Creating a base class 
class Base: 
	def _init_(self):
        # Protected member 
		self.__a = 2
		self.b == self.__a

# Creating a derived class 
class Derived(Base): 
	def _init_(self): 

		# Calling constructor of 
		# Base class 
		Base._init_(self) 
		print("Calling protected member of base class: ", 
			self.b) 

		# Modify the protected variable: 
		self.b = 3
		print("Calling modified protected member outside class: ", 
			self.b) 


obj1 = Derived() 

obj2 = Base() 

# Calling protected member 
# Can be accessed but should not be done due to convention 
print("Accessing protected member of obj1: ", obj1.b) 

# Accessing the protected variable outside 
print("Accessing protected member of obj2: ", obj2.__a)