from functools import reduce
#Decalre a list
urlist=[]
print("Enter 6 Numbers:\n")
for i in range(6):
    element = int(input())
    urlist.append(element)

print(urlist)
#Make list woth 3*a[i]
ur2list = [(lambda x: 3*x) (x) for x in urlist]
print(ur2list)
#Sum of list using lamba and reduce
print(reduce(lambda a,b:a+b,urlist))
