import java.util.*;
class Solution {
    public boolean isPalindrome(String s) {
        if(s.equals("")) return false;
        
        String str = s.replaceAll("[^a-zA-Z]", "").toLowerCase();
        
        System.out.println(str); 

        int left = 0;
        int right = str.length()-1;
        
        while(left<right){
            if( !Objects.equals(str.charAt(left), str.charAt(right)) ) {
                return false;
            }
            left++;
            right--;
        }
        
        return true;
        
        
        
    }
}