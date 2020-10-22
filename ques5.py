# 5.  Find the "Kth" max and min element of an array 

def minmax(arr,k):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return {"min":arr[k-1],"max":arr[len(arr)-k]}

n=int(input("Enter size="))
arr=[]
for i in range(n):
    arr.append(int(input("ENter element=")))
k=int(input("ENter kth element="))
print(minmax(arr,k))