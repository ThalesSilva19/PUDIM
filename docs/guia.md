
# Guia Rápido
Para usar PUDIM você precisa criar um arquivo de texto com o código. No editor de texto de sua preferência inicie crie um arquivo com o nome que desejar para o seu programa. Se você quiser ser formal pode usar a extensão .pudim, mas não vai fazer diferença nenhuma na prática

## Registradores:
São variaveis de 32 bits, podem representar numeros inteiros, caracteres ou posições na memória. Você pode usar os 32 registradores da arquitetura MIPS, em PUDIM eles tem os mesmos nomes mas sem o $, isso é 0, at, v0, v1, a0, a1, a2, a3, t0, t1, t2, t3, t4, t5, t6, t7, s0, s1, s2, s3, s4, s5, s6, s7, t8, t9, k0, k1, gp, sp, fp e ra.
 
Obs: Recomendamos não usar o t9 porque usamos ele como auxiliar nas operações com imediato.

Para você dar valor a um registrador você usa o '='. Exemplo
```
t0 = 5
```

Ou como resultado de uma operação. Exemplos:
```
t0 = t2 - t8
t1 = t3 + 4
t5 = t2 AND 2
```

### Apelidos
Você também pode dar um apelido aos registradores, que quando for passado para MIPS será subistituido pelo nome. Isso permite que usemos termos mais didáticos e significativos aos registradores que t0, v1 ou s2.
A sintaxe para definir o apelido é:
```
REG apelido_do_registrador_ = nome_do_registrador
```
Exemplo:
```
REG comeco = t0
REG final = t1
comeco = 0
final = comeco - 10
```

## Operações
As operações posiveis são:

* \+   Adição
* \-   Subtração
* /   Divisão
* \*   Multiplicação
* %   Módulo
* AND E binário
* OR  Ou binário
* XOR Ou exclusivo binário

Os operandos podem ser registradores, ou valores imediatos (números escritos diretamente no código).
Pelo menos um deles precisa ser registrador, se quiser fazer uma operação entre dois imediatos, faça em sua calculadora e escreva o resultado como imediato ao invés.

Para uma lista mais detalhada das operações veja a [documentação](documentacao.md).
PUDIM não faz operações com números sem sinal (unsigned) ou de ponto flutuante.

## Desvios Incondicionais
Um desvio serve para levar a execução para outra parte do código. Em pudim para você fazer um desvio você precisa de um marcador em um comando de GOTO.
Exemplo:
```
MARK loop #Marca esse linha com o marcador "loop"
    
    #Linhas para serem repetidas.
    #Linhas para serem repetidas.
    #Linhas para serem repetidas.

    GOTO loop #volta para linha marcada como "loop"
```

Além do GOTO simples existem outros tipos de desvio inciondicional:

### Desvia e salva a posição atual.
```
    ra = GOTO loop #Além de fazer o desvio salva a posição atual do programa no registrador ra (return adress)
```
O registrodor precisa ser ra, não pode ser outro registrador.

### Desvia para posição em registrador.
```
    t0 = loop
    GOTO t0
```
Ao invés de usar um marcador como destino do desvio você usa um registrador.
Se o registrador não tiver uma posição válida para o destino a execução vai dar erro.

### Desvia para posição em registrador e salva a posição atual.
```
    t0 = loop
    ra = GOTO t0
```

## Desvios condicionais

Desvios condicionais, só acontecem se uma comparação for satisfeita. Sua sintaxe é
```
     IF condicao GOTO marcador
```
As opções de comparação são:
* ==  Iguais
* !=  Diferentes
* \>   Maior
* <   Menor
* \>=  Maior igual
* <=  menor igual

## Memória

Você também pode ler ou escrever valores na memória.
Para isso você usa:
```
reg[0]
```
Isso representa a memória que tem como endereço reg + 0.
Para ler ou escrever basta usar o sinal do igual:
```
reg[0] = t5 # Escreve o valor de t5 na posição reg + 0 da memória.
t4 = reg[4] # Escreve o valor de reg + 4 em t4.
```
Por padrão ele vai ler e escrever 4 bytes por vez, para ler 1 byte use (byte) e para ler 2 bytes use (half).
Exemplos: 
```
t1[0] = (byte) t2
i (half) = a[2]
```

## Chamadas de Sistema
Chamadas de sistema são comandos que pedem para o sistema operacional realizar alguma atividade, elas são:

### PRINT_INT reg
Escreve na saida o valor de um registrador.

### PRINT_STRING
Escreve na saida o valor de um string.
Como argumento pode vir um string imediato (alguma coisa entre ""), um registrador ou um marcador de String.
Exemplos:
```
PRINT_STRING "Olá Mundo!"

STRING texto = "Olá Mundo, esse texto é grande e eu vou querer usar ele várias vezes.
Por isso vou salvar ele no marcador texto"
PRINT_STRING texto

t0 = READ_STRING(20)
t0 = t0 + 1
PRINT_STRING t0 #Escreve a string lida sem a primeira letra

```

### reg = READ_INT
Lê um número da entrada e salva em um registrador.

### reg = READ_STRING(tamanho)
Lê um string da entrada e salva em um registrador, respeitando um tamanho máximo.

### reg = MALLOC(tamanho)
Salva em reg o endereço de um bloco da memória heap.
