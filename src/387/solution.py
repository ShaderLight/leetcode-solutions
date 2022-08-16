class Solution:
    def firstUniqChar(self, s: str) -> int:
        repeating_chars: set[str] = set()
        encountered_chars: set[str] = set()
        
        for i in range(len(s)):
            if s[i] in encountered_chars:
                repeating_chars.add(s[i])
            else:
                encountered_chars.add(s[i])
        
        nonrepeating = encountered_chars - repeating_chars
        
        for i in range(len(s)):
            if s[i] in nonrepeating:
                return i
            
        return -1