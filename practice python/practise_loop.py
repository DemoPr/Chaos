import random
# # while 9*9乘法表
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(f"{i}*{j}={i*j}\t",end='')
#         j+=1
#     print()
#     i+=1
# # for循环99乘法表
# for x in range(1,10):
#     for k in range(1,x+1):
#         print(f"{x}*{k}={x * k}\t", end='')
#     print()
sum_salary = 10000
score = 0
for i in range(1,21):
    score = random.randint(1,10)
    if sum_salary >= 1000:
        if score <= 5:
            print(f"员工{i}号，绩效分{score},低于5分，不发工资，下一位")
            continue
        else:
            sum_salary -= 1000
            print(f"向员工{i}号，绩效分{score},发放工资1000元，还剩余{sum_salary}元")
    else:
        print(f"员工{i}号,没有工资了，下月发")
        break
def chaos_len(str):
    """
    :param str: 需要判断长度的字符串
    :param j: 无实际意义
    :return: 返回字符串的长度
    """
    count = 0
    for i in str:
        count += 1
    return count
def print_len():
    print(f"字符串长度是：{chaos_len(stt)}位")

stt = "hell898 "
print_len()
