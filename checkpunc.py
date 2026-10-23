d1={".":0,"!":0,"?":0,",":0,":":0,";":0,"/":0}
checkstring=input("Copy paste the text you want to check here ")
for c in checkstring:
    if c in d1:
        d1[c]+=1

pernumber=d1["."]
print("You have "+str(pernumber)+" periods in your text")
excnumber=d1["!"]
print("You have "+str(excnumber)+" exclamation marks in your text")
qnumber=d1["?"]
print("You have "+str(qnumber)+" question marks in your text")
commanumber=d1[","]
print("You have "+str(commanumber)+" commas in your text")
colonnumber=d1[":"]
print("You have "+str(colonnumber)+" colons in your text")
seminumber=d1[";"]
print("You have "+str(seminumber)+" semicolons in your text")
slashnumber=d1["/"]
print("You have "+str(slashnumber)+" slashes in your text")