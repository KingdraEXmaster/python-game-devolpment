d1={}
checkstring=input("Copy Paste the text you want analytics on here ")
for c in checkstring:
    if c in d1:
        d1[c]+=1
    else:
        d1[c]=1

print("Here are you analytics on how many times you use different characters")
print(d1)