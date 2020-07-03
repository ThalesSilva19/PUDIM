import sys

def letraOuNumero(c):
	return ( 'A' <= c and c <= 'Z') or ('a' <= c and c <= 'z') or ('0' <= c and c <= '9')  

def duplos(c):
	return c in ['=','!','>','<'];

def especiais(c):
	return c in ['+','-','*','/','(',')','=','%',':'];

def separaPalavras(linha):

	palavras = []
	palavra = ""
	duplo = False
		
	for c in linha:

		if duplo:
			duplo = False
			if c == '=':
				palavra.append(c)
				palavras.append(palavra)
				palavra = ""
				continue
			else:
				palavras.append(palavra);
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

if __name__ == "__main__":

	#Abre os arquivos passados na chamada da função.
	#"python main.py entrada saida"
	entrada = open(sys.argv[1],"r")
	saida = open(sys.argv[2],"w")

	for linha in entrada:
		palavras = separaPalavras(linha) 
		print(palavras)
		
