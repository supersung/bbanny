import os

""" fp = "temp.txt"

if os.path.exists(fp) :
    f = open(fp,"r")
    for line in f:
        print(line)
else :
    f = open(fp,"w")
    for i in range(100) :
        f.write(str(1) + "\n")
    print("error")

f.close()
 """
 
 
""" def dir_print(p):
    files = os.listdir(p)
    for f in files :
        print(f)
        
        
fp = "new.txt"

f = open(fp,"w")
f.close()

dir_print("./")

os.remove(fp)
print("------------------\n\n")
dir_print("./") """


""" import os

fp = "new.txt"

f = open(fp, "w")
f.close()

os.rename(fp,"new1.txt")
print("complete")
 """
 
""" import os

fp = "new.txt"
tp = "new1.txt"

f = open(fp,"w")
f.close()

if os.path.exists(tp) :
    print("exist, same name file")
    os.remove(tp)
    
else :
    os.rename(fp, "new1.txt")
    print("complete") """
    
    
import os

""" def dir_print(p) :
    files = os.listdir(p)
    for f in files :
        print(f)
        
fp = "new.txt"
tp = "new1.txt"

f = open(fp,"w")
f.close()
    
dir_print("./")
print("===============")


if os.path.exists(tp) :
    os.remove(tp)
    dir_print("./")
    print("exist, same name file")
    
    
else :
    os.rename(fp, "new1.txt")
    dir_print("./")
    print("complete")  """
    
    
""" with open("temp.txt","r") as f :
    print(f.read()) """
