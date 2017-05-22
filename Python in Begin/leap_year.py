try:
    year = int(input("输入一个年份   "));
except:
    print("请输入正确的年份");
    exit();
if (year % 100 == 0) and (year % 400 == 0):
    print(year,"年是闰年");
elif (year % 100 == 0) and (year % 4 == 0):
    print(year,"年是闰年");
else:
    print(year,"年不是闰年");
