#Arquivo com funcoes para separar os comandos do arquivo de entrada para poder processar eles no codigo

#Verifica se o parametro eh uma letra ou numero
def letraOuNumero(c):
	return ('A' <= c and c <= 'Z') or ('a' <= c and c <= 'z') or ('0' <= c and c <= '9') or (c == '_') 

def duplos(c):
	return c in ['erro','=','!','>','<']

def especiais(c):
	return c in ['+','-','*','/','(',')','%',':','[',']']

def separaPalavras(linha):

	palavras = []
	palavra = ""
	duplo = False
		
	for c in linha:

		if duplo:
			duplo = False
			if c == '=':
				palavra += c
				palavras.append(palavra)
				palavra = ""
				continue
			else:
				palavras.append(palavra)
				palavra = ""
		
		if c == ' ':
			if palavra != "":
				palavras.append(palavra)
				palavra = ""

		elif letraOuNumero(c):
			palavra += c

		elif especiais(c):
			if palavra != "":
				palavras.append(palavra)
				palavra = ""
			palavras.append(c)

		elif duplos(c):
			duplo = True
			if palavra != "":
				palavras.append(palavra)
				palavra = ""
			palavra += c
		
		elif c == '#':
			return palavras

	if palavra != "":
		palavras.append(palavra)

	return palavras