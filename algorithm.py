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

    # Output:
    # Before:  [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # After:  [17, 20, 26, 31, 44, 54, 55, 77, 93]