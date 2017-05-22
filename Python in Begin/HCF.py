#定义一个函数
def hcf(x,y):
    if x > y:
        smaller = y;
    else:
        smaller = x;
    for i in range(1,smaller+1):
        if(x % i == 0 ) and (y % i == 0):
            hcf = i;
    return hcf;

#输入两个数
number1 = int(input("one number:"));
number2 = int(input("second number:"));

print(number1," 和 ",number2," 最大公约数是 ",hcf(number1,number2));