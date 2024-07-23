# Name:  Alex Liang, Alexander Berkaloff
# Section: 7
# Description:  Function that reverses the bits of a number

# Java Comment:
# public int reverseBit(int num){
#   int reverse = 0;
#   while(num > 0){
#       reverse = reverse << 1;
#       if((num & 1) == 1){
#           rev++;
#       }
#       num = num >> 1;
#   }
#   return reverse;
# }
#-----------------------------------------------------------
# declare globals
.globl welcome
.globl prompt
.globl modText

# Data Area
.data

welcome:
    .asciiz " This program reverses a number \n\n"

prompt:
    .asciiz " Enter an integer: "

modText:
    .asciiz " \n Reversed integer = "

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
	ori     $a0, $a0,0x23
	syscall

	# Read 1st integer from the user (5 is loaded into $v0, then a syscall)
	ori     $v0, $0, 5
	syscall

    # Sets $t0 to 0 for answer
    add $t0, $0, $0

while:
    # Check if 0 is less than input
    slt $t1, $0, $v0

    # Branch if equal to 0
    beq $t1, $0, end

    # reverse = reverse << 1
    sll $t0, $t0, 1

    # Ands current number with 1. Store in $t2
    andi $t2, $v0, 1

    # Set $t3 to 1 for comparison
    and $t3, $t3, $0
    addi $t3, $t3, 1

    # if num & 1 == 1 (branch if not equal to 1)
    # reverse++
    bne $t2, $t3, ifend
    addi $t0, $t0, 1

ifend:
    # num >>= 1
    srl $v0, $v0, 1

    # Jump back to while loop
    j while

end: 
    # Display the answer text
	ori     $v0, $0, 4			
	lui     $a0, 0x1001
	ori     $a0, $a0,0x37
	syscall

    # Display the reversed number
	# load 1 into $v0 to display an integer
	ori     $v0, $0, 1			
	add 	$a0, $t0, $0
	syscall

    # Exit (load 10 into $v0)
	ori     $v0, $0, 10
	syscall
