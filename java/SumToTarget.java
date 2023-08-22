package java;

import java.util.Arrays;

public class SumToTarget {

    public static void main(String[] args) {
        


    }

    int sumTripletToTarget(int[] arr, int target) {
        Arrays.sort(arr);
        int left = 1,  right = arr.length-1;

        for (int i = 0; i < arr.length; i++) {
            
            while (left < right ) {
                int targetDiff = target - (arr[i] +arr[left] +arr[right]);

                if (targetDiff == 0) {
                    return target - targetDiff;
                }else if (targetDiff < 0) {
                    right--;
                }else {
                    left++;
                }
            }
        }
        return 0;
    }
    
}
