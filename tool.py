import os,time,sys
try: 
   from faker import Faker
   import radom,re
   from radom import randint
except:
	os.system("pip install faker")
  from faker import Faker
   import radom,re
   from radom import randint
  
faker=Faker()
kytu =[","_",".]
soluong = int(input("nhap so luong:")
luu = input("ten file:")
domain = input("nhap mail:")
n = 0
for fake in range(soluong):
	n+= 1
	num= randint(10,200)
	first_name = faker.first_name().lower()
	getkytu = radom.choice(kytu)
	facemail = first_name + last_name + str(num) +"@" +domain
	print(" " " "+facemail)
	open(luu,"a").write(facemail+"\n")
