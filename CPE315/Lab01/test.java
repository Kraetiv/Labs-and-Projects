import java.util.*;

public class test{
    public static List<Integer> divide(int upper, int lower, int divisor){
        List<Integer> list = new ArrayList<>();

        while ((divisor >> 1) != 0){
            divisor = divisor >> 1;
            lower = lower >> 1;
    
            int mask = 1 << 31;
    
            if((upper & 1) != 0){
                lower |= mask;
            }
            upper = upper >> 1;
        }
        list.add(upper);
        list.add(lower);
        return list;
    }

    public static void main(String[] args){
        System.out.println(divide(1, 1, 65536));
    }

}
