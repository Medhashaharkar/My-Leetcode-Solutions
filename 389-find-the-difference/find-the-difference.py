class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        my_dict = {}

        for c in t:
            if c in my_dict.keys():
                my_dict[c] += 1
            else:
                my_dict[c] = 1
        
        for c in s:
            if c in my_dict.keys():
                my_dict[c] -= 1
                if my_dict[c] == 0:
                    del my_dict[c]

        for k in my_dict.keys():
            return k

                


        