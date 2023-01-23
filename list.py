# l1=[]
# l1.append([1,2,3,4,5])
# l1.append("ashish")
# print(l1)

# l2=[]
# l2=[i for i in range (1,11,2)]
# print(l2)

a=int(input("Enter value of a"))
b=int(input("Enter value of b"))
c=int(input("Enter value of c"))
n=int(input("Enter value of n"))

list=[[i,j,k] for i in range(a+1) for j in range(b+1) for k in range(c+1) if (i+j+k!=n)]
# for i in range (a+1):
#     for j in range(b+1):
#         for k in range(c+1):
#             if(i+j+k!=n):
#                 list.append([i,j,k])


print(list)
