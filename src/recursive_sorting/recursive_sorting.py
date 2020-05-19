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
    # counter = 0
    # while len(merged_arr) == len(arrA) + len(arrB):
    #     for i in arrA:
    #         if arrA[i] <= arrB[i]:
    #             merged_arr[i] = arrA[i]
    #             #merged_arr[i+1] = arrB[i + 1]
    #             print('hi')
    #             counter += 1
            
    #         else:
    #             merged_arr[i] = arrB[i]
    #             #merged_arr[i+1] = arrA[i + 1]
    #             print('hello')
    #             counter += 1
    # print(counter)

    return merged_arr

# a = [1, 2, 3]
# b = [4, 5, 6]

# print(merge(a, b))

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    #first, divide in half until subarrays of 1
    print('arr:', arr)
    #can't sort a list of one
    if len(arr) < 2:
        return arr

    half_len = len(arr)//2
    print('half len:', half_len)
    arrA = arr[:half_len]
    print('arrA:', arrA)
    arrB = arr[half_len + 1 : len(arr)]
    print('arrB;', arrB)
    arr = merge(merge_sort(arrA), merge_sort(arrB))
    
    #second, merge the lists together using functio

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
