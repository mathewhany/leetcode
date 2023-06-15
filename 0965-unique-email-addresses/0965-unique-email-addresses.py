class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        visited = set()

        for email in emails:
            parts = email.split("@")

            if len(parts) == 2:
                local, domain = parts
                
                normalized = local.split("+")[0].replace(".", "") + "@" + domain
                if normalized not in visited:
                    visited.add(normalized)
        
        return len(visited)