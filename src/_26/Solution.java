package _26;

import java.util.Arrays;

class Solution {
    public int removeDuplicates(int[] nums) {
        int k = nums.length-1;
        int inner_i = -1;
        for(int i=0; i < k; i++){
            inner_i = i + 1;
            while ((inner_i <= k) && (nums[i] == nums[inner_i])){
                inner_i++;
            }
            if(inner_i - i - 1 > 0){
                k = removeSegment(nums, i+1, inner_i - 1, k);
            }
        }
        return k+1;
    }

    public int removeSegment(int[] nums, int from, int to, int k) {
        int shiftDistance = to - from + 1;
        for(int i=from; i <= k-shiftDistance; i++){
            nums[i] = nums[i + shiftDistance];
        }
        return k - shiftDistance;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums = {1, 1};
        System.out.println(sol.removeDuplicates(nums));

        //sol.removeSegment(nums, 1, 2, 4);
        System.out.println(Arrays.toString(nums));
    }
}
