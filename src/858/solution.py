class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        '''
        Somewhat faster if math.lcm is used instead
        '''

        y_distance_covered = self.lcm(p, q)

        def isEven(x: int) -> bool:
            return x % 2 == 0

        p_cnt_even, q_cnt_even = isEven(int(y_distance_covered/p)), isEven(int(y_distance_covered/q))

        # p_cnt_even Decides about hitting bottom (True) or upper (False) receptors
        # q_cnt_even Decides about hitting left (True) or right (False) receptor


        if not p_cnt_even and q_cnt_even:
            return 2
        
        if not (p_cnt_even or q_cnt_even): # De Morgan's laws, equivalent to: not X and not Y
            return 1

        if p_cnt_even and not q_cnt_even:
            return 0

        return -1

    def lcm(self, a: int, b: int):
        return int((a * b) / self.gcd(a, b))
    
    def gcd(self, a: int, b: int):
        while a!=b:
            if a>b:
                a -= b
            else:
                b -= a
                
        return a

if __name__ == '__main__':
    obj = Solution()
    print(obj.mirrorReflection(3, 2))
    # Should yield 1