# a = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
# # a = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
#
# a = a.split("\n")
# b = a[2].split("\t")
# print(a)
# print(b)

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        curr_len = 0
        stack = []

        split_n = input.split("\n")
        for s in split_n:
            files = s.split('\t')
            print(files)
            while len(stack) >= len(files):
                curr_len -= len(stack.pop())
            path = files[len(files) - 1]
            stack.append(path + '/')
            curr_len += len(path) + 1
            if path.index(".") >= 0:
                max_len = max(max, curr_len - 1)
        return max_len


solution = Solution()
solution.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
