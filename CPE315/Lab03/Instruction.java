
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.lang.Integer;


public class Instruction {
    private String instruction ="";
    private String opcode;
    private char format;
    private String rs;
    private String rt;
    private String rd;
    private String label;
    private int shamt;
    private String func;
    private int immediate;
    private int address;

    private String operand0;
    private String operand1;
    private String operand2;


    Instruction(int addr, String line) {
        address = addr;
        instruction = "";
        //will convert from the line of text to  format, opcode, rs,  rt, rd, immediate,shamt etc...
        parseComponents(line);
        instructionOpCode();
        processOperands();
    }

    private void parseComponents(String line) {
        int startOperands = 0;
        final Matcher matcher=Pattern.compile("and|or|addi|add|sll|sub|slt|beq|bne|lw|sw|jal|jr|j").matcher(line);
        if(matcher.find()) {
            startOperands = matcher.end();
        }
        instruction = line.substring(0,startOperands).trim();
        line = line.substring(startOperands).trim();

        String[] components = line.split(",");
        if (components.length == 1) {
            operand0 = components[0].trim();
        }
        else if (components.length == 2) {
            operand0 = components[0].trim();
            operand1 = components[1].trim();
        }
        else if (components.length == 3) {
            operand0 = components[0].trim();
            operand1 = components[1].trim();
            operand2 = components[2].trim();
        }
    }

    private void processOperands() {
        //will process the 1 2 or 3 operands of the instruction to fill rs, rt rd immediate etc...
        switch(format){
            case 'R':
                if(instruction.equals("jr")){
                    rs = operand0;
                }
                else if (instruction.equals("sll")) {

                    rd = operand0;
                    rt = operand1;
                    shamt = Integer.parseInt(operand2);
                }
                else{
                    rs = operand1;
                    rt = operand2;
                    rd = operand0;
                }
                break;
            case 'I':
                //parse I format instr
                if (instruction.equals("lw") || instruction.equals("sw")) {
                    String[] elems= operand1.split("[ \\(\\)]+");
                    rt = operand0;
                    if (elems.length>=2) {
                        immediate = Integer.parseInt(elems[0]);
                        rs = elems[1];
                    }
                }
                else if (instruction.equals("bne") || instruction.equals("beq")) {
                    rs = operand0;
                    rt = operand1;
                    label = operand2;
                }
                else {
                    rt = operand0;
                    rs = operand1;
                    immediate = Integer.parseInt(operand2);

                }
                break;
            case 'J':
                //parse J format instr
                label = operand0;
                break;
        }
    }

    private void instructionOpCode() {
        switch (instruction){
            case "and":
                opcode = "000000";
                format = 'R';
                func = "100100";
                break;
            case "or":
                opcode = "000000";
                format = 'R';
                func = "100101";
                break;
            case "add":
                opcode = "000000";
                format = 'R';
                func = "100000";
                break;
            case "addi":
                opcode = "001000";
                format = 'I';
                break;
            case "sll":
                opcode = "000000";
                format = 'R';
                func = "000000";
                break;
            case "sub":
                opcode = "000000";
                format = 'R';
                func = "100010";
                break;
            case "slt":
                opcode = "000000";
                format = 'R';
                func = "101010";
                break;
            case "beq":
                opcode = "000100";
                format = 'I';
                break;
            case "bne":
                opcode = "000101";
                format = 'I';
                break;
            case "lw":
                opcode = "100011";
                format = 'I';
                break;
            case "sw":
                opcode = "101011";
                format = 'I';
                break;
            case "j":
                opcode = "000010";
                format = 'J';
                break;
            case "jr":
                opcode = "000000";
                format = 'R';
                func = "001000";
                break;
            case "jal":
                opcode = "000011";
                format = 'J';
        }
    }

    public String getInstruction(){return instruction;}
    public String getOpcode(){ return opcode;}
    public char getFormat(){ return format;}
    public String getRs(){ return rs;}
    public String getRt(){ return rt;}
    public String getRd(){ return rd;}
    public int getShamt(){ return shamt;}
    public String getFunc(){ return func;}
    public int getImmediate(){ return immediate;}
    public int getAddr(){ return address;}
    public String getLabel(){ return label;}
};