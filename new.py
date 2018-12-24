s = [int (a) for a in input().split()]
s1= [int (b) for b in input().split()]
s2=[]
s3=[]
s2=s+s1
for item in s2:
    b=s2.count(item)
    if(b>=2):
        s3.append(item)
print(s3)
l=len(s3)
a=int(l/2)
for i in range(a):
    print(str(s3[i]))
    
