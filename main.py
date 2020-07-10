import sys
import leitura
import logica
import escrita

if __name__ == "__main__":

	#Abre os arquivos passados na chamada da funcao.
	#"python (ou python3) main.py entrada saida"
	entrada = open(sys.argv[1],"r")
	saida = open(sys.argv[2],"w")

	escrita.tipoR(0,19,14,7,0,2)
	escrita.tipoI(12,19,14,34)
	escrita.tipoJ(0,1345)

	for linha in entrada:
		palavras = leitura.separaPalavras(linha) 
		print(palavras)
		#for comando in logica.comandos:
		#	comando.verificar(palavras)