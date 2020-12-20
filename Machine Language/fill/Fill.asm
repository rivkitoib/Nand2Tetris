// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.
// Put your code here.

	
(CHECK)
	@background
	M=0

	@KBD
	D=M

	@COLOR
	D;JEQ
	   	 
	@background
	M=-1
	
	//spirala
(COLOR)	
	@32
	D=A
	@columns
	M=D //columns=32

	@256
	D=A
	@rows
	M=D //rows=256

	@SCREEN
	D=A
	@adress
	M=D //adress=SCREEN
	


(LOOP)
	@index
	M=0 //index=0
	(TOP)
		@background
		D=M
		@adress
		A=M
		M=D //change sreen

		@adress
		M=M+1 //adress++
		
		@index
		M=M+1 //index++
		D=M
		
		// while( index < columns ) continue; 
		@columns
		D=M-D
		@TOP
		D;JGT

	@adress
	M=M-1 //adress--
	@index
	M=0 //index=0
	(RIGHT)
		@background
		D=M
		@adress
		A=M
		M=D //change sreen

		@32
		D=A
		@adress
		M=D+M //adress+=32

		@index
		M=M+1 //index++
		D=M
		
		// while( index < rows ) continue; 
		@rows
		D=M-D
		@RIGHT
		D;JGT

	@32
	D=A
	@adress
	M=M-D //adress-=32
	@index
	M=0 //index=0
	(BOTTOM)
		@background
		D=M
		@adress
		A=M
		M=D //change sreen

		@adress
		M=M-1 //adress--
		
		@index
		M=M+1 //index++
		D=M
		
		// while( index < columns ) continue; 
		@columns
		D=M-D
		@BOTTOM
		D;JGT
	@adress
	M=M+1 //adress++
	@index
	M=0 //index=0
	(LEFT)
		@background
		D=M
		@adress
		A=M
		M=D //change sreen

		@32
		D=A
		@adress
		M=M-D //adress-=32

		@index
		M=M+1 //index++
		D=M
		
		// while( index < rows ) continue; 
		@rows
		D=M-D
		@LEFT
		D;JGT

	@32
	D=A
	@adress
	M=M+D //adress+=32
	M=M+D //adress+=32
	M=M+1//adress++

	//update values
	@columns
	M=M-1
	M=M-1 //columns-=2
	@rows
	M=M-1
	M=M-1 //rows-=2

	@rows
	D=M
	

	@LOOP
	D;JGT
	@CHECK
	0;JMP

(END)
@END
 0;JMP



	







