s = "(]"
for i in range(0,len(s),2):
            if(s[i]=='(' and s[i+1]==')' or s[i]=='[' and s[i+1]==']' or s[i]=='{' and s[i+1]=='}'):
                x=1
            else:
                x = 0
if x == 1:
      print("true")
else:
       print("false")