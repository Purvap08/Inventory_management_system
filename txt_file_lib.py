import os
import json
inventory={}
filename="inventory_det.txt"
def rd():
    global inventory
    r=os.popen(f"type {filename}").read()
    if len(r) > 0:
        a=json.loads(r)
        inventory.update(a)
def wrt():
    os.system(f"break > {filename}")
    os.system(f"echo {json.dumps(inventory)} >> {filename}")
'''def clr():
    os.system(f"break > {filename}")'''