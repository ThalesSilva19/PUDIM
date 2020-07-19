from codigo.registradores import registradores

marcadores = {}
strings = {}
data = '.data\n'
text = '.text\n.globl main\nmain:\n'

hotwords = ['IF','GOTO','SYSTEM','REG','STRING','PRINT_INT','PRINT_STRING','READ_INT','READ_STRING','MARK'];

class Comando: 

	def __init__(self,output,input):
		self.input = input
		self.output = output

	def verificar(self,vetor):

		global text
		global data
		flag = len(vetor) == len(self.input)
		i = 0
		regs = [-1,-1,-1]
		reg = 0
		imme = -1
		mark = ""
		
		#Linha vazia.
		if len(vetor) == 0:
			return True

		#Comandos especiais PUDIM (STRING, REG e MARK)
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

		#Verifica se o vetor é compativel com a instrução.
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

		#Se for compativel escreve a resposta.
		if flag:
			self.escrever(regs,imme,mark)
			return True
		return False


	#Escreve o output esperado definido na saida.
	def escrever(self,regs,imme,mark):
		global text
		global data
		text += '\t'
		for palavra in self.output:
			if palavra == "reg1":
				text += regs[0]
			elif palavra == "reg2":
				text += regs[1]
			elif palavra == "reg3":
				text += regs[2]
			elif palavra == "imme":
				text += imme
			elif palavra == "marcador":
				text += mark
			else:
				text += palavra
		text += '\n'


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
		i = str(len(strings))
		strings[marca] = "string" + i
		data += 'string'+ i +': .asciiz ' + marca + '\n'
		return True
	return False

def marcador(marca):
	if marca in marcadores:
		return True
	if not registador(marca) and not imediato(marca) and not string(marca) and not marca in hotwords:
		print("entrei no marcador:"+ marca)
		marcadores[marca] = False
		return True
	return False
