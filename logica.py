registradores = {
	"zero":0,
	"at":1,
	"v0":2,
	"v1":3,
	"a0":4,
	"a1":5,
	"a2":6,
	"a3":7,
	"t0":8,
	"t1":9,
	"t2":10,
	"t3":11,
	"t4":12,
	"t5":13,
	"t6":14,
	"t7":15,
	"s0":16,
	"s1":17,
	"s2":18,
	"s3":19,
	"s4":20,
	"s5":21,
	"s6":22,
	"s7":23,
	"t8":24,
	"t9":25,
	"k0":26,
	"k1":27,
	"gp":28,
	"sp":29,
	"fp":30,
	"ra":31
}

marcadores = {}

class Comando:
	def __init__(self,nome,modelo):
		self.modelo = modelo
		self.nome = nome

	def verificar(self, vetor):
		flag = len(vetor) == len(self.modelo)
		i = 0
		while flag and i < len(vetor):
			if self.modelo[i] == "reg":
				flag = registador(vetor[i])
			elif self.modelo[i] == "imme":
				flag = imediato(vetor[i])
			elif self.modelo[i] == "mark":
				flag = marcador(vetor[i])
			else:
				flag = self.modelo[i] == vetor[i]
			i += 1
		if flag:
			print(self.nome)

comandos = [
	Comando("add",['reg','=','reg','+','reg']),
	Comando("addi",['reg','=','reg','+','imme']),
	Comando("li",['reg','=','imme']),
	Comando("move",['reg','=','reg']),
	Comando("bnei",['IF','reg','!=','imme','GOTO','marcador'])
]

def registador(reg):
	return reg in registradores

def imediato(imme):
	d = unicode(imme, 'utf-8')
	return d.isnumeric()

def marcador (marca):
	return marca in marcadores