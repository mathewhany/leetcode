class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        groups = defaultdict(set)

        for idea in ideas:
            suf, pre = idea[1:], idea[0]
            groups[pre].add(suf)
            
        
        ans = 0

        for group1 in groups:
            for group2 in groups:
                if group1 == group2: continue

                ans += len(list(groups[group1] - groups[group2])) * len(list(groups[group2] - groups[group1]))

        return ans