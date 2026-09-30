d1={"idk":True,"hot":"fire","Sleep":False}
d1["hello"]="To say hi"
d1["Sleep"]=True
d1.pop("hot")
for key,value in d1.items():
    print(f"{key}:{value}")