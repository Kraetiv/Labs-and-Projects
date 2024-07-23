import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Map;

public class MachineCodeGenerator {
    public static void printAllInstructions(ArrayList<Instruction> instructions, Map<String,Integer> labels,PrintStream output) {
        for (Instruction i : instructions) {
            output.printf("format: %s instruction: %s opcode: %s, rs:%s rt:%s rd:%s, shamt:%d, immediate:%s, address:%d, label:%s\n", 
            i.getFormat(), i.getInstruction(), i.getOpcode(), i.getRs(), i.getRt(), i.getRd(), i.getShamt(), i.getImmediate(), i.getAddr(), i.getLabel());
            //will generate the machine code for each instruction and use labels as needed
        }
    }

    public static void convertToMachineCode(ArrayList<Instruction> instructions, Map<String,Integer> labels, PrintStream output) throws AssemblerException {
        Map<String, String> reg = Registers.regMap();

        for (Instruction cur : instructions) {
            try {
                String result = "";
                //System.out.println(cur.getInstruction());

                if (cur.getFormat() == 'R') {
                    //for opcode = 0
                    result += "000000 ";

                    if (cur.getRs() != null) {
                        if (!cur.getInstruction().equals("jr")) {
                            result += reg.get(cur.getRs());
                            result += " ";
                            result += reg.get(cur.getRt());
                            result += " ";
                            result += reg.get(cur.getRd());
                            result += " ";

                            //for shamt = 0
                            result += "00000 ";
                            result += cur.getFunc();
                        } else {
                            result += reg.get(cur.getRs());
                            result += " ";
                            result += "000000000000000 ";
                            result += cur.getFunc();
                        }
                    } else {
                        String zero = "0";
                        String shift = Integer.toBinaryString(cur.getShamt());
                        //for rs = 0 or none
                        result += "00000 ";
                        result += reg.get(cur.getRt());
                        result += " ";
                        result += reg.get(cur.getRd());
                        result += " ";

                        //loop to create a 5 bit shamt
                        while (shift.length() < 5) {
                            shift = zero + shift;
                        }
                        result += shift;
                        result += " ";
                        result += cur.getFunc();
                    }
                }
                //for I
                else if (cur.getFormat() == 'I') {
                    result += cur.getOpcode();
                    result += " ";
                    result += reg.get(cur.getRs());
                    result += " ";
                    result += reg.get(cur.getRt());
                    result += " ";

                    String zero = "0";
                    //loop to make immediate 16 bits
                    if (!cur.getInstruction().equals("beq") && !cur.getInstruction().equals("bne")) {
                        String immediate = Integer.toBinaryString(cur.getImmediate());
                        if (immediate.length() < 16) {
                            while (immediate.length() < 16) {
                                immediate = zero + immediate;
                            }
                        } else {
                            int start = immediate.length() - 16;
                            immediate = immediate.substring(start, immediate.length());
                        }
                        result += immediate;
                    } else {
                        String addr = Label.labelOffset(labels.get(cur.getLabel()), cur.getAddr() + 1, 16);
                        if (addr.length() > 16) {
                            int start = addr.length() - 16;
                            addr = addr.substring(start, addr.length());
                        }
                        result += addr;

                    }


                }
                //for j
                else if (cur.getFormat() == 'J') {
                    result += cur.getOpcode();
                    result += " ";
                    //System.out.println(labels.get(cur.getLabel()) + " " + cur.getAddr());
                    String addr = Integer.toBinaryString(labels.get(cur.getLabel()));
                    String zero = "0";

                    while (addr.length() < 26) {
                        addr = zero + addr;
                    }
                    result += addr;

                } else {
                    throw new AssemblerException("invalid instruction: " + cur.getInstruction());
                }

                //prints out result
                System.out.println(result);
            }
            catch(AssemblerException e){
                System.out.println(e.getMessage());
                break;
            }
        }

    }
}
