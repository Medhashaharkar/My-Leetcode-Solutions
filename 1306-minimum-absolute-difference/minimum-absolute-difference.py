class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()
        ptr1 = 0
        ptr2 = 1
        min_diff = sys.maxsize
        while ptr2<len(arr):
            print("ptr1",ptr1)
            print("ptr2",ptr2)
            if arr[ptr2]-arr[ptr1]<min_diff:
                min_diff = arr[ptr2]-arr[ptr1]
            ptr1 += 1
            ptr2 += 1

        ptr1 = 0
        ptr2 = 1
        pairs = []
        while ptr2<len(arr):
            if arr[ptr2]-arr[ptr1] == min_diff:
                pairs.append([arr[ptr1], arr[ptr2]])
            ptr1 += 1
            ptr2 += 1

        return pairs

        