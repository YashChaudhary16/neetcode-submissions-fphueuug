class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        speed_pos = []
        for i in range(len(position)):
            speed_pos.append([position[i], speed[i]])
        speed_pos_sorted = sorted(speed_pos, key = lambda x: x[0], reverse=True)

        time_to_reach = []
        for i in range(len(speed_pos_sorted)):
            time_to_reach.append((target - speed_pos_sorted[i][0])/speed_pos_sorted[i][1])
        print(time_to_reach)

        no_of_fleets = 1
        left, right = 0, 0
        while right < len(time_to_reach):
            if time_to_reach[right] > time_to_reach[left]:
                no_of_fleets += 1
                left = right
            else:
                right += 1

        return no_of_fleets