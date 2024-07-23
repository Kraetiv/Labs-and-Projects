import java.util.*;

public class Emulator {
    int[] dataMemory;
    Map<String, Integer> mipsReg = new HashMap<>();
    
    public void emulator(){
        
        mipsReg = createReg();
        dataMemory = new int[8192];
    }

    public static Map<String, Integer> createReg(){
        Map<String, Integer> map = new HashMap<>();
        map.put("pc", 0);
        map.put("$zero", 0);
        map.put("$0", 0);
        map.put("$v0", 0);
        map.put("$v1", 0);
        map.put("$a0", 0);
        map.put("$a1", 0);
        map.put("$a2", 0);
        map.put("$a3", 0);
        map.put("$t0", 0);
        map.put("$t1", 0);
        map.put("$t2", 0);
        map.put("$t3", 0);
        map.put("$t4", 0);
        map.put("$t5", 0);
        map.put("$t6", 0);
        map.put("$t7", 0);
        map.put("$s0", 0);
        map.put("$s1", 0);
        map.put("$s2", 0);
        map.put("$s3", 0);
        map.put("$s4", 0);
        map.put("$s5", 0);
        map.put("$s6", 0);
        map.put("$s7", 0);
        map.put("$t8", 0);
        map.put("$t9", 0);
        map.put("$sp", 0);
        map.put("$ra", 0);
        return map;
    }
}
