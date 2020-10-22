# 4.  Find the maximum and minimum element in an array

def minmax(arr):
    max, min = arr[0], arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]

        if arr[i] < min:
            min = arr[i]

    return {"min": min, "max": max}


n = int(input("Enter size="))
arr = []
for i in range(n):
    arr.append(int(input("ENter element=")))
print(minmax(arr))
