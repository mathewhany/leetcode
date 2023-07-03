class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for directory in path.split('/'):
            if directory == '..' and stack:
                stack.pop()
            elif directory not in ['..', '.', '']:
                stack.append(directory)

        return '/' + '/'.join(stack)