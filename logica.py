from registradores import registradores

marcadores = {}
strings = {}
data = '.data\n'
text = '.text\n.globl main\nmain:\n'

class Comando: 
	def __init__(self,output,input):
		self.input = input
		self.output = output

	def verificar(self, arquivo,vetor):
		global text
		global data
		flag = len(vetor) == len(self.input)
		i = 0
		regs = [-1,-1,-1]
		reg = 0
		imme = -1
		mark = ""
		if len(vetor) == 0:
			return True
		if vetor[0] == 'STRING' and vetor[2] == '=':
			i = str(len(strings))
			strings[vetor[1]] = 'string' + i
			data += 'string'+ i +': .asciiz ' + vetor[3] + '\n'
			return True
		if vetor[0] == 'REG' and vetor[2] == '=':
			registradores[vetor[1]] = registradores[vetor[3]]
			return True
		if vetor[0] == 'MARK':
			marcadores[vetor[1]] = True
			text += vetor[1] + ':\n'
			return True
		while flag and i < len(vetor):
			if self.input[i] == "reg":
				flag = registador(vetor[i])
				if flag:
					regs[reg] = registradores[vetor[i]]
					reg = reg + 1
			elif self.input[i] == "marcador":
				if string(vetor[i]):
					mark = strings[vetor[i]]
					flag = True
				elif marcador(vetor[i]):
					mark = vetor[i]
					flag = True
				else:
					flag = False
			elif self.input[i] == "imme":
				flag = imediato(vetor[i])
				imme = vetor[i]
			else:
				flag = self.input[i] == vetor[i]
			i += 1
		if flag:
			self.escrever(arquivo,regs,imme,mark)
			return True
		return False

	def escrever(self,arquivo,regs,imme,mark):
		global text
		global data
		text += '\t'
		for palavra in self.output:
			if palavra == "reg1":
				text += regs[0]+' '
			elif palavra == "reg2":
				text += regs[1]+' '
			elif palavra == "reg3":
				text += regs[2]+' '
			elif palavra == "imme":
				text += imme+' '
			elif palavra == "marcador":
				text += mark+' '
			else:
				text += palavra+' '
		text += '\n'

comandos = [

	# operacoes aritmeticas
	Comando(['add', 'reg1', ',','reg2', ',', 'reg3'],['reg','=','reg','+','reg']),
	Comando(['addi','reg1', ',','reg2', ',', 'imme'],['reg','=','reg','+','imme']),
	
	Comando(['sub', 'reg1', ',','reg2', ',', 'reg3'],['reg','=','reg','-','reg']),
	Comando(['addi $k0 $0','imme','\nsub','reg1',',','reg2',',$k0'],['reg','=','reg','-','imme']),

	Comando(['mul', 'reg1', ',','reg2', ',', 'reg3'],['reg','=','reg','*','reg']),
	Comando(['div', 'reg1', ',','reg2', ',', 'reg3'],['reg','=','reg','/','reg']),
	Comando(['rem', 'reg1', ',','reg2', ',', 'reg3'],['reg','=','reg','%','reg']),
	Comando(['abs', 'reg1', ',','reg2'],['reg','=','ABS','reg']),
	
	Comando(['li','reg1',',','imme'],['reg','=','imme']),
	Comando(['move','reg1',',','reg2'],['reg','=','reg']),
	
	# comparacoes
	Comando(['bne',  'reg1', ',', 'reg2',',','marcador'],['IF','reg','!=','reg','GOTO','marcador']),
	Comando(['beq',  'reg1', ',', 'reg2',',','marcador'],['IF','reg','==','reg','GOTO','marcador']),
	Comando(['bge', 'reg1', ',','reg2', ',', 'marcador'],['IF','reg','>=','reg','GOTO','marcador']),
	Comando(['bgt', 'reg1', ',','reg2', ',', 'marcador'],['IF','reg','>','reg','GOTO','marcador']),
	Comando(['ble', 'reg1', ',','reg2', ',', 'marcador'],['IF','reg','<=','reg','GOTO','marcador']),
	Comando(['blt', 'reg1', ',','reg2', ',', 'marcador'],['IF','reg','<','reg','GOTO','marcador']),

	# pulos
	Comando(['j','marcador'],['GOTO','marcador']),
	Comando(['jr', 'reg1'],['GOTO','reg']),
	Comando(['jal', 'marcador'],['ra','=','GOTO','marcador']),

	#memória
	Comando(['lw', 'reg1',',','imme','(','reg2',')'],['reg','=','reg','[','imme',']']),
	Comando(['lb', 'reg1',',','imme','(','reg2',')'],['reg','(','byte',')','=','reg','[','imme',']']),
	Comando(['sw', 'reg2',',','imme','(','reg1',')'],['reg','[','imme',']','=','reg']),

	# syscall
	Comando(['syscall'],['SYSTEM']),
	Comando(['addi $v0, $0, 10\n\tsyscall'],['EXIT']),
	Comando(['addi $v0, $0, 1\n\tadd $a0,','reg1',',$0\n\tsyscall'],['PRINT_INT','reg']),
	Comando(['addi $v0, $0, 4\n\tla $a0,','marcador','\n\tsyscall'],['PRINT_STRING','marcador']),
	Comando(['addi $v0, $0, 4\n\tadd $a0,','reg1','$0\n\tsyscall'],['PRINT_STRING','reg']),
	Comando(['addi $v0, $0, 5\n\tsyscall\n\tadd','reg1','$v0,$0'],['reg','=','READ_INT']),
	Comando(['addi $v0, $0, 8\n\tadd $a0,','reg1',',$0\n\tadd $a1,','reg2',',$0\n\tsyscall'],['reg','=','READ_STRING','(','reg',')']),
	Comando(['addi $v0, $0, 8\n\tadd $a0,','reg1',',$0\n\taddi $a1,$0,','imme','\n\tsyscall'],['reg','=','READ_STRING','(','imme',')']),
	Comando(['addi $v0, $0, 9\n\taddi $a0,$0,','imme','\n\tsyscall\n\tadd ','reg1',',$0,$v0'],['reg','=','MALLOC','(','imme',')']),
	Comando(['addi $v0, $0, 9\n\tadd $a0,$0','reg2','\n\tsyscall\n\tadd ','reg1',',$0,$v0'],['reg','=','MALLOC','(','reg',')'])
]

def registador(reg):
	return reg in registradores

def imediato(imme):
	return imme.isnumeric()

def string (marca):
	global data
	print(marca[0])
	if marca in strings:
		return True
	if marca[0] == "\"":
		print("banana")
		i = str(len(strings))
		strings[marca] = "string" + i
		data += 'string'+ i +': .asciiz ' + marca + '\n'
		print("maracuja")
		return True
	return False

def marcador(marca):
	if marca in marcadores:
		return True
	if not registador(marca) and not imediato(marca) and not string(marca):
		print("entrei no marcador:"+ marca)
		marcadores[marca] = False
		return True
	return False