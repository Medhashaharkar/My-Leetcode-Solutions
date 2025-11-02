class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        my_dict = {}

        for c in s:
            if c in my_dict.keys():
                my_dict[c] += 1
            else:
                my_dict[c] = 1

        for c in t:
            if c in my_dict.keys():
                my_dict[c] -= 1
                if my_dict[c] == 0:
                    del my_dict[c]
        
        steps = 0

        for key, value in my_dict.items():
            steps = steps + value

        return steps
