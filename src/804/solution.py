from typing import List

class Solution:
    def __init__(self):
        self.morse_table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        self.unicode_offset = ord('a')
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        transformations: set[str] = set()
        for word in words:
            transformations.add(self.transformation(word))

        return len(transformations)

    def transformation(self, s:str) -> str:
        output = ''
        
        for char in s:
            output += self.morse_table[ord(char) - self.unicode_offset]

        return output

if __name__ == '__main__':
    obj = Solution()
    print(obj.uniqueMorseRepresentations(["gin","zen","gig","msg"]))
    # Should give 2