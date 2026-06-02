class Solution {
    public boolean hasDuplicate(int[] nums) {
        int currentNum;
        for(int i = 0; i < nums.length; i++) {
            currentNum = nums[i];
            for(int j = 0; j < nums.length; j++) {
              if(j == i) {
                continue;
              } 
              if(currentNum == nums[j]) {
                  return true;
              }           
            }                  
        }
        return false;  
    }
}
