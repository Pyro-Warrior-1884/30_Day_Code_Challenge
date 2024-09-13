n = int(input("Enter Size: "))
arr = [0 for _ in range(n)]
for i in range(n):
    arr[i] = int(input())

max_num = 0 
leader = []
for i in range(len(arr)-1,-1,-1):
    if max_num < arr[i]:
        max_num = arr[i]
        leader.insert(0, arr[i])
print(leader)

    