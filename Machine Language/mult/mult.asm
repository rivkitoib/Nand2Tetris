// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.


	@R0
	D=M
	@num
	M=D //num=R0

	@R1
	D=M
	@multiplier
	M=D //multiplier=R1

	@result
	M=0 //result=0

	@i
	M=0 //i=0
(LOOP)
	@i
	D=M
	M=M+1 //i++
	@multiplier
	D=M-D
	//if (i==multiplier) goto END
	@PUT_RES
	D;JEQ

	@num
	D=M
	@result
	M=M+D
	@LOOP
	0;JMP

(PUT_RES)
	@result
	D=M
	@R2
	M=D //R2=result
	@END
	0;JMP

(END)
	@END
	0;JMP


	