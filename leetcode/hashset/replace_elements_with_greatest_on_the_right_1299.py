class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        for i in range(len(arr)):
            try:
                arr[i] = max(arr[i+1:])
            except ValueError:
                arr[i] = -1
        return arr