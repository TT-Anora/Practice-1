arr = [8,9,1,2,3,4,5,6]
target = 7
targetPairs = []
sum = 0

def func(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        if arr[left] + arr[right] > target:
            right-=1
        elif arr[left] + arr[right] < target:
            left+=1
        elif arr[left] + arr[right] == target:
            targetPairs.append((arr[left],arr[right]))
            left+=1
            right-=1
arr.sort()
func(arr, target)
print("Pairs: ", targetPairs)

