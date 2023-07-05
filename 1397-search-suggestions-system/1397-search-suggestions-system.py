class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        currentWord = ""
        pre = 0
        ans = []

        for l in searchWord:
            currentWord += l

            lo, hi = pre, len(products) - 1
            start = 0
            while lo <= hi:
                mid = (lo + hi) // 2
                if products[mid] >= currentWord:
                    start = mid
                    hi = mid - 1
                else:
                    lo = mid + 1
            ans.append([])
            for i in range(3):
                if start + i < len(products) and products[start + i].startswith(currentWord):
                    ans[-1].append(products[start + i])
            pre = start
        
        return ans
