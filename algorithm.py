def insertion_sort(L):
    number = len(L)
    if number <= 1:
        return
    #If n is <= 1 it means there is 1 or 0 elments
    #else start for loop, there are two loops, so worst time complexity is n^2, however if we were only swaping 2 elements then it would be n
    for i in range(1, number): 
        j = i
        while j >= 1 and L[j] < L[j-1]:# if statment only works if current element is less than current index - 1
            L[j], L[j-1] = L[j-1], L[j]# swaping two elements
            j -= 1 # decrase j by 1
    #every time while loop finishes, j will be reassigned a new value wihch is new i value in the outter loop
def linear_search(List,item):#Time complexity for linear search is o(n)
    for i in List:
        if i == item:
            return True
    return False
def sum(list):
    sumTotal = 0
    for item in list:#o(n)
        sumTotal += item #o(1)
    return sumTotal
def sum_Rec(list):
    if len(list) < 1    :
        return 0
    return list[0] + sum_Rec(list[1:])#linear recursion o(1) * (n+1) = o(n)


def rmv_dup(test_list):#remove depulicates from a list o(n)
    res = [] 
    for i in test_list: 
        if i not in res: 
            res.append(i)
    return res
def removeSecondLargest():#remove second largest number in the list
    arr = list(map(int, input().split()))
    new = rmv_dup(arr)
    new.remove(max(new))
    newlst = new
    print(max(newlst))
    
#reverse a string using recursion
def reverseRecursion(str):
    if len(str) == 0:
        return
    tempLetter = str[0]
    reverseRecursion(str[1:])
    print(tempLetter, end='') 
#Input = "12345"
#It will be constructed like this:
#       1 is stored in tempLetter, and slice string using [1:] keep everything but the first letter len 4
#       2 is stored in tempLetter, and slice string using [1:] keep everything but the first letter len 3
#       3 is stored in tempLetter, and slice string using [1:] keep everything but the first letter len 2
#       4 is stored in tempLetter, and slice string using [1:] keep everything but the first letter len 1
#       5 is stored in tempLetter, and slice string using [1:] keep everything but the first letter => reach base case
# STOP recrusion => 5 will be printed at first, then the rest will be printed in a reverse order
# Slice is very powerful


def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year %% 400:
                leap = True
            else
                leap = False
        else
            leap = True
    else
        leap = False
    return leap
#simple control flow to determintes whether a year provied is a leap year
#if a year modulo 4 == 0, year module 100  == 0 and a year modulo 400 
if __name__ == '__main__':

    list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print('Before Insertion sort: ', list)
    insertion_sort(list)

    print('After Insertion sort: ', list)
    print("We are trying to look for 31 in:",list)
    bol = linear_search(list,333)
    print("It is in our list:",bol)

    print("We are trying to look for 55 in:",list)
    bol = linear_search(list,55)
    print("It is in our list: ",bol)

    print("Normal: ",sum(list))
    print("Recursion: ",sum_Rec(list))
    # Output:
    # Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # After:  [17, 20, 26, 31, 44, 54, 55, 77, 93]
    string = "1 2 3 4 5 6"
    print(string)
    reverseRecursion(string)
    print("\n")
    
   # Hello World program in Python
#Bubble Sort Time Complexity => n^2
def bubbleSort(lis):
    for i in range(len(lis)-1):
        for j in range(len(lis)-i-1):
            if(lis[j]>lis[j+1]):
                lis[j],lis[j+1] = lis[j+1],lis[j]#swaping two elements if current element is great than next element.
    return lis

lis = [7,6,5,4,3,2,1]
print(bubbleSort(lis))
