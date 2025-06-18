x=input().split("=")
y=input().split("=")
x=eval(str(x[-1]))
y=eval(str(x([-1]))
la=[]
lb=[]
for i in range(len(x)):
    la.append(x[i][0])
    lb.append(x[i][1])
ct=0
for u in la:
    z=lb.count(u)
    p=la.count(u)
    if z>2*p:
       print(u)
       ct+=1
if ct==0:
    print("No Influencers Found")