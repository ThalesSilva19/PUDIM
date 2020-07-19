# Funcionamento

O módulo principal pudim.py abre o arquivo de entrada e para cada linha dele ela:

* Chama a função SepararPalavras do módulo leitura.py que lê a entrada caracter por caracter e separa a linha em um vetor de Strings.
* Verifica para cada instrução na lista de comandos do módulo instrucoes.py se aquela linha é compatível com o instruções. Se for escreve a instrução na string .text

Se quiser adcionar uma nova instrução vá em instrucoes.py e adicone um novo comando na lista.

Para criar um comando você vai precisar de dois vetores o input e output.

O input é como sua instrução é escrita em PUDIM, com as palavras e simbolos sepadarados (com exceção dos comparadores).
As palavras 'reg','imme' e 'marcador' são reservadas para serem usadas para representatem qualquer registrador, imediato e marcador respactivamente.
Obs.: Strings também são marcadores.

Por exemplo se quiser criar um incrementador de registrador com sintaxe 'i++', o input ficará:
```python
['reg','+','+']
```

Como output você precisa definir como fica sua sintaxe em MIPS.
Para referenciar o primeiro registrador que foi marcado na instrução use 'reg1', o segundo 'reg2' e o terceiro 'reg3'.
Para referenciar o valor imediato descrito use 'imme' e o 'marcador'.
Nenhuma instrução de PUDIM consegue usar mais de 3 registradores, 1 imediato ou 1 marcador. (Porque nunca precisamos, se quiser usar é só mexer na função escrever do comando).

Para o exemplo anterior o output ficaria:
```python
['addi ','reg1',',','reg1',',1']
```

Se seu comando usar palavras adicione elas entre as 'hotwords' no módulo lógica.py para elas não serem confudidadas com marcadores na execução.

