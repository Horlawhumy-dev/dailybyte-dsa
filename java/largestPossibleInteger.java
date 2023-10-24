class Solution {
  
  public static int solution(int N)
  {
      System.err.println("Tip: Use Console.Error.WriteLine() to write debug messages on the output tab.");
      // T(C) => O(logN)
    // S(C) => O(1)
      int[] digits = {0, 0, 0}; // store the ints
    
      Solution.getLargestDigits(N, digits);
    
      int largestDigit = Solution.combineInts(digits);
      return largestDigit;
  }
  
  public static void getLargestDigits(int N, int[] digits) {
   // T(C) => O(logN)
    //base case
    if (N == 0) return;
    
    int remainder = N % 10;
    
    
    //get highest int
    if (remainder > digits[0]) {
      digits[2] = digits[1];
      digits[1] = digits[0];
      digits[0] = remainder;
    }
    
    //get middle int
    else if(remainder > digits[1]){
      
      digits[2] = digits[1];
      digits[1] = remainder;
    }
    // get lowest int
    else if (remainder > digits[2]) {
      digits[2] = remainder;
    }
    
    getLargestDigits(N/10, digits); // recursively divide N by 10
    
  }
  
 public static int combineInts(int[] digits) {
   //combine the integers from highest to lowest as an integer
    return (digits[0]*100) + (digits[1] * 10) + digits[2];
  }

}
