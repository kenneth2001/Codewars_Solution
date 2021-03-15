def dirReduc(arr):
    i = 0
    while (i < len(arr)-1):
        print(arr, i)
        if (arr[i] == 'NORTH' and arr[i+1] == 'SOUTH') or (arr[i] == 'SOUTH' and arr[i+1] == 'NORTH') or (arr[i] == 'EAST' and arr[i+1] == 'WEST') or (arr[i] == 'WEST' and arr[i+1] == 'EAST'):
            arr.pop(i)
            arr.pop(i)
            i = 0
        else:
            i += 1
    return arr
