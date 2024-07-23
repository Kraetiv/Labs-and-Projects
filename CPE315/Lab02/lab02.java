import java.util.*;
import java.io.*;

public class lab02{
    public static void main(String[] args) throws FileNotFoundException{
        File infile = new File(args[0]);
        Scanner s = new Scanner(infile);
        Map<String, Integer> labels = new HashMap<>();
        getLabel(labels, s);
        System.out.println(labels.get("label2"));
    }

    public static void getLabel(Map<String, Integer> labels, Scanner s){
        int lineCnt = 0; //keeps track of which line we're at
        while(s.hasNextLine()){
            String line = s.nextLine().strip();
            
            /*Checks if it is a line of code or label
            Ignores newlines with whitespaces or comments */
            if((line.length() != 0) && (line.charAt(0) != '#')){
                lineCnt += 1;
            }

            for(int i = 0; i < line.length(); i++){
                if(line.charAt(i) == ':'){
                    labels.put(line.substring(0, i), lineCnt);
                }
            }
        }
    }


}

/* First pass:
    Reads input file
    Parse through the file to check labels
        - probably compare each line to the given opcodes??
        - maybe remove comments during this stage?
    Store labels and addr into a hashmap
*/
/* Second pass:
    Read opcodes/instructions and convert to 32-bit binary
        - Probably do something with stored addr for jumps??
*/