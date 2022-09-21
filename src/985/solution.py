from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sums: List[int] = []
        temp_sum = 0
        
        for num in nums:
            if num % 2 == 0:
                temp_sum += num
                
        for query in queries:
            was_even = (nums[query[1]] % 2) == 0
            will_be_even = (nums[query[1]] + query[0]) % 2 == 0
            
            if was_even and will_be_even:
                temp_sum += query[0]
            elif was_even and not will_be_even:
                temp_sum -= nums[query[1]]
            elif not was_even and will_be_even:
                temp_sum += nums[query[1]] + query[0]
            
            sums.append(temp_sum)
            nums[query[1]] += query[0]
                

        return sums


if __name__ == '__main__':
    obj = Solution()
    print(obj.sumEvenAfterQueries([1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]))