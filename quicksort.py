def quick_sort(arr:list):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[0]
        less_than_pivot=[x for x in arr[1:] if x<=pivot]
        greater_than_pivot= [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) +[pivot]+quick_sort(greater_than_pivot)
arr=[3,5,1,6,3,7,3,8]
resut=quick_sort(arr)
print(resut)