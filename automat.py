import sys

MaxExec = 500

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

	def direct(self):
		return self.direction
		pass

	def nextValue(self):
		return self.newValue
		pass

	def exe(self, value):
		if(self.valid(value)):
			return self.newState
			pass
		else:
			return 0
		pass

	def print(self):
		print("\t",self.state.cod, self.newState.cod, self.value, self.newValue, self.direction)
		pass
	pass

class State():

	def __init__(self, cod, fStates):
		self.cod = cod
		self.final = False
		for fS in fStates:
			if(fS == self.cod):
				self.final = True
				break
		self.transitions = []
		pass
	
	def mount(self, trans, states):
		for tr in trans:
			if(int(tr.split()[0]) == self.cod):
				self.transitions.append(Transition(tr, self, states))
		pass
	
	def exe(self, value):
		for tr in self.transitions:
			if(tr.valid(value)):
				return tr.exe(value)
		return 0
		pass

	def selectDirection(self, pos):
		if(pos >= 0 & pos < len(self.transitions)):
			b = self.transitions[pos].direct()
			return b
		pass

	def selectValue(self, pos):
		if(pos >= 0 & pos < len(self.transitions)):
			return self.transitions[pos].nextValue()
		pass

	def trans(self, value):
		vet = []
		count = 0
		for tr in self.transitions:
			if (tr.valid(value)):
				vet.append(count)
			count += 1
		return vet
		pass

	def exeSpec(self, pos, value):
		if(pos >= 0 & pos < len(self.transitions)):
			return self.transitions[pos].exe(value)
		pass

	def isFinal(self):
		return self.final
		pass
	
	def print(self):
		print("  ", self.cod)
		for tr in self.transitions:
			tr.print()
		print("\r")
		pass
	pass

class Tape():

	def __init__(self, tape, brank):
		self.head = 3
		self.tape = ''
		self.brank = brank
		if(isinstance(tape, Tape)):
			self.tape = tape.content()
			self.head = tape.headR()
			pass
		else:
			self.tape = [brank, brank, brank]
			self.tape.extend(list(tape))
			self.tape.extend([brank, brank, brank])
		pass
	
	def headR(self):
		value = self.head
		return value
		pass
	
	def content(self):
		tp = self.tape
		return tp
		pass

	def value(self):
		return self.tape[self.head]
		pass

	def reflesh(self, newValue, direction):
		self.tape[self.head] = newValue
		if((self.head + 1) == len(list(self.tape))):
			self.tape.extend([self.brank, self.brank, self.brank])
			pass
		elif (self.head == 0):
			aux = [self.brank, self.brank, self.brank]
			aux.extend(self.tape)
			self.tape = aux
			self.head += 3
			pass
		if(direction == 'R'):
			self.head += 1
			pass
		elif(direction == 'L'):
			self.head -= 1
			pass
		pass

	def print(self):
		print("> > > > "+"".join(self.tape)+" < < < <")
		pass
	pass

class Machine():

	def __init__(self, IState, tape, brank):
		self.state = IState
		self.oldState = None
		self.staked = 0
		self.tape = Tape(tape, brank)
		pass

	def main(self):
		self.tape.print()
		v = self.tape.value()
		s = self.state.trans(v)
		if(len(s) > 0):
			if(self.oldState == self.state):
				self.staked += 1
			else:
				self.staked = 0
			self.oldState = self.state
			d = self.state.selectDirection(s[0])
			nV = self.state.selectValue(s[0])
			self.state = self.state.exeSpec(s[0], v)
			self.tape.reflesh(nV,d)
			if(self.state.isFinal()):
				return 2
			if(self.staked > MaxExec):
				return -1
			return 1
		else:
			return 0
		pass
	pass

if(sys.argv.__len__() >= 2):
	arq = open(sys.argv[1], 'r')
	data = arq.readlines()
	dataStates = list(map(int, data[3].split()))
	dataTrans = data[7:]
	brank = data[2].split()[0]
	fStates = data[5].split()
	fStates = list(map(int, fStates))
	states = []
	for st in dataStates:
		states.append(State(st,fStates))
	for st in states:
		st.mount(dataTrans, states)
	IState = int(data[4].split()[0])
	for st in states:
		if(st.cod == IState):
			IState = st
			break
	
	maq = Machine(IState, sys.argv[2], brank)
	a = 1
	while a == 1:
		a = maq.main()
		pass
	if (a == -1):
		print("A maquina entrou em loop!!!")
	elif (a == 0):
		print("A palavra não era valida!!!")
	else:
		print("A palavra era valida!!!")