strs=["flower","flow","flight"]
strs=sorted(strs)
ans=""
for i in range(min(len(strs[0]),len(strs[-1]))):
    if(strs[0][i] != strs[-1][i]):
        print(ans)
        break
    ans+=strs[0][i]