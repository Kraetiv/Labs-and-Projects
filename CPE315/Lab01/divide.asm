# Name:  Alex Liang, Alexander Berkaloff
# Section: 7
# Description:  Function that divides 2 32-bit numbers by a 32-bit divisor
# Java Comment:
# public static void main(String[] args) {
    #   int high;
    #   int low;
    #   int div;
    #   Scanner myObj = new Scanner(System.in);
    #   System.out.println("First Dividend: " + userName);
    #   high = scanner.nextInt();
    #   System.out.println("Second Dividend: " + userName);
    #   low = scanner.nextInt();
    #   System.out.println("Divisor: " + userName);
    #   div = scanner.nextInt();
    #   div == div >>1;
    #   while ((div >> 1) != 0) {
    #       div = div >> 1;
    #       low = low >> 1;
    #
    #       int msbMask = 1<<31; 
    #       if ((high & 1) != 0 ) { 
    #         low  |= msbMask; 
    #       }
    #       high = high >> 1;
    #   }
    #
    #   System.out.println("Result"+ high + " " + low);
    # }
    ####################
    
    
    .globl intro
    .globl dividend
    .globl divider
    .globl answer
    
    .data
    intro:
        .asciiz "This program divides a 64-bit number by  a mutiple of 2.\n" #len 57
    dividend:
        .asciiz " Enter a 32-bit Integer: " #len 25
    
    divider:
        .asciiz " Enter Divisor: " #len 16
    
    answer:
        .asciiz " \n Answer: " #len 11
    
    commma:
        .asciiz "," #len 1
    
    #Text Area 
    .text
    
    main:
        # intro message
        ori     $v0, $0, 4
        lui     $a0, 0x1001
        syscall
    
        #  prompt #1
        ori     $v0, $0, 4
        lui     $a0, 0x1001
        ori     $a0, $a0,0x3A
        syscall
    
        # Read 1st integer from the user
        ori     $v0, $0, 5
        syscall
        # load high to s0
        ori     $s0, $0, 0
        addu    $s0, $v0, $s0
    
        # Display prompt 2
        ori     $v0, $0, 4
        lui     $a0, 0x1001
        ori     $a0, $a0,0x3A
        syscall
    
        # Read 2nd integer
        ori		$v0, $0, 5
        syscall
        # load high to s0
        addu    $s1, $v0, $0
    
        # divider  prompt
        ori     $v0, $0, 4
        lui     $a0, 0x1001
        ori     $a0, $a0,0x54
        syscall
    
        # Read 3rd integer
        ori		$v0, $0, 5
        syscall
        # load divider to s0
        addu    $s2, $v0, $0
    
        # go to divide
        jal 	divide
    
        #  answer intro
        ori     $v0, $0, 4
        lui     $a0, 0x1001
        ori     $a0, $a0,0x65
        syscall
    
        #  set $v0 to 1 indicate integer and display $s0
        ori     $v0, $0, 1
        add 	$a0, $s0, $0
        syscall
    
        # display comma
        ori     $v0, $0, 4
        lui     $a0, 0x1001
        ori     $a0, $a0,0x71
        syscall
    
        #  set $v0 to 1 indicate integer and display $s1
        ori     $v0, $0, 1
        add 	$a0, $s1, $0
        syscall
    
        # Exit (load 10 into $v0)
        ori     $v0, $0, 10
        syscall
        
    divide:
    # int msbMask = 1<<31;
        ori		$t2, $0, 1
        sll		$t2, $t2, 31
    # shift div once
        srl		$s2, $s2, 1 
    loop:
    # div = div >> 1;
        srl		$s2, $s2, 1
    # low = low >> 1;
        srl		$s1, $s1, 1
    #  if ((high & 1) != 0 ) 
        addi    $v1, $0, 1
        and		$v1, $v1, $s0
        beq		$v1, $0, notransfer
    transferlsb:
    #   low  |= msbMask; 
        or		$s1, $s1, $t2
    notransfer: 
    #  high = high >> 1;
        srl     $s0, $s0, 1
    # while ((div >> 1) != 0)
        bne		$s2,$0, loop
        jr		$ra