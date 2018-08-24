import sys

class Transition():
	state = 0
	newState = 0
	value = ''
	newValue = ''
	direction = ''

	def __init__(self, trans, state, states):
		data = trans.split()
		self.state = state
		self.newState = int(data[1])
		for state in states:
			if(self.newState == state.cod):
				self.newState = state
				break
		self.value = data[2]
		self.newValue = data[3]
		self.direction = data[4]
		pass
	
	def valid(self, value):
		if(self.value == value):
			return 1
		return 0
		pass

	def print(self):
		print("\t",self.state.cod, self.newState.cod, self.value, self.newValue, self.direction)
		pass
	pass

class State():
	def __init__(self, cod, fStates):
		self.cod = cod
		self.type = 0
		for fS in fStates:
			if(fS == self.cod):
				self.type = 1
				break
		self.transitions = []
		pass
	
	def mount(self, trans, states):
		for tr in trans:
			if(int(tr.split()[0]) == self.cod):
				self.transitions.append(Transition(tr, self, states))
		pass
	def print(self):
		print("  ", self.cod)
		for tr in self.transitions:
			tr.print()
		print("\n")
		pass

class Machine():

	def __init__(self):
		self.states = 0
		pass
	pass


if(sys.argv.__len__() >= 2):
	arq = open(sys.argv[1],)
	data = arq.readlines()
	dataStates = list(map(int, data[3].split()))
	dataTrans = data[7:]
	fStates = data[5].split()
	fStates = list(map(int, fStates))
	states = []
	for st in dataStates:
		states.append(State(st,fStates))
	for st in states:
		st.mount(dataTrans, states)
		st.print()