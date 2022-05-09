import time
import json
x={"first":["bale","casemiro","modric","navas","varane","kroos"]}
with open("real_madrid.txt",'w') as f:
    f.write(json.dumps(x))


