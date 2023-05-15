s = str(input())

if int(len(s)) >= 3:
    if s[::-3] != "ing":
        s=list(s)
        s.append("ing")
    else:
        s=list(s)
        s.append("ly")
else:
    s = s
for i in s:
    print(i,end="")