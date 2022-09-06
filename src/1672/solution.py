from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum_wealth = 0
        
        for customer in accounts:
            local_wealth = self.singleWealth(customer)
            if local_wealth > maximum_wealth:
                maximum_wealth = local_wealth
        
        return maximum_wealth
        
    def singleWealth(self, account: List[int]) -> int:
        wealth = 0
        for money in account:
            wealth += money
            
        return wealth
