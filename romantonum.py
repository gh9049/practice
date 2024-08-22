s="MCMXCIV"
dict={          'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000
    }
result=0
for i in range(len(s)):
    if i==0:
        result+=dict[s[i]]
    elif dict[s[i-1]]>=dict[s[i]]:
        result+=dict[s[i]]
    elif dict[s[i-1]]<dict[s[i]]:
        result+= dict[s[i]]-2*dict[s[i-1]]
print(result)