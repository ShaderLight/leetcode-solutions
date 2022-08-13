from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        N = len(words[0])
        NN = N * len(words)
        output: List[int] = []
        
        for i in range(len(s)-NN + 1):
            available_words = words.copy()
            first_index = i
            j = i
            
            while True:

                try:
                    found_ind = available_words.index(s[j:j+N])
                except ValueError:
                    break

                available_words.pop(found_ind)
                
                if not available_words:
                    output.append(first_index)
                    break
                
                j += N

        return output


if __name__ == '__main__':
    obj = Solution()
    print(obj.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
