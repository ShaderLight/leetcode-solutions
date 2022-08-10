class Solution {
    public int findNumbers(int[] nums) {
        int counter = 0;
        for(int i = 0; i < nums.length; i++){
            if(Integer.toString(nums[i]).length() %2 == 0){
                counter++;
            }
        }       
        return counter;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {12,345,2,6,7896};
        System.out.println(s.findNumbers(nums));
    }
}