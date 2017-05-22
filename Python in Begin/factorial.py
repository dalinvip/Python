num = int(input("请输入一个数字"));
factorial = 1;
if num < 0:
    print("sorry");
elif num == 0:
    print("0 的阶乘为1");
else:
    for i in range(1,num + 1):
        factorial = factorial * i;
    print(factorial);

#字符串判断
str = "runoobcom";
print(str.isalnum());  #字母或者是数字
print(str.isalpha());  #全是字母
print(str.isdigit());  #全是数字
print(str.islower());  #全是小写
print(str.isdecimal());#数值
print(str.isspace());  #空白字符
print(str.istitle());  #首字母大写