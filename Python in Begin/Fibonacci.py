nterms = int(input("几项"));

#第一项和第二项
n1 = 0;
n2 = 1;
count = 2;

#判断输入是否合法
if nterms <= 0:
    print("请输入一个正数");
elif nterms == 1:
    print("Fibonacci");
    print(n1);
else:
    print("Fibonacci");
    print(n1,",",n2,end=",");
    while(count < nterms):
        nth = n1 + n2;
        print(nth,end=",");
        #交换值
        n1 = n2;
        n2 = nth;
        count += 1;
print();
