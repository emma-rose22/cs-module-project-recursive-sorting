# quick sort
# better for larger scale

#halves the given data, allowing multiple tasks to happen simultaneously

# when writing a recursive algorithim:
# -- what is the case that will terminate the recursion?
# -- how will we move towards that termination case?

def partition(data):
    #created for use in quicksort, used to divide arrays
    
    #pick first element in data as pivot

    pivot = data[0]
    left = []
    right = []

    for x in data[1:]: #skip pivot
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return left, pivot, right

def quicksort(data):
    if len(data) == 0:
        return data

    #gives us our subarrays
    left, pivot, right = partition(data)

    #keep doing it and add them together
    return quicksort(left) + [pivot] + quicksort(right)


#OPTIMIZED VERSION 

def ip_partition(data, start, end):
    # pick the first element in data as our pivot 
    pivot = data[start]
​
    i = start + 1
    j = start + 1
    
    # partitioning step to move elements around the pivot 
    while j <= end:
        if data[j] <= pivot:
            data[j], data[i] = data[i], data[j]
            i += 1
        j += 1
​
    data[start], data[i - 1] = data[i - 1], data[start]
    # return the index of the pivot
    return i - 1
​
def ip_quicksort(data, start=0, end=None):
    if end is None:
        end = len(data) - 1
​
    # base case
    # if len(data) == 0:
    if start >= end:
        return
​
    # returns the index of the pivot 
    # and partitions the data around the pivot 
    index = ip_partition(data, start, end)
​
    # qs call for everything to the left of the pivot 
    ip_quicksort(data, start, index - 1)
    # qs call for everything to the right of the pivot 
    ip_quicksort(data, index + 1, end)


# Requires us to know the "max" value that we'll be sorting 
# The maximum was arg was so we could specify the max value 
# The total range of data we'll be sorting sits between 0 and maximum 
# O(max + n) 
# O(max) space complexity 
def counting_sort(arr, maximum=-1):
    if len(arr) == 0: #O(1)
        return arr #O(1)
    
    # if maximum is not given, we'll take the max value from the input array 
    if maximum == -1: #O(1)
        maximum = max(arr) #O(n)
​
    # make a bunch of buckets 
    buckets = [0 for _ in range(maximum+1)] #O(max)
​
    for x in arr: #O(n)
        if x < 0:
            return "Error, negative numbers not allowed"
        buckets[x] += 1 #O(1)
​
    # we have the counts of every value in our input array 
    # loop through our buckets, starting at the smallest index 
    # j keeps track of the spot we're writing to in our input array 
    j = 0
​
    # this whole loop is reversing the tallying we did in the previous loop 
​
    # max - n = diff 
    for i in range(len(buckets)): #O(max)
        while buckets[i] > 0: 
            arr[j] = i
            j += 1
            buckets[i] -= 1
​
    return arr
​
​
arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
​
print(counting_sort(arr1))