
<h2>Segue a documentação da linguagem</h2>

<div>

<h2>Atribuições Simples</h2>
	<table>
		<tr><td><b>PUDIM</b></td><td><b>MIPS</b></td></tr>
		<tr><td>regDest = reg1</td><td>move regDest, reg1</td></tr>
		<tr><td>regDest = imme</td><td>addi regDest, 0, imme</td></tr>
		<tr><td>regDest = marcador</td><td>la reg1, marcador</td></tr>
	</table>

<h2>Atribuições Aritméticas</h2>
	<table>
		<tr><td><b>PUDIM</b></td><td><b>MIPS</b></td></tr>
		<tr><td>regDest = reg1 + reg2</td><td>add regDest, reg1, reg2</td></tr>
		<tr><td>regDest = reg1 + imme</td><td>addi regDest, reg1, imme</td></tr>
		<tr><td>regDest = reg1 - reg2</td><td>sub regDest, reg1, reg2</td></tr>
		<tr><td>regDest = reg1 - imme</td><td>addi $at, 0, imme<br>sub regDest, reg1, $at</td></tr>
		<tr><td>regDest = reg1 * reg2</td><td>mul regDest, reg1, reg2</td></tr>
		<tr><td>regDest = reg1 * imme</td><td>addi $t9, $0, imme <br> mul regDest, reg1, $t9 </td></tr>
		<tr><td>regDest = reg1 / reg2</td><td>div regDest, reg1, reg2</td></tr>
		<tr><td>regDest = reg1 / imme</td><td>addi $t9, $0, imme <br> div regDest, reg1, $t9</td></tr>
		<tr><td>regDest = imme / reg1</td><td>addi $t9, $0, imme <br> div regDest, %t9, reg1</td></tr>
		<tr><td>regDest = reg1 % reg2</td><td>rem regDest, reg1, reg2</td></tr>
		<tr><td>regDest = reg1 % imme</td><td>addi $t9, $0, imme <br> rem regDest, reg1, $t9</td></tr>
		<tr><td>regDest = imme % reg1</td><td>addi $t9, $0, imme <br> rem regDest, $t9, reg1</td></tr>
	</table>

<h2>Operadores Condicionais</h2>
	<table>
	<tr><td><b>PUDIM</b></td><td><b>MIPS</b></td></tr>
		<tr><td>IF reg1 != reg2 GOTO marcador</td><td>bne reg1, reg2, marcador</td></tr>
		<tr><td>IF reg1 != imme GOTO marcador</td><td>addi $t9, $0, imme <br> bne reg1, $t9, marcador</td></tr>
		<tr><td>IF reg1 == reg2 GOTO marcador</td><td>beq reg1, reg2, marcador</td></tr>
		<tr><td>IF reg1 == imme GOTO marcador</td><td>addi $t9, $0, imme <br> beq reg1, $t9, marcador</td></tr>
		<tr><td>IF reg1 >= reg2 GOTO marcador</td><td>bge reg1, reg2, marcador</td></tr>
		<tr><td>IF reg1 >= imme GOTO marcador</td><td>addi $t9, $0, imme <br> bge reg1, $t9, marcador</td></tr>
		<tr><td>IF reg1 > reg2 GOTO marcador</td><td>bgt reg1, reg2, marcador</td></tr>
		<tr><td>IF reg1 > imme GOTO marcador</td><td>addi $t9, $0, imme <br> bgt reg1, $t9, marcador</td></tr>
		<tr><td>IF reg1 <= reg2 GOTO marcador</td><td>ble reg1, reg2, marcador</td></tr>
		<tr><td>IF reg1 <= imme GOTO marcador</td><td>addi $t9, $0, imme <br> ble reg1, $t9, marcador</td></tr>
		<tr><td>IF reg1 < reg2 GOTO marcador</td><td>blt reg1, reg2, marcador</td></tr>
		<tr><td>IF reg1 < imme GOTO marcador</td><td>addi $t9, $0, imme <br> blt reg1, $t9, marcador</td></tr>
	</table>
	
<h2>Jumps</h2>
	<table>
		<tr><td><b>PUDIM</b></td><td><b>MIPS</b></td></tr>
		<tr><td>GOTO marcador</td><td>j marcador</td></tr>
		<tr><td>GOTO reg</td><td>jr reg</td></tr>
		<tr><td>ra = GOTO marcador</td><td>jal marcador</td></tr>
		<tr><td>ra = GOTO reg</td><td>jalr reg</td></tr>
	</table>

<h2>Comandos da memória</h2>
	<table>
		<tr><td><b>PUDIM</b></td><td><b>MIPS</b></td></tr>
		<tr><td>regDest = reg1[imme]</td><td>lw regDest, imme(reg1)</td></tr>
		<tr><td>regDest(byte) = reg1[imme]</td><td>lb regDest, imme(reg1)</td></tr>
		<tr><td>reg2[imme] = reg1</td><td>sw reg1, imme(reg2)</td></tr>
	</table>

<h2>Comandos do Sistema</h2>
	<table>
		<tr><td><b>PUDIM</b></td><td><b>MIPS</b></td></tr>
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
