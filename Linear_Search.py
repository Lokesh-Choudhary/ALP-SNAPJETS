pos=-1
def linearsearch(list,n):
    i=0
    for i in range(i<len(list)):
        if list[i]==n:
           globals() ['pos']=i
           return True 
           i+=1
    return False 
list=[6,9,7,4,2,1,0]
n=6
if linearsearch(list,n):
    print("Found at",pos)
else:
    print("Not Found")
