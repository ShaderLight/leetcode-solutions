from queue import Queue
from typing import List, Tuple

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        result_translation = ['L', '.', 'R']
        N = len(dominoes)
        queries: Queue[Tuple[int, str]] = Queue()
        dom: List[str] = [i for _,i in enumerate(dominoes)]

        def genNextState(k:int):
            result = 1
            
            try:
                if dom[k-1] == 'R' and k-1 >= 0:
                    result += 1
            except IndexError:
                pass

            try:
                if dom[k+1] == 'L':
                    result -= 1
            except IndexError:
                pass

            return result

        def genQueries():
            for i in range(N):
                if dom[i] == '.':
                    ith_step = genNextState(i)
                    if ith_step != 1:
                        queries.put((i, result_translation[ith_step]))

        def applyQueries():
            while not queries.empty():
                q = queries.get()
                dom[q[0]] = q[1]

        genQueries()

        while not queries.empty():
            applyQueries()
            genQueries()

        return ''.join(dom)


if __name__ == '__main__':
    obj = Solution()
    print(obj.pushDominoes(".L.R...LR..L.."))
    # Should yield "LL.RR.LLRRLL.."