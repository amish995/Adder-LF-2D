one = open('1bitAdder.bc','r');
one.close()

adder = open('32Adder.bc','w');
adder.write('BC1.1\n')
#adder.write('B1:= ODD(b1,OP_0);\n')
adder.write('S0:= ODD(OP_0,A1,B1);\n')
adder.write('CO_1:= OR(AND(A1,B1),AND(B1,OP_0),AND(A1,OP_0));\n\n')

for x in range(2,33):
    #Bx = "B{0}:= ODD(b{0},OP_0);\n".format(x);
    Sx = "S{1}:= ODD(CO_{1},A{0},B{0});\n".format(x,x-1)
    C0_x = "CO_{0}:= OR(AND(A{0},B{0}),AND(B{0},CO_{1}),AND(A{0},CO_{1}));\n".format(x,x-1)
    adder.write(Sx+C0_x+"\n") #adder.write(Bx+Sx+C0_x+"\n")

adder.close()
print "done"
