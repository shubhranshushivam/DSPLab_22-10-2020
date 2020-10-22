# 8.  Find the Union and Intersection of the two sorted arrays

def union(arr1,arr2):
    res=arr1+arr2
    res=set(res)
    return list(res)

def intersection(arr1, arr2):
    res=[]
    for i in arr1:
        if i in arr2:
            res.append(i)
    return res

n1=int(input("Enter size of 1st array="))
arr1, arr2=[],[]
for i in range(n1):
    arr1.append(int(input("ENter element=")))

n2=int(input("Enter size of 2nd array="))
for i in range(n2):
    arr2.append(int(input("ENter element=")))
print("UNION=",union(arr1, arr2))
print("INTERSECTION=",intersection(arr1, arr2))