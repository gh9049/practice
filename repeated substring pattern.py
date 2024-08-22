s = "abab"
s_fold = "".join( (s[1:], s[:-1]) )
print(s in s_fold)
