class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        def dfs(node, parent):
            ans = 0
            for adj in tree[node]:
                if adj != parent:
                    childrenMinPath = dfs(adj, node)

                    if childrenMinPath > 0:
                        ans += 2 + childrenMinPath
                    elif hasApple[adj]:
                        ans += 2
                    
            return ans
        
        return dfs(0, -1)
