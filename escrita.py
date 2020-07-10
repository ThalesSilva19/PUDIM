#R opcode (6) rs (5) rt (5) rd (5) shamt (5) funct (6)
#I opcode (6) rs (5) rt (5) imediato (16)
#J opcode (6) endereco (26)

def tipoR(opcode,rs,rt,rd,shamt,funct):
    print("{:06b}".format(opcode),end = ' ')
    print("{:05b}".format(rs),end = ' ')
    print("{:05b}".format(rt),end = ' ')
    print("{:05b}".format(rd),end = ' ')
    print("{:05b}".format(shamt),end = ' ')
    print("{:06b}".format(funct))

def tipoI(opcode,rs,rt,imme):
    print("{:06b}".format(opcode),end=' ')
    print("{:05b}".format(rs),end=' ')
    print("{:05b}".format(rt),end=' ')
    print("{:016b}".format(imme))

def tipoJ(opcode,imme):
    print("{:06b}".format(opcode),end=' ')
    print("{:026b}".format(imme))