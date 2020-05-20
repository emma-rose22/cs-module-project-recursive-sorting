# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    #merge two sorted arrays

    i = 0
    j = 0
    k = 0

    while i < len(arrA) and j < len(arrB):
        #check if first element is smaller in first array than second
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            k +=1
            i += 1
        #if it isn't, append the value from B instead
        else:
            merged_arr[k] = arrB[j]
            k += 1
            j += 1

    #until we are done (incrementing i to know if we went through 
    #the whole list)
    #elements that weren't sorted above are already 
    #less than b, but bigger than the a values already sorted
    #so we can add all of them 
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        k += 1
        i += i

    #same idea here, all the elements w/ merge conflicts
    #have been taken care of, leaving only elements safe to 
    #append in order, no conflict from A
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        k += 1
        j += 1

    return merged_arr

# a = [1, 2, 3]
# b = [4, 5, 6]

# print(merge(a, b))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    #first, divide in half until subarrays of 1
    print('arr:', arr)
    arrA = []
    arrB = []
    #can't sort a list of one
    if len(arr) < 2:

        #get the middle of the list
        half_len = len(arr)//2
        #get the left half
        print('half len:', half_len)
        arrA = arr[:half_len]
        print('arrA:', arrA)
         #get the right half
        arrB = arr[half_len:]
        print('arrB;', arrB)

    #we want to keep doing this until our values have 
    #individual arrays

        merge_sort(arrA)
        merge_sort(arrB)

    
    #second, merge the lists together using function
    arr = merge(arrA, arrB)

    return arr

arr = [5, 3, 8, 6, 9, 2, 3, 10]

print(merge_sort(arr))


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
