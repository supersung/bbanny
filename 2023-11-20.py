import pandas as pd

""" df = pd.DataFrame([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]])
print(df)
print(df[1])
print(df[1][1])

data = {
    "x" : [10, 15, 20],
    "y" : [50, 55, 60],
    "z" : [100, 110, 120]
}

idx = ["x축", "y축", "z축"]

fr = pd.DataFrame(data, index=idx)

print(fr)
print(fr["x"])
print(fr.x)

dt = [[1,10,100],[2,20,200],[3,30,300]]
col = ["x","y","z"]
idx = ["x축","y축","z축"]

df = pd.DataFrame(data=dt,index=idx,columns=col)
print(df) """

""" from faker import Faker as fk
import os

temp = fk("ko-KR")
print(temp.name())
folder = "data/"

if not os.path.isdir(folder) :
    os.mkdir(folder)
    
with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")

with open(folder + "fktemp.csv", "a", newline='', encoding='utf8') as f :
    for i in range(30) :
		    f.write(temp.name() + "," + 
            temp.address() + "," + 
            temp.postcode() + "," + 
            temp.company() + "," + 
            temp.job() + "," + 
            temp.phone_number() + "," + 
            temp.email() + "," + 
            temp.user_name() + "," + 
            temp.ipv4_private() + "," + 
            temp.ipv4_public() + "," + 
            temp.catch_phrase() + "," + 
            temp.color_name() + "\n")
       """
      
import pandas as pd

""" folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target)

print(df.company == "박박정")

temp = df[df.postcode > 70000]
print(temp)

 
res = df[df.postcode > 70000][["name", "postcode"]]
print(res)
print(res.count())

temp = df.postcode.mean()
print(temp)

temp = df[df.color=="Ivory"].postcode.mean()
print(temp)

temp = df[df.postcode > df.postcode.mean()]["name", "postcode"]
print(temp)

temp = df.company.empty()
print(temp)

temp = df[df.company.isnull()]["name", "postcode"]
print(temp)

temp = df.company.isnull()
for el in temp :
    if el == True :
        print(el)
temp = df[(df.color == "Ivory")][("name")]
print(temp.color.count())

temp = df.sort_values("postcode", ascending = False)
print(temp) """


""" import pandas as pd
col = ['Machine','Country','Price','Brand']
data = [['TV','Korea',1000,'A'],
        ['TV','Japan',1300,'B'],
        ['TV','China',300,'C'],
        ['PC','Korea',2000,'A'],
        ['PC','Japan',3000,'E'],
        ['PC','China',450,'F']]
df = pd.DataFrame(data=data, columns=col)
print(df)
dff = df.pivot(index='Machine',columns='Country',values='Price')
print(dff)
print(df.pivot())

 """
