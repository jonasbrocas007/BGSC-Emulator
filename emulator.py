mem = open('memory.txt', 'r')
memread = mem.readlines()
memread = str(memread)
memread = memread.replace('[','')
memread = memread.replace('"','')
memread = memread.replace("'",'')
memread = memread.replace(']','')
memread = memread.replace(' ','')
memread = memread.replace('\\n','')
memread = memread.replace(',','')
memread = memread.split('/')
N = 0
def cpu():
    PC = 0 # Program counter
    txtlist = []
    while True:
        if PC > 31:
            PC = 0
        A = memread[PC] # Accumulator
        if PC != 31:
            PC += 1
        i = memread[PC] # Direct interger
        A = int(A,2)
        i = int(i,2)
        ALU = A + i # Aritmetic logic unit
        iput = input("$ ")


        if iput == ('OUT'):
            if ALU < 255:
                print(ALU)
            else: print("Error Number is bigger then 255 " + str(ALU))

        if iput[:4] == ('CALC'):
            iput = iput.replace('CALC','')
            if '+' in iput:
                iput = iput.split('+')
                A = int(iput[0])
                i = int(iput[1])
                result = A + i
                print(result)

            if '-' in iput:
                iput = iput.split('-')
                A = int(iput[0])
                i = int(iput[1])
                result = A - i
                print(result)
        if iput == 'A':
            print(A)
        if iput == 'i':
            print(i)

        if iput == ('PCI'):
            PC += 1
            print(PC)
        if iput == ('PCD'):
            PC -= 1
            print(PC)

        if iput == ('PCR'):
            PC = 0
            print(PC)

        if iput == ("PC"):
            print(PC)
        if PC < 32:
            if iput[:3] == ('JMP'):
                iput = iput.split(' ')
                PC = int(iput[1])

        if iput == ('TEXT'):
            if memread[PC] == '00000001':
                txtlist.append('a')
            if memread[PC] == '00000010':
                txtlist.append('b')
            if memread[PC] == '00000011':
                txtlist.append('c')
            if memread[PC] == '00000100':
                txtlist.append('d')
            if memread[PC] == '00000101':
                txtlist.append('e')
            if memread[PC] == '00000110':
                txtlist.append('f')
            if memread[PC] == '00000111':
                txtlist.append('g')
            if memread[PC] == '00001000':
                txtlist.append('h')
            if memread[PC] == '00001001':
                txtlist.append('i')
            if memread[PC] == '00001010':
                txtlist.append('j')
            if memread[PC] == '00001011':
                txtlist.append('k')
            if memread[PC] == '00001100':
                txtlist.append('l')
            if memread[PC] == '00001101':
                txtlist.append('m')
            if memread[PC] == '00001110':
                txtlist.append('n')
            if memread[PC] == '00001111':
                txtlist.append('o')
            if memread[PC] == '00010000':
                txtlist.append('p')
            if memread[PC] == '00010001':
                txtlist.append('q')
            if memread[PC] == '00010010':
                txtlist.append('r')
            if memread[PC] == '00010011':
                txtlist.append('s')
            if memread[PC] == '00010100':
                txtlist.append('t')
            if memread[PC] == '00010101':
                txtlist.append('u')
            if memread[PC] == '00010110':
                txtlist.append('v')
            if memread[PC] == '00010111':
                txtlist.append('w')
            if memread[PC] == '00011000':
                txtlist.append('x')
            if memread[PC] == '00011001':
                txtlist.append('y')
            if memread[PC] == '00011010':
                txtlist.append('z')

        if iput[0] == '.':
            if memread[PC] == '00011011': #set mem 00011011 to write to temporary text memory
                PC += 1
                iput = iput.split('.')
                txtlist.append(iput[1])
                #print(txtlist)
            else: 
                print('set current memory address to 00011011 to write text input')
                continue
            
        if iput == ('TOUT'): #Text Out
            txtlist = str(txtlist)
            txtlist = txtlist.replace('[','')
            txtlist = txtlist.replace(']','')
            txtlist = txtlist.replace('"','')
            txtlist = txtlist.replace("'",'')
            txtlist = txtlist.replace(',','')
            print(txtlist)
            if txtlist == []:
                print('write some text to output to the textlist')
                continue
print('booted')
cpu()