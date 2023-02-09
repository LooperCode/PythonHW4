arr = [5,9,7,3,4,9]
max = 0
size = len(arr)
for i in range(len(arr)):
    sum = 0
    sum = arr[i%size] + arr[(i+1)%size] + arr[(i+2)%size]
    if sum > max:
        max = sum    
print(max)        