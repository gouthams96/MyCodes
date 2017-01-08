import sys
string = sys.stdin.read()
temp = list(string)
temp.reverse()
reverse = "".join(temp)
if string==reverse:
	print("YES")
else:
	print("NO")
