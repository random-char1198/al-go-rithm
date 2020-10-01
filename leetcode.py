#136
def singleNumber(nums):
    for item in nums:
        nums[0] ^= item
    return nums[0]
#Test for 136

"""
Explanation:
We want to find the number that only appear once in a list. So we can use bitwise operation
XOr is a great choice
Truth table for Xor:
0 0 => 0
1 0 => 1
0 1 => 1
1 1 => 0
We have an array [4,1,2,1,2] which can be translated to
[100,001,010,001,010]
1: 100
   001
=  101 which is 5

2: 101
   010
=  111 which is 7

3: 111
   001
   110 which is 6

4:110
  010
  100 which is 4 <= This is our solution
  TIME COMPLEXITY is linear
  so If A xor B  is 1 it means it appears once,
     If A xor B is 0 never appear or appear twice. In this probelm we consider it appear twice
"""
#217
def containsDuplicates(nums):
   nums.sort()
   for i in range(len(nums)-1):
      if(nums[i] == nums[i+1]):
         return True
   return False
def containsDuplicatesSet(nums):
   return len(nums) != len(set(nums))
   # Just use Set data structure and it will automitically removes duplicates
   # If there are not duplicates we will return true which means they are no duplicates

# def removeDuplicates(nums):
#    #iteration way
#    nums.sort() #first we need to sort them
#    for i in range(len(nums)-1):
#       if(nums[i] == nums[i+1]):
#          nums.pop(i)

# a = [1,1,1,2,3,4]
# print(removeDuplicates(a))

# 262
# def reverseLinkedList(Lis):
#    prev = None
#    while head:
#       tmp = head.next#Store tmp variable
#       head.next = prev# We want to reverse the referecne.1 -> 2 (1.next is 2 right?) We want to make it 2->1(2->next 1)
#       prev = head#Assign head to prev
#       head = tmp#Assign new nead


#509 fib
def fib(n):
   if n < 2:
      return n
   else:
      return fib(n-1) + fib(n-2)
print(fib(1))
print(fib(2))
print(fib(6))
def test():
   #TO DO: add unit test

   #136
   arr = [4,1,1,2,6]
   print("Single Number:")
   print("The array is: ",arr,"Output is:",singleNumber(arr))
   print("Test Result: Passed")#add automation
   #217
   
   print("Contains Duplicates:")
   print("The array is: ",arr,"Output is:",containsDuplicates(arr))
   print("Test Result: Passed")#add automation

   print("Contains Duplicates Set:")
   print("The array is: ",arr,"Output is:",containsDuplicatesSet(arr))
   print("Test Result: Passed")#add automation


### TO DO
#Unit Test
#Linked List