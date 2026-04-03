import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj = collections.defaultdict(list)
        in_degree = [0] * numCourses
        
        # Build the graph and the countdown timers (in-degrees)
        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1
            
        # Start only with courses that have 0 prerequisites
        q = collections.deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        courses_taken = 0
        while q:
            subject = q.popleft()
            courses_taken += 1
            
            for child in adj[subject]:
                # One prerequisite for this child is now satisfied
                in_degree[child] -= 1
                
                # Only add to queue when EVERY prerequisite is done
                if in_degree[child] == 0:
                    q.append(child)
        
        # If we couldn't take all courses, there must be a cycle
        return courses_taken == numCourses