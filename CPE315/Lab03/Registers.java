import java.util.*;


/*Contains all supported register and their binary as a string.
Thinking about calling the function so we can search the registers up directly.*/
public class Registers {
    public static Map<String, String> regMap(){
        Map<String, String> map = new HashMap<>();
        map.put("$zero", "00000");
        map.put("$0", "00000");
        map.put("$v0", "00010");
        map.put("$v1", "00011");
        map.put("$a0", "00100");
        map.put("$a1", "00101");
        map.put("$a2", "00110");
        map.put("$a3", "00111");
        map.put("$t0", "01000");
        map.put("$t1", "01001");
        map.put("$t2", "01010");
        map.put("$t3", "01011");
        map.put("$t4", "01100");
        map.put("$t5", "01101");
        map.put("$t6", "01110");
        map.put("$t7", "01111");
        map.put("$s0", "10000");
        map.put("$s1", "10001");
        map.put("$s2", "10010");
        map.put("$s3", "10011");
        map.put("$s4", "10100");
        map.put("$s5", "10101");
        map.put("$s6", "10110");
        map.put("$s7", "10111");
        map.put("$t8", "11000");
        map.put("$t9", "11001");
        map.put("$sp", "11101");
        map.put("$ra", "11111");
        map.put(null, "");

        return map;
    }
}
