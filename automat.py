import sys

class Transition():
	__state = 0
	__newState = 0
	__value = ''
	__newValue = ''
	__direction = ''

	def __init__(self, date):
		data = date.split()
		self.__state = int(data[0])
		self.__newState = int(data[1])
		self.__value = data[2]
		self.__newValue = data[3]
		self.__direction = data[4]
		pass
	
	def print(self):
		print(self.__state, self.__newState, self.__value, self.__newValue, self.__direction)
		pass
	pass

class State():
	

class Machine():

	def __init__(self):

		pass
	pass

arq = open(sys.argv[1], )
data = arq.readlines()
trans = Transition(data[7])
trans.print()