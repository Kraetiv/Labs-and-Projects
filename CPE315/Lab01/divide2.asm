# Name:  Alex Liang, Alexander Berkaloff
# Section: 7
# Description:  Function that splits a 64 bit number into 2 32 bits and 
# divides them by a 31 bit number

# Java Comment:
#    public static List<Integer> divide(int upper, int lower, int divisor){
#        List<Integer> list = new ArrayList<>();
#
#        while ((divisor >> 1) != 0){
#            divisor = divisor >> 1;
#            lower = lower >> 1;
#    
#            int mask = 1 << 31;
#    
#            if((upper & 1) != 0){
#                lower |= mask;
#            }
#            upper = upper >> 1;
#        }
#        list.add(upper);
#        list.add(lower);
#        return list;
#    }


.globl intro
.globl dividend
.globl divider
.globl answer

.data
intro:
	.asciiz " This program divides a 64-bit number \n\n"

dividend:
	.asciiz " Enter a 32-bit Integer: "

divider:
	.asciiz " Enter Divisor: "

answer:
	.asciiz " \n Answer: "

commma:
	.asciiz ", "

#Text Area 
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
	ori     $a0, $a0, 0x2A
	syscall

	# Read 1st integer from the user (5 is loaded into $v0, then a syscall)
	ori     $v0, $0, 5
	syscall

    # Clear $s0 for the base
	ori     $s0, $0, 0

    # Puts first 32-bit number into register
    addu $s0, $v0, $s0

    # This is the starting address of the second prompt
    # Address is the welcome message + first prompt
    ori     $v0, $0, 4
    lui     $a0, 0x1001
    ori     $a0, $a0, 0x2A
    syscall

    # Read second 32-bit number from the user
	ori     $v0, $0, 5
	syscall

    # Clear $s1 for the number
    ori     $s1, $0, 0

    # Puts number into register
    addu $s1, $v0, $s1

	# This is the starting address of the thirdprompt
    # Address is the welcome message + first prompt + second
    ori     $v0, $0, 4
    lui     $a0, 0x1001
    ori     $a0, $a0, 0x43
    syscall

    # Read second 32-bit number from the user
	ori     $v0, $0, 5
	syscall

    # Clear $s1 for the number
    ori     $s2, $0, 0

    # Puts number into register
    addu $s2, $v0, $s2

while:
	# Shift divisor bits right by 1 to check while loop
	srl $t1, $s2, 1
	beq $t1, 0, whileEnd

	# Sets divisor = divisor >> 1
	add $s2, $t1, $0

	# Lower = lower >> 1
	srl $t1, $s1, 1
	add $s1, $s1, $0

	# Clears and sets $t2 for mask
	and $t2, $t2, 0
	addi $t3, $0, 1
	sll $t2, $t3, 31

if:
	# Check if upper & 1  != 0
	and $t3, $s0, 1
	beq $t3, $0, ifend

	# lower |= mask
	or $s1, $s1, $t2
	j if

ifend:
	# upper = upper >> 1
	srl $s0, $s0, 1
	j while

whileEnd:
	 # Display the answer text
	ori     $v0, $0, 4			
	lui     $a0, 0x1001
	ori     $a0, $a0,0x53
	syscall

    # Display the first number
	# load 1 into $v0 to display an integer
	ori     $v0, $0, 1			
	add 	$a0, $s0, $0
	syscall

	# Display the comma
	# load 1 into $v0 to display an integer
	ori     $v0, $0, 4			
	lui     $a0, 0x1001
	ori     $a0, $a0,0x5F
	syscall

	# Display the second number
	# load 1 into $v0 to display an integer
	ori     $v0, $0, 1			
	add 	$a0, $s1, $0
	syscall

    # Exit (load 10 into $v0)
	ori     $v0, $0, 10
	syscall