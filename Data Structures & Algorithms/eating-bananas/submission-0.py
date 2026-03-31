class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # get max from piles
        max_speed = 0
        min_speed = 1
        for pile in piles:
            max_speed = max(max_speed, pile)
        
        resspeed = max_speed

        res = []

        while min_speed <= max_speed:
            mid_speed = (max_speed + min_speed)//2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid_speed)

            if hours > h:
                min_speed = mid_speed + 1
            
            elif hours <= h:
                resspeed = mid_speed
                max_speed = mid_speed - 1
        
        return resspeed



        