import sys
import leitura
import logica


if __name__ == "__main__":

	#Abre os arquivos passados na chamada da funcao.
	#"python (ou python3) main.py entrada saida"
	entrada = open(sys.argv[1],"r")
	saida = open(sys.argv[2],"w")

	print(".text")
	print(".globl main")
	print("main:")

	for linha in entrada:
		palavras = leitura.separaPalavras(linha) 
		#print(palavras)
		for comando in logica.comandos:
			if comando.verificar(palavras):
				break
