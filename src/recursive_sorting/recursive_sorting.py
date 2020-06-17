# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []

    a = 0
    b = 0 

    # merge them into pairs of two, sorted by value
    #  for the length of arrA:

    while a < len(arrA) and b < len(arrB):
        # compare index in a to index in b
        # whichever one is smaller is removed and added to merged arr
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        
        else:
            merged_arr.append(arrB[b])
            b += 1

        print()

    #  for the length of arrB:
        # check to see if arrA still has variables
        # if so, go by index as above 

    #  if anything is left in a or b:
    while a < len(arrA):
        merged_arr.append(arrA[a])
        a += 1

    while b < len(arrB):
        merged_arr.append(arrB[b])
        b += 1
        # recursion?

    # to merge two twos, look at the two smaller values and place them accordingly
    # then do the same with the larger values

    

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # break down the array into single, individual arrays
    # create base case - if len(arr) > 1, break it down once more and send it to the merge function
    if len(arr) > 1:

        middle = len(arr) // 2
        arrA, arrB = merge_sort(arr[:middle]), merge_sort(arr[middle:])
        arr = merge(arrA, arrB)
    

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    #I will need to use the same logic as above, but rearranging the same arr instead

    #create trackers for moving through the array itself
    a = 0
    l = 0
    m = 0
    r = 0

    #loop through array, while checking to see if l, m, and r belong in that spot
    #will have to switch variables to the index pos before the current view of array
    #while a < len(arr):
        #this base case isn't working, what can I do instead?
        #for loop?
    for i in range(len(arr)):
        if start < arr[a]:
            print('start')
            arr[a-1] = start
            l += 1
        if mid < arr[a]:
            print('mid')
            arr[a-1] = mid
            m += 1
        if end < arr[a]:
            print('end')
            arr[a-1] = end
            r += 1
        if arr[a] > arr[a+1]:
            print('array is being rearrnged')
            arr[a+1] = arr[a]
            a += 1

    #once the length of the array is done, we can check to see if the l, m, and r variables exist
    #and add the rest of the array 
    print(arr)
    while l < 1:
        arr[a + 1] = start[l]
        l += 1

    while m < 1:
        arr[a + 1] = mid[m]
        m += 1

    while r < 1:
        arr[a + 1] = end[r]
        r += 1
    
    while a < len(arr):
        arr[a+1] = arr[a]
        a += 1



    return arr


def merge_sort_in_place(arr, l, r):
    #divide in the middle 
    #create a middle with the l and r variables
    #call mergesort on the array itself w/ l and r variables (instead of making a new one)
    #merge them all together?

    if l < r:

        m = (l + r) // 2
        print(f'arr: {arr}, l: {l}, m: {m}, r: {r}')

        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)

        merge_in_place(arr, l, m, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr


numbers = [3, 5, 2, 4, 3, 8, 8, 5, 1]

print(merge_sort_in_place(numbers, 0, len(numbers)-1))