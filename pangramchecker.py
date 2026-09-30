d1={}
checkstring=input("Enter the text you want to check here ")
for c in checkstring:
    if c.isalpha():
        if c in d1:
            d1[c]+=1
        else:
            d1[c]=1

pangram=False


if len(d1)==26:
    for values in d1.values():
        if values>0:
            pangram=True


if pangram==True:
    print("Congrats, It's a pangram")
else:
    print("Not a pangram")