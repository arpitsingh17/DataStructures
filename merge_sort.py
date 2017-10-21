def MergeSort(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid = int(len(lst)/2)
        left = MergeSort(lst[:mid])
        right = MergeSort(lst[mid:])
        return Merge(left,right)

def Merge(left,right):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

print MergeSort([4,3,7,1,2,6,3,8,0,4,9])
