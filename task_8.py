a=""
for i in range(1,10):
    b=a+str(i)
    c=int(b)*8+i
    print(b,"* 8 + ",i,"=",c)
    a=b
a=""
for i in range(1,10):
    b=a+str(i)
    c=int(b)*9+i+1
    print(b,"* 9 + ",i+1,"=",c)
    a=b
a="1"
for i in range(1,10):
    b=a*i
    c=int(b)**2
    print(b, "*  ",b, "=", c)
