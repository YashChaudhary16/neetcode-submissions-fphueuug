class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_freq = {}
        for c in s1:
            s1_freq[c] = s1_freq.get(c, 0) + 1

        left = right = 0
        count = len(s1)

        while right < len(s2):
            # if current char is valid (in s1)
            if s2[right] in s1_freq:
                if s1_freq[s2[right]] > 0:
                    count -= 1
                s1_freq[s2[right]] -= 1
            else:
                # reset window if invalid char
                while left < right:
                    if s2[left] in s1_freq:
                        s1_freq[s2[left]] += 1
                        if s1_freq[s2[left]] > 0:
                            count += 1
                    left += 1
            right += 1

            # if window size > len(s1), move left
            if right - left > len(s1):
                if s2[left] in s1_freq:
                    if s1_freq[s2[left]] >= 0:
                        count += 1
                    s1_freq[s2[left]] += 1
                left += 1

            # if all chars matched
            if count == 0:
                return True

        return False