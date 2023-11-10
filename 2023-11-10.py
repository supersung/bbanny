

""" import multiprocessing
import time

def counter(num):
    for i in range(5):
        print(f"Counter {num} - Step {i + 1}")
        time.sleep(1)


process1 = multiprocessing.Process(target=counter, args=("1num",))
process2 = multiprocessing.Process(target=counter, args=("2num",))
process3 = multiprocessing.Process(target=counter, args=("3num",))


process1.start()
process2.start()
process3.start()


process1.join()
print("Process 1 finished")
process2.join()
print("Process 2 finished")
process3.join()
print("Process 3 finished")

print("All processes have finished.") """

import asyncio
import random as rd
import time

""" async def tester(name):
    snum = rd.randint(10,20)
    print(f"{name} - {snum} - {1}")
    for i in range(snum) :
        await asyncio.sleep(1)
        print(f"{name} - {snum} - {i}")
        
        
async def main():
    task1 = asyncio.create_task(tester("1test"))
    task2 = asyncio.create_task(tester("2test"))
    task3 = asyncio.create_task(tester("3test"))
    
    print("start")
    start = time.time()
    await task1
    await task2
    await task3
    end = time.time()
    print("end",end-start)
    
    
if __name__ == '__main__' :
    asyncio.run(main()) """


""" async def worker1():
    for i in range(1,6) :
        print(f"Task1 : Step {i}")
        await asyncio.sleep(1)
        
async def worker2():
    for i in range(1,4) :
        print(f"Task2 : Step {i}")
        await asyncio.sleep(2)
        
        
async def main():
    
    task_1 = asyncio.create_task(worker1())
    task_2 = asyncio.create_task(worker2())
    
    print("start task")
    await task_1
    await task_2
    print("end task")
    
    
if __name__ == '__main__':
    asyncio.run(main()) """
    
import sched

""" start = time.time()

def tester(name):
    print(f"start-time {time.time() - start}")
    for i in range(3):
        print(f"{name} - {i}")
        
        
    print(f"end of {name}")
    
s = sched.scheduler()
s.enter(5, 1, tester, ('1num',))
s.enter(3, 1, tester, ('1num',))
s.enter(7, 1, tester, ('1num',))
s.run() """

""" import diff_match_patch.diff_match_patch as dm


origin = "To be or not to be, That is a question!"
copyed = "To be or not to be, That is the answer!"

dmp = dm()
diff = dmp.diff_main(origin,copyed)
print (diff)
dmp.diff_cleanupSemantic(diff)

for d in diff:
    print(d) """
    
""" from faker import Faker


fake = Faker("ko_KR")


fake_name = fake.name()
fake_address = fake.address()
fake_postcode = fake.postcode()
fake_country = fake.country()
fake_company = fake.company()
fake_job = fake.job()
fake_phone_number = fake.phone_number()
fake_email = fake.email()
fake_user_name = fake.user_name()
fake_ipv4_private = fake.ipv4_private()
fake_catch_phrase = fake.catch_phrase()
fake_color_name = fake.color_name()


print(f"이름: {fake_name}")
print(f"주소: {fake_address}")
print(f"우편번호: {fake_postcode}")
print(f"국가: {fake_country}")
print(f"회사: {fake_company}")
print(f"직업: {fake_job}")
print(f"전화번호: {fake_phone_number}")
print(f"이메일: {fake_email}")
print(f"사용자명: {fake_user_name}")
 """

""" import subprocess

res = subprocess.run(["cmd", "/c", "dir"], capture_output=True, text=True)


print("Return Code:", res.returncode)
print("\n=== Standard Output ===")
print(res.stdout)
print("\n=== Standard Error ===")
print(res.stderr) """


""" import traceback as tb

def tester():
    return 1/0

def caller() :
    tester()
    
def main() :
    try :
        caller()
        
    except ZeroDivisionError:
        print("zde error")
        
    except ValueError :
        print("ve error")
        
    except Exception as ex:
        print("ex error", ex)
        
    else :
        print("ok")
        
    finally :
        print() """
        
""" from bs4 import BeautifulSoup as bs
import requests as rq

url = "https://xkcd.com/2852/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, "html.parser")

pres = res_html.find("h1")
print(pres)
print("\n1-------------------\n")
print(pres.get_text().strip())
print("\n2-------------------\n")
print(pres.next_element.get_text.strip())
print(pres.get_text())
print("\n6----------------------\n")


fares = res_html.findAll("a")
for i in fares:
    print(i.get_text())
    
import requests as rq
from bs4 import BeautifulSoup as bs
   




url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')

item = res_html.select_one("body > div.container.do")


print(item.get_text())    


wt = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > div > span.txt_name")
print(wt.get_text())


goods = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_reply > div > button > strong")
print(goods.get_text()) """

A

