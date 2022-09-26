arr = [[0]*5 for _ in range(5)]
arr[0][0] = [[1,2]]
arr[0][0].append([3,4])
print(arr[0][0])
print(arr[0])