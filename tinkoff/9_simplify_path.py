# https://leetcode.com/problems/simplify-path
# Stack, String

class Solution:
    def simplifyPath(self, path: str) -> str:
        seps = path.split("/")
        stack = []
        for item in seps:
            if item == ".." and len(stack) == 0:
                continue
            if item == "..":
                stack.pop()
            elif item == ".":
                continue
            elif item == "":
                continue
            else:
                stack.append("/" + item)
        if len(stack) == 0:
            return "/"
        return "".join(stack)


if __name__ == "__main__":
    path0 = "/.../a/../b/c/../d/./" 
    path1 = "/../"
    path = "/home/////foo/////" # -> /home/foo
    print(Solution().simplifyPath(path1))
