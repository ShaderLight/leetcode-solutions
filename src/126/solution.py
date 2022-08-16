from typing import List, Dict, Set
from queue import Queue
from math import inf

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []        

        graph: Dict[str, Set[str]] = self.generateGraph(beginWord, wordList)

        paths: Dict[str, List[str]] = self.bfs(beginWord, graph)

        print(graph)
        print(paths)

        

        return self.tracePaths(paths, endWord, beginWord)

    def tracePaths(self, paths:Dict[str, List[str]], endWord: str, beginWord: str) -> List[List[str]]:
        output = [[endWord]]

        while True:
            n = len(output)
            for _ in range(n):
                curr_path = output.pop(0)

                for node in paths[curr_path[-1]]:
                    output.append(curr_path + [node])

            try:
                if output[0][-1] == beginWord:
                    return list(map(lambda x: list(reversed(x)), output))
            except IndexError:
                return []

    def bfs(self, beginWord: str, graph:Dict[str, Set[str]]) -> Dict[str, List[str]]:
        q: Queue[str] = Queue(0)
        dist: Dict[str, float|int] = {}
        parents: Dict[str, List[str]] = {}

        for word in graph.keys():
            dist[word] = inf
            parents[word] = []

        dist[beginWord] = 0
        q.put(beginWord)

        while not q.empty():
            node = q.get()

            for neighbour in graph[node]:
                if dist[neighbour] == inf:
                    dist[neighbour] = dist[node] + 1
                    parents[neighbour].append(node)
                    q.put(neighbour)
                
                else:
                    if dist[node] + 1 == dist[neighbour]:
                        parents[neighbour].append(node)
                    elif dist[node] + 1 == dist[neighbour]:
                        dist[neighbour] = dist[node] + 1
                        parents[neighbour].clear()
                        parents[neighbour].append(node)

        return parents

    def generateGraph(self, beginWord:str, words: List[str]) -> Dict[str, Set[str]]:
        output: Dict[str, Set[str]] = {}

        for i in range(len(words)):
            output[words[i]] = set(self.possibleTransforms(words[i], words[:i] + words[i+1:]))

        if beginWord not in words:
            output[beginWord] = set(self.possibleTransforms(beginWord, words))

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

    #print(obj.findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
    # Should yield [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]

    print(obj.findLadders('hot', 'dog', ['hot', 'dog']))
