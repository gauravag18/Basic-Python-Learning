p1="subscribe"
p2="like"
p3="share"
message=input("enter your comment")
if(p1 in message or p2 in message or p3 in message):
    print("scam")
else:
    print("genuine")