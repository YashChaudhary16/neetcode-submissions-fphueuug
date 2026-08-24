from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        graph = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}

        for i in range(1, len(words)):
            prev_word, curr_word = words[i-1], words[i]
            if len(prev_word) > len(curr_word) and prev_word.startswith(curr_word):
                return ""
            for j in range(min(len(prev_word), len(curr_word))):
                if prev_word[j] != curr_word[j]:
                    if curr_word[j] not in graph[prev_word[j]]:   # dedup here
                        graph[prev_word[j]].add(curr_word[j])
                        indegree[curr_word[j]] += 1
                    break

        
        queue = deque([])
        for n in indegree:
            if indegree[n] == 0:
                queue.append(n)
        
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        
        return "".join(res) if len(res) == len(indegree) else ""