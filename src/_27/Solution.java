package _27;

import java.util.Arrays;

class Solution {
    public int removeElement(int[] nums, int val) {
        int k = nums.length;
        for(int i = 0; i < k; i++) {
            while((nums[i] == val) && (i < k)){
                removeNth(nums, i, k);
                k--;
            }
        }
        return k;
    }

    public void removeNth(int[] nums, int n, int k) {
        for(int i = n; i < k-1; i++){
            nums[i] =  nums[i+1];
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] numbers = {0,1,2,2,3,0,4,2};

        sol.removeElement(numbers, 2);

        System.out.println(Arrays.toString(numbers));
        // Should yield [0, 1, 3, 0, 4, 2, 2, 2]
    }
}