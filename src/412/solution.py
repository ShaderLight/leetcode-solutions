class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return map(self.singleFizzBuzz, range(1, n+1))
    
    def singleFizzBuzz(self, i):
        three_rem = (i%3 == 0)
        five_rem = (i%5 == 0)
        
        if three_rem and five_rem:
            return "FizzBuzz"
        elif five_rem:
            return "Buzz"
        elif three_rem:
            return "Fizz"
        
        return str(i)