# num=9
# while(num>=0):
#     i=num
#     while(i>1):
#         i=i-2
#         print(i,end=" ")
#     num=num-2
#     print("\n") if num>0 else print('0')



n=5
m=7
for i in range(n,1,-1):
    for j in range(m,0,-1):
        if j%2 !=0:
            print(j, end=" ")
    m=m-2
    print("\n") if n>0 else print('0')