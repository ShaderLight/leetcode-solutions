from queue import Queue
from typing import List, Dict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        output: List[List[str]] = []
        minimum_seq_len = -1
        check_seq = False
        transforms = self.generateTransforms(beginWord, wordList)
        to_transform: Queue[List[str]] = Queue(0)
        
        to_transform.put([beginWord])
        
        while not to_transform.empty():
            curr_seq: List[str] = to_transform.get()
            
            if check_seq:
                if minimum_seq_len < len(curr_seq):
                    continue
                elif endWord == curr_seq[-1]:
                    output.append(curr_seq)
                    continue
            else:
                if endWord == curr_seq[-1]:
                    check_seq = True
                    minimum_seq_len = len(curr_seq)
                    output.append(curr_seq)
                    continue
            
            for w in transforms[curr_seq[-1]]:
                if w not in curr_seq:
                    to_transform.put(curr_seq + [w])

        return output

    def generateTransforms(self, beginWord:str, wordList: List[str]) -> Dict[str, List[str]]:
        output: Dict[str, List[str]] = {}
        if beginWord not in wordList:
            output[beginWord] = self.possibleTransforms(beginWord, wordList)
            
            for i in range(len(wordList)):
                output[wordList[i]] = self.possibleTransforms(wordList[i], wordList[:i] + wordList[i+1:])
        else:
            for i in range(len(wordList)):
                output[wordList[i]] = self.possibleTransforms(wordList[i], wordList[:i] + wordList[i+1:])
        
        return output

    def possibleTransforms(self, w:str, wordList:List[str]) -> List[str]:
        out: List[str] = []
        for word in wordList:
            if self.string1Diff(w, word):
                out.append(word)
        
        return out
        
    def string1Diff(self, s1:str, s2:str) -> bool:
        assert len(s1) == len(s2)
        
        counter = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                counter += 1
                
        return counter == 1


if __name__ == '__main__':
    obj = Solution()

    print(obj.findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
    # Should yield [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
