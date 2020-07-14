from registradores import registradores

marcadores = {}

class Comando: 
	def __init__(self,output,input):
		self.input = input
		self.output = output

	def verificar(self, vetor):
		flag = len(vetor) == len(self.input)
		i = 0
		regs = [-1,-1,-1]
		reg = 0
		imme = -1
		mark = ""
		if len(vetor) == 0:
			return True
		if vetor[0] == 'REG' and vetor[2] == '=':
			registradores[vetor[1]] = registradores[vetor[3]]
			return True
		if vetor[0] == 'MARK':
			marcadores[vetor[1]] = True
			print(vetor[1] + ':')
			return True
		while flag and i < len(vetor):
			if self.input[i] == "reg":
				flag = registador(vetor[i])
				if flag:
					regs[reg] = registradores[vetor[i]]
					reg = reg + 1
			elif self.input[i] == "imme":
				flag = imediato(vetor[i])
				imme = vetor[i]
			elif self.input[i] == "marcador":
				flag = marcador(vetor[i])
				mark = vetor[i]
			else:
				flag = self.input[i] == vetor[i]
			i += 1
		if flag:
			self.escrever(regs,imme,mark)
			return True
		return False

	def escrever(self,regs,imme,mark):
		print('\t',end=' ')
		for palavra in self.output:
			if palavra == "reg1":
				print(regs[0], end=' ')
			elif palavra == "reg2":
				print(regs[1], end=' ')
			elif palavra == "reg3":
				print(regs[2], end=' ')
			elif palavra == "imme":
				print(imme, end=' ')
			elif palavra == "marcador":
				print(mark,end =' ')
			else:
				print(palavra,end=' ')
		print()

#,',',',',',',',',',',','
#,',',',',',',',',',',','
#,',',',',',',',',',',','
#,',',',',',',',',',',','
#,',',',',',',',',',',','
#,',',',',',',',',',',','
#,',',',',',',',',',',','
#,',',',',',',',',',',','
#,',',',',',',',',',',','
#,',',',',',',',',',',','

comandos = [


	
	# operacoes aritmeticas
	Comando(['add', 'reg1', ',','reg2', ',', 'reg3'],['reg','=','reg','+','reg']),
	Comando(['addi','reg1', ',','reg2', ',', 'imme'],['reg','=','reg','+','imme']),
	
	Comando(['sub', 'reg1', ',','reg2', ',', 'reg3'],['reg','=','reg','-','reg']),
	Comando(['addi','reg1', ',','reg2', ',', '-','imme'],['reg','=','reg','-','imme']),

	Comando(['mul', 'reg1', ',','reg2', ',', 'reg3'],['reg','=','reg','*','reg']),
	Comando(['div', 'reg1', ',','reg2', ',', 'reg3'],['reg','=','reg','/','reg']),
	Comando(['rem', 'reg1', ',','reg2', ',', 'reg3'],['reg','=','reg','%','reg']),
	Comando(['abs', 'reg1', ',','reg2'],['reg','=','ABS','reg']),
	
	Comando(['li','reg1',',','imme'],['reg','=','imme']),
	Comando(['move','reg1',',','reg2'],['reg','=','reg']),
	
	# comparacoes
	Comando(['bne',  'reg1', ',', 'reg2',',','marcador'],['IF','reg','!=','reg','GOTO','marcador']),
	Comando(['beq',  'reg1', ',', 'reg2',',','marcador'],['IF','reg','==','reg','GOTO','marcador']),
	Comando(['bgez', 'reg1', ',', 'marcador'],['IF','reg','>=','0','GOTO','marcador']),
	Comando(['bgtz', 'reg1', ',', 'marcador'],['IF','reg','>','0','GOTO','marcador']),
	Comando(['blez', 'reg1', ',', 'marcador'],['IF','reg','<=','0','GOTO','marcador']),
	Comando(['bltz', 'reg1', ',', 'marcador'],['IF','reg','<','0','GOTO','marcador']),

	# pulos
	Comando(['j','marcador'],['GOTO','marcador']),
	Comando(['jr', 'reg1'],['GOTO','reg1']),

	# syscall
	Comando(['syscall'],['SYSTEM'])
]

def registador(reg):
	return reg in registradores

def imediato(imme):
	return imme.isnumeric()

def marcador (marca):
	return marca in marcadores 