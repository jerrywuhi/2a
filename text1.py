def square(y):
	print(f"{y}的平方是{y*y}")



x =int(input("請輸入一 個數字:"))
#x +=10

if (x<=0):
    print(f"你輸入的值是{x}","小於等於0" )
else:
    print(f"你輸入的值是{x}","大於0")
    for i in range(1,x+1):
        #print (i, end=";")    
        square(i)