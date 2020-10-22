# 3.  Reverse the array with using loops

def arrReverse(arr):
    arrTemp=[]
    n=len(arr)
    for i in range(len(arr)):
        arrTemp.append(arr[n-i-1])

    return arrTemp

n=int(input("Enter size="))
arr=[]
for i in range(n):
    arr.append(int(input("ENter element=")))
print(arrReverse(arr))