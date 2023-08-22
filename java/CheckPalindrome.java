package java;
// package java;
import java.util.*;

class CheckPalindrome {
 
    public static void main(String[] args) {
        
        ArrayList<Integer> arrayList = new ArrayList<Integer>();

        arrayList.add(1);
        arrayList.add(2);
        arrayList.add(-1);
        arrayList.add(2);
        arrayList.add(2);

       
        boolean isCycled = hasCycle(arrayList);
        System.out.println(isCycled);
        
    }

    public static boolean hasCycle(ArrayList<Integer> arrayList) {
        int slow = 0, fast = 0;
        while (fast < arrayList.size()) {
            
            if (arrayList.get(slow) == arrayList.get(fast)) {
                return true;
            }

            slow ++;
            fast += 2;

        }

        return false;
    }
}