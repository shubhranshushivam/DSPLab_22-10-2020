# 6.  Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo.

def sort(arr):
    count0,count1,count2=0,0,0
    for i in arr:
        if i==0:
            count0+=1
        if i==1:
            count1+=1
        if i==2:
            count2+=1
    res1=[0]*count0
    res2=[1]*count1
    res3=[2]*count2
    res=res1+res2+res3
    return res 

n=int(input("Enter size="))
arr=[]
for i in range(n):
    arr.append(int(input("ENter element=")))
print(sort(arr))