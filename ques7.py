# Move all the negative elements to one side of the array 

def move(arr):
    idx=0
    for i in range(len(arr)):
        if arr[i]<0:
            arr[i],arr[idx]=arr[idx],arr[i]
            idx+=1
    return arr

n=int(input("Enter size="))
arr=[]
for i in range(n):
    arr.append(int(input("ENter element=")))
print(move(arr))