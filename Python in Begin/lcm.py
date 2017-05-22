#最小公倍数函数
def lcm(x,y):
    if x > y:
        greater = x;
    else:
        greater = y;
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater;
            break;
        greater += 1;
    return lcm;

#用户输入
number1 = int(input("First number:"));
number2 = int(input("Second number:"));

print(number1," 和 ",number2,"最大公倍数是:",lcm(number1,number2));