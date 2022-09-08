class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack, dict_r = [], {}
        dict_r = {i: -1 for i in nums2}
        res = []
        for item in nums2:
            while stack and item > stack[-1]:
                # stack[-1] will the top of the stack.
                val = stack.pop()
                dict_r[val] = item
            # if current item is not smaller than the top of the stack.
            # it will be kept in the stack and the value of that key should remain -1
            # This line gets to execute when the stack is empty.
            stack.append(item)
        print(dict_r)
        for i in nums1:
            res.append(dict_r[i])
        return res


solution = Solution()
print(solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
