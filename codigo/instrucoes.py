import codigo.logica as logica

comandos = [

	# operacoes aritmeticas
	logica.Comando(['add ', 'reg1', ',','reg2', ',', 'reg3'],['reg','=','reg','+','reg']),
	logica.Comando(['addi ','reg1', ',','reg2', ',', 'imme'],['reg','=','reg','+','imme']),
	logica.Comando(['sub ', 'reg1', ',','reg2', ',', 'reg3'],['reg','=','reg','-','reg']),
	logica.Comando(['addi $t9,$0,','imme','\n\tsub ','reg1',',','reg2',',$t9'],['reg','=','reg','-','imme']),
	logica.Comando(['mul ', 'reg1', ',','reg2', ',', 'reg3'],['reg','=','reg','*','reg']),
	logica.Comando(['addi $t9,$0,','imme','\n\tmul ','reg1',',','reg2',',$t9'],['reg','=','reg','*','imme']),
	logica.Comando(['div ', 'reg1', ',','reg2', ',', 'reg3'],['reg','=','reg','/','reg']),
	logica.Comando(['addi $t9,$0,','imme','\n\tdiv ','reg1',',','reg2',',$t9'],['reg','=','reg','/','imme']),
	logica.Comando(['addi $t9,$0,','imme','\n\tdiv ','reg1',',$t9,','reg2'],['reg','=','imme','/','reg']),
	logica.Comando(['rem ', 'reg1', ',','reg2', ',', 'reg3'],['reg','=','reg','%','reg']),
	logica.Comando(['addi $t9,$0,','imme','\n\trem ','reg1',',','reg2',',$t9'],['reg','=','reg','%','imme']),
	logica.Comando(['addi $t9,$0,','imme','\n\trem ','reg1',',$t9,','reg2'],['reg','=','imme','%','reg']),
	
	#atribuições simples
	logica.Comando(['li ','reg1',',','imme'],['reg','=','imme']),
	logica.Comando(['move ','reg1',',','reg2'],['reg','=','reg']),
	logica.Comando(['la ','reg1',',','marcador'],['reg','=','marcador']),
	
	# comparacoes
	logica.Comando(['bne ',  'reg1', ',', 'reg2',',','marcador'],['IF','reg','!=','reg','GOTO','marcador']),
	logica.Comando(['addi $t9,$0,','imme','\n\tbne ','reg1',',$t9,','marcador'],['IF','reg','!=','imme','GOTO','marcador']),
	logica.Comando(['beq ',  'reg1', ',', 'reg2',',','marcador'],['IF','reg','==','reg','GOTO','marcador']),
	logica.Comando(['addi $t9,$0,','imme','\n\tbqe ','reg1',',$t9,','marcador'],['IF','reg','==','imme','GOTO','marcador']),
	logica.Comando(['bge ', 'reg1', ',','reg2', ',', 'marcador'],['IF','reg','>=','reg','GOTO','marcador']),
	logica.Comando(['addi $t9,$0,','imme','\n\tbge ','reg1',',$t9,','marcador'],['IF','reg','>=','imme','GOTO','marcador']),
	logica.Comando(['bgt ', 'reg1', ',','reg2', ',', 'marcador'],['IF','reg','>','reg','GOTO','marcador']),
	logica.Comando(['addi $t9,$0,','imme','\n\tbgt ','reg1',',$t9,','marcador'],['IF','reg','>','imme','GOTO','marcador']),
	logica.Comando(['ble ', 'reg1', ',','reg2', ',', 'marcador'],['IF','reg','<=','reg','GOTO','marcador']),
	logica.Comando(['addi $t9,$0,','imme','\n\tble ','reg1',',$t9,','marcador'],['IF','reg','<=','imme','GOTO','marcador']),
	logica.Comando(['blt ', 'reg1', ',','reg2', ',', 'marcador'],['IF','reg','<','reg','GOTO','marcador']),
	logica.Comando(['addi $t9,$0,','imme','\n\tblt ','reg1',',$t9,','marcador'],['IF','reg','<','imme','GOTO','marcador']),

	# pulos
	logica.Comando(['j ','marcador'],['GOTO','marcador']),
	logica.Comando(['jr ', 'reg1'],['GOTO','reg']),
	logica.Comando(['jal ', 'marcador'],['ra','=','GOTO','marcador']),
	logica.Comando(['jalr ', 'reg1'],['ra','=','GOTO','reg']),

	#memória
	logica.Comando(['lw ', 'reg1',',','imme','(','reg2',')'],['reg','=','reg','[','imme',']']),
	logica.Comando(['lb ', 'reg1',',','imme','(','reg2',')'],['reg','(','byte',')','=','reg','[','imme',']']),
	logica.Comando(['sw ', 'reg2',',','imme','(','reg1',')'],['reg','[','imme',']','=','reg']),

	# syscall
	logica.Comando(['syscall'],['SYSTEM']),
	logica.Comando(['addi $v0, $0, 10\n\tsyscall'],['EXIT']),
	logica.Comando(['addi $v0, $0, 1\n\tadd $a0,','reg1',',$0\n\tsyscall'],['PRINT_INT','reg']),
	logica.Comando(['addi $v0, $0, 4\n\tla $a0,','marcador','\n\tsyscall'],['PRINT_STRING','marcador']),
	logica.Comando(['addi $v0, $0, 4\n\tadd $a0,','reg1','$0\n\tsyscall'],['PRINT_STRING','reg']),
	logica.Comando(['addi $v0, $0, 5\n\tsyscall\n\tadd ','reg1',',','$v0,$0'],['reg','=','READ_INT']),
	logica.Comando(['addi $v0, $0, 8\n\tadd $a0,','reg1',',$0\n\tadd $a1,','reg2',',$0\n\tsyscall'],['reg','=','READ_STRING','(','reg',')']),
	logica.Comando(['addi $v0, $0, 8\n\tadd $a0,','reg1',',$0\n\taddi $a1,$0,','imme','\n\tsyscall'],['reg','=','READ_STRING','(','imme',')']),
	logica.Comando(['addi $v0, $0, 9\n\taddi $a0,$0,','imme','\n\tsyscall\n\tadd ','reg1',',$0,$v0'],['reg','=','MALLOC','(','imme',')']),
	logica.Comando(['addi $v0, $0, 9\n\tadd $a0,$0','reg2','\n\tsyscall\n\tadd ','reg1',',$0,$v0'],['reg','=','MALLOC','(','reg',')'])
]

