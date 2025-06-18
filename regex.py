import re
s="John000Doe000123"
p=r"[0]"
a=("\n".join(re.split(p,s)))
b=a.split()
print(b)
d={}
d["first"]=b[0]
d["last"]=b[1]
d["id"]=b[2]
print(d)