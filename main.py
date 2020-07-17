import sys
import leitura
import logica


if __name__ == "__main__":

	#Abre os arquivos passados na chamada da funcao.
	#"python (ou python3) main.py entrada saida"
	entrada = open(sys.argv[1],"r")
	saida = open(sys.argv[2],"w")

	for linha in entrada:
		palavras = leitura.separaPalavras(linha)
		achou = False
		i = 0
		while not achou and i < len(logica.comandos):
			if logica.comandos[i].verificar(saida,palavras):
				achou = True
			i = i + 1
		if not achou:
			print("Erro!\nLinha não indentificada:"  + linha ,end='')
			print(palavras)
			exit(1)
	for marca in logica.marcadores:
		if not logica.marcadores[marca]:
			print("Marcador com nome \"" + marca + "\" não foi criado")
			exit(1)

	saida.write(logica.data + logica.text)
