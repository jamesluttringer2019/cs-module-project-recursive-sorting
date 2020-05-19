# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    a = 0
    b = 0
    ind = 0
    while a<len(arrA) and b<len(arrB):
        if arrA[a]<=arrB[b]:
            merged_arr[ind] = arrA[a]
            a +=1
        else:
            merged_arr[ind] = arrB[b]
            b+=1
        ind+=1

    while a<len(arrA):
        merged_arr[ind] = arrA[a]
        a += 1
        ind += 1
    
    while b<len(arrB):
        merged_arr[ind] = arrB[b]
        b+=1
        ind+=1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]

        l = merge_sort(l)
        r = merge_sort(r)

        arr = merge(l,r)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    rstart = mid + 1
    # check if already in order
    if arr[mid]<=arr[rstart]:
        return
    
    while (start<=mid and rstart<=end):
        if arr[rstart] <= arr[start]:
            val = arr[rstart]
            ind = rstart
            while ind != start:
                arr[ind] = arr[ind-1]
                ind -= 1
            arr[start] = val

            mid += 1
            start += 1
            rstart += 1
        else:
            start += 1
            
    return arr


def merge_sort_in_place(arr, l=0, r=None):
    if r == None:
        r = len(arr)-1

    if l < r:
        m = (l+r)//2
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m+1, r)

        merge_in_place(arr, l, m, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
