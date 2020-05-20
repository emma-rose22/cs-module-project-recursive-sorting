# # TO-DO: complete the helper function below to merge 2 sorted arrays
# def merge(arrA, arrB):
#     elements = len(arrA) + len(arrB)
#     merged_arr = []

#     #merge two sorted arrays

#     i = 0
#     j = 0

#     while i < len(arrA) and j < len(arrB):
#         #check if first element is smaller in first array than second
#         if arrA[i] < arrB[j]:
#             merged_arr.append(arrA[i])
#             i += 1
#         #if it isn't, append the value from B instead
#         else:
#             merged_arr.append(arrB[j])
#             j += 1

#     #until we are done (incrementing i to know if we went through 
#     #the whole list)
#     #elements that weren't sorted above are already 
#     #less than b, but bigger than the a values already sorted
#     #so we can add all of them 
#     while i < len(arrA):
#         merged_arr.append(arrA[i])
#         i += i

#     #same idea here, all the elements w/ merge conflicts
#     #have been taken care of, leaving only elements safe to 
#     #append in order, no conflict from A
#     while j < len(arrB):
#         merged_arr.append(arrB[j])
#         j += 1

#     return merged_arr

# a = [1, 2, 3]
# b = [4, 5, 6]

#print(merge(a, b))

#LESSON CODE 

def merge(A, B):
    # init the combined list of A and B
    #combined = [0 for _ in range(len(A) + len(B))]
    combined = []

    #init the two pointers that start at each list

    a = 0
    b = 0

    while a < len(A) and b < len(B):
        # compare the elements that a and b point at
        if A[a] < B[b]:
            combined.append(A[a])
            a+=1

        else:
            combined.append(B[b])
            b+=1

    #at this point, we have finished traversing one of the lists
    # we don't know which one, as the while breaks if either finishes

    #we need to add the remaining elements to the combined list

    #only one of these loops will be used
    while a < len(A):
        combined.append(A[a])
        a +=1

    while b < len(B):
        combined.append(B[b])
        b+=1

    return combined

# # TO-DO: implement the Merge Sort function below USING RECURSION
# def merge_sort(arr):
#     #first, divide in half until subarrays of 1
#     print('arr:', arr)
#     arrA = []
#     arrB = []
#     #can't sort a list of one
#     if len(arr) > 1:

#         #get the middle of the list
#         half_len = len(arr)//2
#         #get the left half
#         print('half len:', half_len)
#         arrA = arr[:half_len]
#         print('arrA:', arrA)
#          #get the right half
#         arrB = arr[half_len:]
#         print('arrB;', arrB)

#     #we want to keep doing this until our values have 
#     #individual arrays

#         merge_sort(arrA)
#         merge_sort(arrB)

    
#     #second, merge the lists together using function
#         arr = merge(arrA, arrB)


#     return arr

# arr = [5, 3, 8, 6, 9, 2, 3, 10]

#print(merge_sort(arr))

#LESSON CODE 

def merge_sort(arr):
    #break the array down recursively
    #base case: when the lists have length of one
    # merge them back up

    if len(arr) > 1:
        left = merge_sort(arr[:len(arr)//2])
        right = merge_sort(arr[len(arr)//2:])
        arr = merge(left, right)

    return arr

arr = [5, 3, 8, 6, 9, 2, 3, 10]

print(merge_sort(arr))



# implement an in-place merge sort algorithm
def merge_in_place(A, B): #originally also had start, mid, end
    # instead of making empty array, arrange new array
    # pick one array to be added to
    # lets always add to A

    a = 0
    b = 0

    # go through the first array and compare each value 
    #to the first value in the second

    #two counters
    # -- one iterates through the first list, continuously
    # -- second only is increased if added into initial array

    while a < len(A) and b < len(B):
        # print('first A:', A[a])
        # print('first B:', B[b])
        # print('A pointer:', a)
        # print('B pointer:', b)
        # print('Current array:', A)
        if A[a] >= B[b]:
            a += 1
            A.insert(a - 1, B[b])
            b += 1
        else:
            a += 1

    # once the array being added to is done,
    # anything left in the second array can just be appended on
    while b < len(B):
        A.append(B[b])
        b +=1

    return A

A = [1, 2, 3, 7, 9, 22]
B = [2, 3, 4, 5, 6, 7, 8]

print(merge_in_place(A, B))


def merge_sort_in_place(arr, l, r):
    if len(arr) > 1:
        left = merge_sort(arr[:len(arr)//2])
        right = merge_sort(arr[len(arr)//2:])
        arr = merge(left, right)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
