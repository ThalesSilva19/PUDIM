import sys
import codigo.leitura as leitura
import codigo.logica as logica
from codigo.instrucoes import comandos


if __name__ == "__main__":

	#Abre os arquivos passados na chamada da funcao.
	entrada = open(sys.argv[1],"r")

	#Para cada linha na entrada
	for linha in entrada:

		#Separa a linha em um vetor de strings.
		palavras = leitura.separaPalavras(linha)
		achou = False
		i = 0

		#Até achar uma instrução compatível
		while not achou and i < len(comandos):
			if comandos[i].verificar(palavras):
				achou = True
			i = i + 1

		#Se não achou avisa o erro
		if not achou:
			print("Erro!\nLinha não indentificada:"  + linha ,end='')
			print(palavras)
			exit(1)

	#Depois verifica se algum marcador era inexistente.
	for marca in logica.marcadores:
		if not logica.marcadores[marca]:
			print("Marcador com nome \"" + marca + "\" não foi criado")
			exit(1)


	#Escreve o .data e o .text na saida
	saida = open(sys.argv[2],"w")
	saida.write(logica.data + logica.text)
