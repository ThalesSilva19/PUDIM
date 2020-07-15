<html>
# P.U.D.I.M.
# Palavreado Universal Didático de Instruções MIPS</h1>

<h2>Para converter para MIPS digite:</h2>

```bash
python3 main.py nome_arquivo_entrada nome_arquivo_saida  
```

<h2>Para executar use:</h2>

<div class="codigo">
</div>

```bash
spim -f nome_arquivo_saida  
```
<div class="codigo">
</div>

<p>   
O objetivo do programa é criar uma linguagem mais facilitada para que, as pessoas em processo de aprendizagem da linguagem do MIPS, aprendam ela mais rapido, utilizando comandos mais didáticos para programar.
	<li>Como entrada, temos um arquivo com as instrucoes facilitadas</li>
	<li>Como saida, um arquivo com as instrucoes no mesmo formato das instrucoes do MIPS pronto para execução.</li>
</p>
<h2>Segue a documentação da linguagem</h2>

<div class="tabelas">

<h3>Operadores Aritméticos</h3>
	<table>
		<tr class="cabecalho"><td>PUDIM</td><td>MIPS</td></tr>
		<tr><td>regDest = reg1</td><td>move regDest, reg1</td></tr>
		<tr><td>regDest = imme</td><td>PSEUDO (li)</td></tr>
		<tr><td>regDest = reg1 + reg2</td><td>add regDest, reg1, reg2</td></tr>
		<tr><td>regDest = reg1 + imme</td><td>addi regDest, reg1, imme</td></tr>
		<tr><td>regDest = reg1 - reg2</td><td>sub regDest, reg1, reg2</td></tr>
		<tr><td>regDest = reg1 - imme</td><td>addi $at, 0, imme<br>sub regDest, reg1, $at</td></tr>
		<tr><td>regDest = reg1 * reg2</td><td>PSEUDO (mult)</td></tr>
		<tr><td>regDest = reg1 / reg2</td><td>PSEUDO (div)</td></tr>
		<tr><td>regDest = reg1 % reg2</td><td>PSEUDO (rem)</td></tr>
		<tr><td>regDest = ABS reg1</td><td>PSEUDO (abs)</td></tr>
	</table>

<h3>Operadores Lógicos</h3>
	<table>
		<tr class="cabecalho"><td>PUDIM</td><td>MIPS</td></tr>
		<tr><td>regDest = reg1 AND reg2</td><td>and regDest, reg1, reg2</td></tr>
		<tr><td>regDest = reg1 AND imme</td><td>and regDest, reg1, imme</td></tr>
		<tr><td>regDest = reg1 OR reg2</td><td>or regDest, reg1, reg2</td></tr>
		<tr><td>regDest = reg1 OR imme</td><td>or regDest, reg1, imme</td></tr>
		<tr><td>regDest = reg1 XOR reg2</td><td>xor regDest, reg1, reg2</td></tr>
		<tr><td>regDest = reg1 XOR reg2</td><td>xor regDest, reg1, imme</td></tr>
		<tr><td>regDest = reg1 NOR reg2</td><td>nor regDest, reg1, reg2</td></tr>
		<tr><td>regDest = NOT reg1</td><td>PSEUDO</td></tr>
	</table>

<h3>Operadores Condicionais</h3>
	<table>
		<tr class="cabecalho"><td>PUDIM</td><td>MIPS</td></tr>
		<tr><td>IF reg1 != reg2 GOTO marcador</td><td>bne reg1, reg2, marcador</td></tr>
		<tr><td>IF reg1 == reg2 GOTO marcador</td><td>beq reg1, reg2, marcador</td></tr>
		<tr><td>IF reg1 >= 0 GOTO marcador</td><td>bgez reg1, marcador</td></tr>
		<tr><td>IF reg1 > 0 GOTO marcador</td><td>bgtz reg1, marcador</td></tr>
		<tr><td>IF reg1 <= 0 GOTO marcador</td><td>blez reg1, marcador</td></tr>
		<tr><td>IF reg1 < 0 GOTO marcador</td><td>bltz reg1, marcador</td></tr>
	</table>
	
<h3>Jumps</h3>
	<table>
		<tr class="cabecalho"><td>PUDIM</td><td>MIPS</td></tr>
		<tr><td>GOTO marcador</td><td>j marcador</td></tr>
		<tr><td>GOTO reg</td><td>jr reg</td></tr>
		<tr><td>ra = GOTO marcador</td><td>jal marcador</td></tr>
	</table>

<h3>Comandos do Sistema</h3>
	<table>
		<tr class="cabecalho"><td>PUDIM</td><td>MIPS</td></tr>
		<tr><td>regDest = MEM(reg1 + imme)</td><td>lw regDest, imme(reg1)</td></tr>
		<tr><td>MEM(reg2 + imme) = reg1</td><td>sw reg1, imme(reg2)</td></tr>
		<tr><td>PRINT_INT reg1</td><td>addi $v0, $0, 1<br>addi $a0, reg1, $0<br>syscall</td></tr>
		<tr><td>PRINT_STRING marcador</td><td>addi $v0, $0, 4<br>la $a0, marcador<br>syscall</td></tr>
		<tr><td>PRINT_STRING reg1</td><td>addi $v0, $0, 4<br>add $a0, reg1, $0<br>syscall</td></tr>
		<tr><td>regDest = READ_INT</td><td>addi $v0, $0, 5<br>syscall<br>add reg1, $v0, $0</td></tr>
		<tr><td>regDest = READ_STRING(reg1)</td><td>addi $v0, $0, 8<br>add $a0, reg1, $0<br>add $a1, reg2, $0<br>syscall</td></tr>
		<tr><td>regDest = READ_STRING(imme)</td><td>addi $v0, $0, 8<br>add $a0, reg1, $0<br>addi $a1, $0, imme<br>syscall</td></tr>
		<tr><td>regDest = MALLOC(reg1)</td><td>addi $v0, $0, 9<br>add $a0, $0, reg<br>syscall<br>add reg1, $0, $v1</td></tr>
		<tr><td>regDest = MALLOC(imme)</td><td>addi $v0, $0, 9<br>addi $a0, $0, imme<br>syscall<br>add reg1, $0, $v1</td></tr>
		<tr><td>EXIT</td><td>addi $v0, $0, 10<br>syscall</td></tr>
	</table>
</div>