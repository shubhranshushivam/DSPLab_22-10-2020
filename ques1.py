# 1.Write a program to find the max element of an array and swap it with the last unsorted value of the array.

def swap(arr):
    n=len(arr)
    for i in range(n):
        max=0
        for j in range(n-i):
            if arr[j]>arr[max]:
                max=j
                # print(arr[index])
        arr[n-i-1],arr[max]=arr[max],arr[n-i-1]
        print("Processing=",arr)
    return arr

n=int(input("Enter size="))
arr=[]
for i in range(n):
    arr.append(int(input("ENter element=")))
print("After Sorted=",swap(arr))
