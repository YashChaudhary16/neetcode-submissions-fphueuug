class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preq = collections.defaultdict(list)
        preq_count = [0] * numCourses
        for [course, p] in prerequisites:
            preq[p].append(course)
            preq_count[course] += 1
        
        q = deque([i for i, x in enumerate(preq_count) if x == 0])
        completed_courses = len(q)
        res = list(q)

        while q:
            subject = q.popleft()

            for child in preq[subject]:
                preq_count[child] -= 1
                if preq_count[child] == 0:
                    q.append(child)
                    completed_courses += 1
                    res.append(child)
        
        return res if completed_courses == numCourses else []