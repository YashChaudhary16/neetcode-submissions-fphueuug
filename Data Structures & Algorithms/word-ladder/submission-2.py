class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
                return 0

        def check_difference(word1, word2):
                difference = 0
                idx = 0

                while idx < len(word1):
                        if word1[idx] != word2[idx]:
                                difference+=1
                        idx+=1

                return difference


        q = deque([beginWord])
        visited = set([beginWord])
        transformations = 1

        while q:
                for _ in range(len(q)):
                        word = q.popleft()

                        if word == endWord:
                                return transformations

                        for word2 in wordList:
                                if word2 not in visited and check_difference(word, word2) == 1:
                                        q.append(word2)
                                        visited.add(word2)
                
                transformations+=1

        return 0

