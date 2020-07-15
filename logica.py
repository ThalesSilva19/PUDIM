from registradores import registradores

marcadores = {}

class Comando: 
	def __init__(self,output,input):
		self.input = input
		self.output = output

	def verificar(self, arquivo,vetor):
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
			arquivo.write(vetor[1] + ':\n')
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
			self.escrever(arquivo,regs,imme,mark)
			return True
		return False

	def escrever(self,arquivo,regs,imme,mark):
		arquivo.write('\t')
		for palavra in self.output:
			print(palavra)
			if palavra == "reg1":
				arquivo.write(regs[0]+' ')
			elif palavra == "reg2":
				arquivo.write(regs[1]+' ')
			elif palavra == "reg3":
				arquivo.write(regs[2]+' ')
			elif palavra == "imme":
				arquivo.write(imme+' ')
			elif palavra == "marcador":
				arquivo.write(mark+' ')
			else:
				arquivo.write(palavra+' ')
		arquivo.write('\n')

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
]

def registador(reg):
	return reg in registradores

def imediato(imme):
	return imme.isnumeric()

def marcador (marca):
	if marca in marcadores:
		return True
	if not registador(marca) and not imediato(marca):
		marcadores[marca] = False
		return True
	return False