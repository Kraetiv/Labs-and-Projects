# Name:  Alex Liang, Alexander Berkaloff
# Section: 7
# Description:  Function that finds exponent of given number and power

# Java Comment:
# public int exponent(int num, int power){
#   if(power == 0){ return 1;}
#   int ans = num, inc = num;
#   for(int i = 1; i < power; i++){
#       for(int j = 1; j < num; j++){
#           ans += inc;
#       }
#       inc = ans;
#   }
#   return ans;
# }
#------------------------------------------------------------------
# declare globals
.globl welcome
.globl prompt
.globl modText

# Data Area
.data

welcome:
    .asciiz " This program returns result of exponent \n\n"

prompt1:
    .asciiz " Enter an integer: "

prompt2:
    .asciiz " Enter a power: "

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
	ori     $a0, $a0, 0x2C
	syscall

	# Read 1st integer from the user (5 is loaded into $v0, then a syscall)
	ori     $v0, $0, 5
	syscall

    # Clear $s0 for the base
	ori     $s0, $0, 0

    # Puts base into register
    addu $s0, $v0, $s0

    # This is the starting address of the second prompt
    # Address is the welcome message + first prompt
    ori     $v0, $0, 4
    lui     $a0, 0x1001
    ori     $a0, $a0, 0x40
    syscall

    # Read power from the user (5 is loaded into $v0, then a syscall)
	ori     $v0, $0, 5
	syscall

    # Clear $s1 for the power
    ori     $s1, $0, 0

    # Puts power into register
    addu $s1, $v0, $s1

    # Clears $t0 for answer register
    ori $t0, $0, 0

    # If power is 0, set answer to 1
    # and jump to end
    bne $s1, $0, initloop
    addi $t0, $t0, 1
    j end

initloop:
    # Set answer to number
    add $t0, $s0, $0

    # Set $t1 to 1 (i = 1)
    addi $t1, $0, 1

    # Set inc ($t3) variable to num
    add $t3, $s0, $0

loop1:
    # Check if i is less than power
    beq $t1, $s1, end

    # Set $t2 to 1 (j = 1)
    addi $t2, $0, 1

loop2:
    # Check if j is less than num
    # ans += inc
    # increment j
    beq $t2, $s0, loop2end
    add $t0, $t0, $t3
    addi $t2, $t2, 1
    j loop2

loop2end:
    # inc = ans
    add $t3, $0, $t0

    # Increment i
    addi $t1, $t1, 1
    j loop1

end:
    # Display the answer text
	ori     $v0, $0, 4			
	lui     $a0, 0x1001
	ori     $a0, $a0,0x51
	syscall

    # Display the final number
	# load 1 into $v0 to display an integer
	ori     $v0, $0, 1			
	add 	$a0, $t0, $0
	syscall

    # Exit (load 10 into $v0)
	ori     $v0, $0, 10
	syscall