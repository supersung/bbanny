
""" import pandas as pd
tr = pd.read_csv("data/train.csv")

#print(tr)
print("\n----------------------\n")


res = tr.isnull().sum()
#print(res)

##승선지
#print("\n----------------\n")
res=pd.crosstab(tr["Embarked"], tr["Srvived"])
print(res)

#res.columns = res.columns.map({0:"Dead", 1:"Alive"})
#print(res)

##연령
#print("\n---------------------\n")
pd.crosstab(tr["Age"], tr["Survived"])
#print(res)

res.columns = res.columns.map({0:"Dead", 1:"Alive"})
#print(res)

##passenger class
#print("\n---------------------\n")
#res = pd.crosstab(tr["Pclass"], tr["Survived"])
#print(res)

#성별별
#print("\n---------------------\n")
res=pd.crosstab(tr["Sex"], tr["Survived"])
# print(res)

#print("\n---------------------\n")
tr["Title"] = tr.Name.str.extract(" ([A-Za-z]+)\.")
# print(res)

tr["Title"] = tr["Title"].replace(["Capt", "Col", "Countess", "Don","Dona", "Dr", "Jonkheer", "Lady","Major", "Rev", "Sir"], "Other")
tr["Title"] = tr["Title"].replace("Mlle", "Miss")
tr["Title"] = tr["Title"].replace("Mme", "Mrs")
tr["Title"] = tr["Title"].replace("Ms", "Miss")
res = tr["Title"].value_counts()

#print(res)

#print(tr["Age"].isnull())
#print(tr["Age"].isnull().sum)

meanAge = tr[["Title", "Age"]].groupby(["Title"]).mean()
print(meanAge)
#print(tr["Age"].head(20))

#print("\n---------------------\n")

for index, row in meanAge.iterrows():
    nullIndex = tr[(tr.Tittle == index) & (tr.Age.isnull())].index
    # print(nullIndex, index, row[0])
    tr.loc[nullIndex, "Age"] = row[0]

#print(tr)

print(tr["Age"].head(20))
#print(tr["Age"].isnull().sum())

tr["AgeCaate"]=pd.qcut(tr.Age, 8, labels=range(1,9))
#print(tr.head())
#print(tr.dtypes)
#print("\n---------------------\n")

tr.AgeCate = tr.AgeCate.astpe(int)
#print(tr.head())
#print(tr.dtypes)

#tr.Cabin.fillna("N", inplace=True)
tr["CabinCate"]=tr["Cabin"].str.slice(start=0, stop=1)
#print(tr["CabinCate"].value_counts())

tr["CabinCate"] = tr["CabinCate"].map({ "N": 0, "C": 1, "B": 2, "D": 3, "E": 4, "A": 5, "F": 6, "G": 7, "T": 8 })
#tr.CabinCate = tr.CabinCate.asty
#print(tr.dtypes)
#print(tr)
#print(tr["CabinCate"].value_counts())

res = pd.crosstab(tr["CabinCate"], tr["Survived"])
#print(res)

##요금
print(tr.Fare)
#print("\n---------------------\n")

##print(tr["Fare"].value_counts())

tr["FareCate"] = pd.qcut(tr.Fare, 8, labels=range(1, 9))
#tr.FareCate = tr.FareCate.astype(int)
#tr.FareCate = tr.FareCate.awstpe(int)
print(tr["FareCate"].value_counts())

res = pd.crosstab(tr["FareCate"], tr["Survived"])
print(res)



#아이리스 전처리

import pandas as pd

df = pd.read_csv("./data/Iris.csv", index_col="Id")
print(df.head())

#df.rename(columns={
#    "SepalLengthCm": "꽃받침길이",
#    "SepalWidthCm": "꽃받침너비",
#    "PetalLengthCm": "꽃잎길이",
#    "PetalWidthCm": "꽃잎너비", 
#    "Species": "품종"},
#    inplace=True
#)

ir = df.rename(columns={
    "SepalLengthCm": "꽃받침길이",
    "SepalWidthCm": "꽃받침너비",
    "PetalLengthCm": "꽃잎길이",
    "PetalWidthCm": "꽃잎너비", 
    "Species": "품종"},
)
print(ir.head())

#print("\n---------------------\n")
res= ir.iloc[:, [0, 1, 4]]
print(res)



ir["품종"] = ir["품종"].str[5:]
print(ir)

res = ir.groupby("품종").mean()
print(res)


res=ir["품종"].value_counts()
print(res)



import matplotlib.pyplot as plt

#기본사용y

value = [1, 2, 3, 4]
#value = [2, 4, 5, 7, 10]
res = plt.plot(value)
plt.show()

#두 축 지정 구성
x_value = [2, 3, 6, 7, 10 ]
y_value = [1, 4, 5, 8, 9]

plt.plot(x_value, y_value)
#res = plt.plot([2,4,6,8,10], [1,3,5,7,9])
plt.show()

#딕셔너리 설정

dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val)

plt.xlabel("x_data", labelpad=15)
plt.ylabel("y_data", labelpad=50)

#plt.xlabel("x_data",labelpad=15, loc="right")
#plt.ylabel("y_data",labelpad=50, loc="top")

#### 다중데이터 출력

dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,10]}

plt.plot("x_data", "y_data", data=dic_val)
plt.plot("x1_data", "y1_data", data=dic1_val)

plt.xlabel("x_data")
plt.ylabel("y_data")

plt.show()

#위치조절

dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

plt.plot("x_data", "y_data", data=dic_val, label="PData(km)")
#plt.plot([1,4,5,9], [2,3,8,10])
plt.xlabel("x_data")
plt.ylabel("y_data")

#plt.legend(loc=(1, 1))
#plt.legend(loc="best")


#plt.legend(loc=(0.5, 0.5))
#plt.legend(loc=(0.3, 0.))




#plt.legend(loc="lower right")
#plt.legend(loc="center right")
#plt.legend(loc="upper right")
#plt.legend(loc="upper left")
plt.legend(loc="upper center")

plt.show()


#위치조절

dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}
dic1_val = {"x1_data": [1,3,5,7,9], "y1_data": [2,4,6,8,9]}

plt.plot("x_data", "y_data", data=dic_val, label="PData(km)")
plt.plot("x1_data", "y1_data", data=dic_val, label="PData(km)")
#plt.plot([1,4,5,9], [2,3,8,10])
plt.xlabel("x_data")
plt.ylabel("y_data")

#col조절

#plt.legend(ncol=1)
#plt.legend(ncol=2)

#폰트 조절
#plt.legend(ncol=2, fontsize=10)
#plt.legend(ncol=2, fontsize=20)

#테두리 설정
## plt.legend(ncol=2, fontsize=20, frameon=True)
# plt.legend(ncol=2, fontsize=20)
plt.legend(ncol=2, fontsize=20, frameon=False)


dic_val = {"x_data": [2,3,6,7,10], "y_data": [1,4,5,8,9]}

#plt.plot("x_data", "y_data", data=dic_val)
#plt.xlabel("x_data")
#plt.ylabel("y_data")

#plt.xlim()
#plt.ylim()

#축 범 위 출력
#x_min, x_max = plt.xlim()
##print(x_min, x_max)
#print(y_min, y_max)

#축 계산
#plt.xlim(x_min - 0.6, x_max)
#plt.ylim(y_min - 0.6, y_max)

#축 범위 지정
#plt.xlim([0, 10])
#plt.ylim([0, 10])

#plt.xlim([0, 50])
#plt.ylim([0, 50])

#plt.xlim([-5, 50])
#plt.ylim([5, 50])

#plt.xlim([0, 10])
#plt.ylim([0, 10])
#plt.axis([0,10,0,10])

#plt.xlim([-5, 50])
#plt.ylim([5, 50])
#plt.axis([-5, 50, 5, 50])

x_min, x_max, ymin, ymax = plt.axis()
print(x_min, x_max, ymin, ymax)
plt.axis([x.min, x.max, y.min, y.max])

plt.axis("square")
plt.axis("scaled")
plt.axis("tight")
plt.axis("on")
plt.axis("off")
plt.axis("equal")
plt.axis("auto")


#선
plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")

#plt.plot([2,3,6,7,10], [1,4,5,8,9], "-", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "--", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], ";", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], "-.", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], ".", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], ".-", label="PData(km)")
#plt.plot([2,3,6,7,10], [1,4,5,8,9], ".--", label="PData(km)")

plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="solid"
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="solid"
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashed"
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dotted"
plt.plot([2,3,6,7,10], [1,4,5,8,9], linestyle="dashdo """