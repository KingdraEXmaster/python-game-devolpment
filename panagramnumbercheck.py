d1={}
while True:
    checkstring=input("Enter the number you want to check here ")
    for c in checkstring:
        if c.isdigit():
            if c in d1:
                d1[c]+=1
            else:
                d1[c]=1

    pangram=False


    if len(d1)==10:
        for values in d1.values():
            if values>0:
                pangram=True


    if pangram==True:
        print("Congrats, It's a number pangram")
    else:
        print("Not a number pangram")