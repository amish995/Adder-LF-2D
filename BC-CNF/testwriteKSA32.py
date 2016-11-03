adder = open('KSA32.bc','w')
adder.write('BC1.1\n')

x = {1:1,2:2,3:4,4:8,5:16,6:32,7:64,8:128}

#adder.write('ROW 0\n\n')
for i in range(1,33): #WHITE
    #adder.write('WHITE\n')
    Bx = 'B{0}:= ODD(b{0},OP_0);\n'.format(i)
    Px = 'P0_{0}:= ODD(A{0},B{0});\n'.format(i)
    Gx = 'G0_{0}:= AND(A{0},B{0});\n'.format(i)
    adder.write(Bx+Px+Gx+'\n')

adder.write('\n\n\n')

for i in range(1,6):
    #adder.write('ROW '+str(i)+'\n\n')
    #adder.write('GREY\n')
    Cx = 'C{0}_{1}:= AND(P{2}_{1},OP_0);\n'.format(i,x[i],i-1)
    Gx = 'G{0}_{1}:= OR(G{2}_{1},C{0}_{1});\n'.format(i,x[i],i-1)
    adder.write(Cx+Gx+'\n')   
    for j in range(x[i]+1,2*x[i]): #GREY
        #adder.write('GREY\n')
        Cx = 'C{0}_{1}:= AND(P{2}_{1},G{2}_{3});\n'.format(i,j,i-1,j-x[i])
        Gx = 'G{0}_{1}:= OR(G{2}_{1},C{0}_{1});\n'.format(i,j,i-1)
        adder.write(Cx+Gx+'\n')        

    adder.write('\n\n')
    
    for j in range(x[i+1],33): #BLACK
        #adder.write('BLACK\n')
        Px = 'P{0}_{1}:= AND(P{2}_{1},P{2}_{3});\n'.format(i,j,i-1,j-x[i])
        Cx = 'C{0}_{1}:= AND(G{2}_{3},P{2}_{1});\n'.format(i,j,i-1,j-x[i])
        Gx = 'G{0}_{1}:= OR(G{2}_{1},C{0}_{1});\n'.format(i,j,i-1)
        adder.write(Px+Cx+Gx+'\n')

    adder.write('\n\n\n')

#adder.write('ROW 5\n\n')
#adder.write('OUTPUT\n')
Zx = 'Z0:= ODD(P0_1,OP_0);\n'
adder.write(Zx+'\n')

for i in range(1,6): #OUTPUT
    for j in range(x[i],x[i+1]):
        #adder.write('OUTPUT\n')
        Zx = 'Z{1}:= ODD(P0_{2},G{0}_{1});\n'.format(i,j,j+1)
        adder.write(Zx+'\n')
        
adder.close()
print 'done'
