s="(]"
stack=[]
for i in range(len(s)):
    if(s[i]=='('or s[i]=='[' or s[i]=='{'):
        stack.append(s[i])
    elif(s[i] != 0 and s[i]==')'and stack[-1] == '(' or s[i]==']'and stack[-1] == '[' or s[i]=='}'and stack[-1] == '{' ):
        stack.pop()
    elif(stack[-1]==0 or s[i]==')'and stack[-1] != '(' or s[i]==']'and stack[-1] != '[' or s[i]=='}'and stack[-1] != '{' ):
        print("false")
if(stack == [] ):
    print("true")

