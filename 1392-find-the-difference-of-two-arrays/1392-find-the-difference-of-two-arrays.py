class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[], []]

        set1, set2 = set(nums1), set(nums2)
        for n in nums1: 
            if n not in set2: 
                answer[0].append(n)
        for n in nums2: 
            if n not in set1: 
                answer[1].append(n)

        return [list(set(answer[0])), list(set(answer[1]))]