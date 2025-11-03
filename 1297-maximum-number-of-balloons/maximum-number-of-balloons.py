class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        my_dict = {"b":0, "a":0, "l":0, "o":0, "n":0}

        for t in text:
            if t in my_dict.keys():
                my_dict[t] += 1
        
        my_dict["l"] = my_dict["l"]//2
        my_dict["o"] = my_dict["o"]//2

        min_value = sys.maxsize

        for key, value in my_dict.items():
            if value<min_value:
                min_value = value


        return min_value
            

        


        