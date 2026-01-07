import json
import os
filename="bill.txt"
r=os.popen(f"type {filename}").read()
inv_no=[]
#a=json.loads(r)
#print(a)
r1=r.splitlines()
for line in r1:
    data=json.loads(line)
    #print(data)
    for i in data:
        if i != "date-time":
            inv_no.append(int(i))
#max_inv=i 
#print(max_inv)  
def billrd():
    if len(inv_no)>0:
        return max(inv_no)  
        #print(max_inv)
    else :
        max_inv=0
#billrd()   