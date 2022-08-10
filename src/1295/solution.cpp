class Solution {
public:
    int findNumbers(vector<int>& nums) {
        int counter = 0;
        int curr_num_of_digits;
        int curr_num;
        for(int num: nums){
            curr_num_of_digits = 0;
            curr_num = num;
            while(curr_num != 0){
                curr_num /= 10;
                curr_num_of_digits += 1;
            }
            if(curr_num_of_digits % 2 == 0){
                counter += 1;
            }
        }
        return counter;
    }
};