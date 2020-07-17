# P.U.D.I.M.
# Palavreado Universal Didático de Instruções MIPS

<p>
O objetivo do programa é criar uma linguagem mais facilitada para que, as pessoas em processo de aprendizagem da linguagem do MIPS, aprendam ela mais rapido, utilizando comandos mais didáticos para programar.
	<li>Como entrada, temos um arquivo com as instrucoes facilitadas na linguagem PUDIM;</li>
	<li>Como saida, um arquivo com as instrucoes no mesmo formato das instrucoes do MIPS pronto para execução.</li>
</p>

### Pre requisitos do sistema:

- python3 
- spim (pode usar outros simuladores de mips, mas a gente usa spim)

### Para instalar utilize:

```bash
sudo apt install python3 && sudo apt install spim && git fetch https://github.com/ThalesSilva19/mipsPython
```

<h2>Para converter para MIPS digite:</h2>

```bash
python3 main.py nome_arquivo_entrada nome_arquivo_saida  
```

<h2>Para executar use:</h2>

<div>
</div>

```bash
spim -f nome_arquivo_saida  
```
<div>
</div>

<h2>Guia Rápido</h2>
	<p>Para usar PUDIM você precisa criar um arquivo de texto com o código. No editor de texto de sua preferência inicie crie um arquivo com o nome que desejar para o seu programa. Se você quiser ser formal pode usar a extensão .pudim, mas não vai fazer diferença nenhuma na prática.<br>
	PUDIM tem 3 tipos de elementos: registradores, maracadores(labels) e imediatos.<br>
	<b>Registradores:<b>
	São variaveis de 32 bits, podem representar numeros inteiros, caracteres ou posições na memória. Você pode usar os 32 registradores da arquitetura MIPS, em PUDIM eles tem os nomes 0, at, v0, v1, a0, a1, a2, a3, t0, t1, t2, t3, t4, t5, t6, t7, s0, s1, s2, s3, s4, s5, s6, s7, t8, t9, k0, k1, gp, sp, fp e ra. Recomendamos não usar o t9 porque usamos ele como auxiliar.
		
</p>

<h2>Segue a documentação da linguagem</h2>

<div>

<h2>Operadores Aritméticos</h2>
	<table>
		<tr><td><b>PUDIM</b></td><td><b>MIPS</b></td></tr>
		<tr><td>regDest = reg1</td><td>move regDest, reg1</td></tr>
		<tr><td>regDest = imme</td><td>addi regDest, 0, imme</td></tr>32
		<tr><td>regDest = reg1 + reg2</td><td>add regDest, reg1, reg2</td></tr>
		<tr><td>regDest = reg1 + imme</td><td>addi regDest, reg1, imme</td></tr>
		<tr><td>regDest = reg1 - reg2</td><td>sub regDest, reg1, reg2</td></tr>
		<tr><td>regDest = reg1 - imme</td><td>addi $at, 0, imme<br>sub regDest, reg1, $at</td></tr>
		<tr><td>regDest = reg1 * reg2</td><td>mul reg1, reg2 <br> mflo regDest</td></tr>
		<tr><td>regDest = reg1 / reg2</td><td>div reg1, reg2 <br> mflo regDest</td></tr>
		<tr><td>regDest = reg1 % reg2</td><td>div reg1, reg2 <br> mfhi regDest</td></tr>
	</table>

<h2>Operadores Lógicos</h2>
	<table>
		<tr><td><b>PUDIM</b></td><td><b>MIPS</b></td></tr>
		<trW><td>regDest = reg1 AND reg2</td><td>and regDest, reg1, reg2</td></tr>
		<tr><td>regDest = reg1 AND imme</td><td>and regDest, reg1, imme</td></tr>
		<tr><td>regDest = reg1 OR reg2</td><td>or regDest, reg1, reg2</td></tr>
		<tr><td>regDest = reg1 OR imme</td><td>or regDest, reg1, imme</td></tr>
		<tr><td>regDest = reg1 XOR reg2</td><td>xor regDest, reg1, reg2</td></tr>
		<tr><td>regDest = reg1 XOR reg2</td><td>xor regDest, reg1, imme</td></tr>
		<tr><td>regDest = reg1 NOR reg2</td><td>nor regDest, reg1, reg2</td></tr>
		<tr><td>regDest = NOT reg1</td><td>nor regDest, reg1, reg2</td></tr>
	</table>

<h2>Operadores Condicionais</h2>
	<table>
		<tr><td><b>PUDIM</b></td><td><b>MIPS</b></td></tr>
		<tr><td>IF reg1 != reg2 GOTO marcador</td><td>bne reg1, reg2, marcador</td></tr>
		<tr><td>IF reg1 == reg2 GOTO marcador</td><td>beq reg1, reg2, marcador</td></tr>
		<tr><td>IF reg1 >= 0 GOTO marcador</td><td>bgez reg1, marcador</td></tr>
		<tr><td>IF reg1 > 0 GOTO marcador</td><td>bgtz reg1, marcador</td></tr>
		<tr><td>IF reg1 <= 0 GOTO marcador</td><td>blez reg1, marcador</td></tr>
		<tr><td>IF reg1 < 0 GOTO marcador</td><td>bltz reg1, marcador</td></tr>
	</table>
	
<h2>Jumps</h2>
	<table>
		<tr><td><b>PUDIM</b></td><td><b>MIPS</b></td></tr>
		<tr><td>GOTO marcador</td><td>j marcador</td></tr>
		<tr><td>GOTO reg</td><td>jr reg</td></tr>
		<tr><td>ra = GOTO marcador</td><td>jal marcador</td></tr>
	</table>

<h2>Comandos do Sistema</h2>
		<tr><td>ra = GOTO marcador</td><td>jal marcador</td></tr>
	</table>

<h2>Comandos do Sistema</h2>
		<tr><td>ra = GOTO marcador</td><td>jal marcador</td></tr>
	</table>

<h2>Comandos do Sistema</h2>
		<tr><td>ra = GOTO marcador</td><td>jal marcador</td></tr>
	</table>

<h2>Comandos do Sistema</h2>
		<tr><td>ra = GOTO marcador</td><td>jal marcador</td></tr>
	</table>

<h2>Comandos do Sistema</h2>
		<tr><td>ra = GOTO marcador</td><td>jal marcador</td></tr>
	</table>

<h2>Comandos do Sistema</h2>
	<table>
		<tr><td><b>PUDIM</b></td><td><b>MIPS</b></td></tr>
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
