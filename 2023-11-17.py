import pandas as pd
""" df = pd.DataFrame([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]])
print(df)

print(df[1])
print("\n--------------------\n")

print(df[1][1])
print("\n---------------------\n") """


""" data = {
    "x" : [10, 15, 20],
    "y" : [50, 55, 60],
    "z" : [100, 110, 120]
}

idx = ["x축", "y축", "z축"]

fr = pd.DataFrame(data, index=idx)
print(fr)
print("\n--------------------\n")
print(fr["x"])
print("\n--------------------\n")
print(fr.x)
print("\n--------------------\n")
print(fr.iloc[2])

frs = pd.DataFrame(fr,columns=["x", "y", "z", "t"])
frs["t"] = [60, 120, 180]
print(frs)
print("\n--------------------\n")

frs.loc["t축"] = [100, 200, 300, 400]
print(frs)

frs.loc["t축"] = [500, 600, 700, 800]
print(frs)

frs.drop("x", axis=1, inplace=True)
print(frs)

frs.drop("x축", inplace=True)
print(frs) """

import pandas as pd

""" dt = [[1,10,100],[2,20,200],[3,30,300]]
col = ["x","y","z"]
idx = ["삼성","현대","LG"]

df = pd.DataFrame(data=dt,index=idx,columns=col)
print(df)
print(df["x"])

print(df+1)
print(df.div(100))
print(df.mul(100))


# 같은 인덱스끼리 연산
dt2  = [[0],[2],[3]]
df2 = pd.DataFrame(data=dt2,index=["x축","y축","z축"],columns=["y"])

print(df2)
print(df.div(df2))
print(df.div(df2, fill_value=1))
print(df.loc["현대"])
print(df.div(df2,fill_value=100))
 """
import pandas as pd

""" idx = [('row1', 'val1'), ('row1', 'val2'), ('row2', 'val1'), ('row2', 'val2'), ('row2', 'val3'), ('row3', 'val2'),('row3', 'val3')]
dt = [ [1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18], [19,20,21]]

ind = pd.MultiIndex.from_tuples(idx)
df = pd.DataFrame(dt, columns=['col1', 'col2', 'col3'], index = ind)

print(df)

print(df.loc["row1"])
print("\n--------------------\n")
print(df.loc[("row3", "val3"), "col1"])
print("\n--------------------\n") """

import numpy as np

dt = np.random.randint(10, size=(5, 5))
df = pd.DataFrame(dt)

""" print(df)
print("\n--------------------\n")
print(df[2])
print("\n--------------------\n")
print(df.head(3))

print("\n--------------------\n")
print(df.tail(3))

print("\n--------------------\n")
print(df.sample(3))
 """

from faker import Faker as fk
import os

temp = fk("ko-KR")
print(temp.name())

folder = "c:\Users\Catholic\bbanny"
if not os.path.isdir(folder):
    os.mkdir(folder)
    
with open(folder + "fktemp.csv", "w", encoding='utf8') as f :
    f.write("name,address,postcode,company,job,phone,email,id,ip_prv,ip_pub,catch_parase,color\n")


with open(folder + "fktemp.csv", "w", newline='', encoding='utf8') as f :
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
 """
import pandas as pd

folder = "data/"
target = folder + "fktemp.csv"

df = pd.read_csv(target)
print(df[1])


print("\n--------------------\n")
print(df.head())

print("\n--------------------\n")
print(df.head(3))

print("\n--------------------\n")
print(df.tail())

print("\n--------------------\n")
print(df.tail(3))

print("\n--------------------\n")
print(df.index)

print(df.dtypes)

print(df.values)
print(df.values[1])

for el in df.values[0] :
    print(el)

print(df.info())

print(df.values)
print(df.isnull())

print(df.name)
print(df.postcode)

print(df.color)
print(df["name"])
print(df["color"])


