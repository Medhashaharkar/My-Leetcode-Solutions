class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, st1, end1, st2, end2):
            temp=[]
            ogst1 = st1
            ogst2 = st2
            while(st1<=end1 and st2<=end2):
                if(arr[st1]<arr[st2]):
                    temp.append(arr[st1])
                    st1 += 1
                else:
                    temp.append(arr[st2])
                    st2 += 1
            while (st1<=end1):
                temp.append(arr[st1])
                st1+=1
            while (st2<=end2):
                temp.append(arr[st2])
                st2+=1
            for i in range(len(temp)):
                arr[ogst1] = temp[i]
                ogst1+=1

            #print(temp)
            #print(arr)
            return arr

        def sort(arr, start, end):
            if(end<=start):
                return
            mid = (start+end)//2
            sort(arr, start, mid)
            sort(arr, mid+1, end)
            merge(arr, start, mid, mid+1, end)
            return

        sort(nums, 0, len(nums)-1)
        return nums
        