import java.util.*;

public class ParseScript {
    
    public static void readScript(Scanner s, ArrayList<Instruction> instructions, Map<String, Integer> labels){
        while(s.hasNextLine()){
            String line = s.nextLine().trim();
            System.out.println("mips> " + line);
            parseCommands(line, );
        }
    }
    public static void parseCommands(String command, ){
        switch(command){
            case 'h':
                System.out.println("h = show help" +
                "d = dump register state" +
                "s = single step through the program (i.e. execute 1 instruction and stop)" +
                "s num = step through num instructions of the program" +
                "r = run until the program ends" +
                "m num1 num2 = display data memory from location num1 to num2" +
                "c = clear all registers, memory, and the program counter to 0" +
                "q = exit the program");
                break;
            case 'd':
            case 's':

        }
    }
}
