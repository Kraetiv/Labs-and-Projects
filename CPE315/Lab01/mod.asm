# Name:  Alex Liang, Alexander Berkaloff
# Section: 7
# Description:  Function that finds remainder of number and divisor

# Java Comment:
# public int mod(int num, int divisor){
# 	return(num % (divisor - 1))l
# }
#----------------------------------------------------------------------

# declare globals
.globl welcome
.globl prompt
.globl modText

# Data Area
.data

welcome:
    .asciiz " This program mods two numbers \n\n"

prompt:
    .asciiz " Enter an integer: "

modText:
    .asciiz " \n Mod = "

#Text Area (i.e. instructions)
.text

main:
    # Display the welcome message (load 4 into $v0 to display)
	ori     $v0, $0, 4			

	# This generates the starting address for the welcome message.
	# (assumes the register first contains 0).
	lui     $a0, 0x1001
	syscall

	# Display prompt
	ori     $v0, $0, 4			
	
	# This is the starting address of the prompt (notice the
	# different address from the welcome message)
	lui     $a0, 0x1001
	ori     $a0, $a0,0x22
	syscall

	# Read 1st integer from the user (5 is loaded into $v0, then a syscall)
	ori     $v0, $0, 5
	syscall

	# Clear $s0 for the sum
	ori     $s0, $0, 0

    # Puts first integer into register
    addu $s0, $v0, $s0

    # Display prompt (4 is loaded into $v0 to display)
	# 0x22 is hexidecimal for 34 decimal (the length of the previous welcome message)
	ori     $v0, $0, 4			
	lui     $a0, 0x1001
	ori     $a0, $a0,0x22
	syscall

	# Read 2nd integer 
	ori	$v0, $0, 5			
	syscall
	# $v0 now has the value of the second integer

    # Subtract 1 from second integer and put it into temp register
    sub $t0, $v0, 1

    # And the number and (divisor - 1) to get remainder
    and $s0, $s0, $t0

    # Display the mod text
	ori     $v0, $0, 4			
	lui     $a0, 0x1001
	ori     $a0, $a0,0x36
	syscall

    # Display the remainder
	# load 1 into $v0 to display an integer
	ori     $v0, $0, 1			
	add 	$a0, $s0, $0
	syscall

    # Exit (load 10 into $v0)
	ori     $v0, $0, 10
	syscall