class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int curr_consec, max_consec;
        curr_consec = 0;
        max_consec = 0;
        
        for(int i = 0; i < nums.size(); ++i){
            if(nums[i] == 1) {
                curr_consec = curr_consec + 1;
            }
            else {
                if(max_consec < curr_consec){
                    max_consec = curr_consec;
                }
                curr_consec = 0;
            }
        }
        
        if(max_consec >= curr_consec){
            return max_consec;
        }
        return curr_consec;
    }
};