
import java.util.ArrayList;
import java.util.Map;
import java.util.Scanner;

public class LinesScanner {
    public static void processLines(Scanner s, ArrayList<Instruction> instructions, Map<String, Integer> labels) {
        int lineCnt = 0; //keeps track of which line we're at
        while (s.hasNextLine()) {
            String line = s.nextLine().trim();
            line = line.split("#",2)[0]; // comment if any by keeping only anything before the #
            if (line.length() != 0) {
                if (line.contains(":")) {
                    String[] elems = line.split(":");
                    labels.put(elems[0].trim(), lineCnt);
                    if (elems.length == 2) {  //case
                        instructions.add(new Instruction(lineCnt++, elems[1].trim()));
                    }
                } else {
                    instructions.add(new Instruction(lineCnt++, line));
                }
            }
        }
    }
}
