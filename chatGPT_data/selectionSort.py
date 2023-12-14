def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
arr = [64, 25, 12, 22, 11]
selectionSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])
