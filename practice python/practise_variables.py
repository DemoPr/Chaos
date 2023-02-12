
sum_money = 500000
name = "Jack"
flag = True
# 查询余额
def query_balance():
    print(f"当前钱包余额：{sum_money}元")
    print()
# 进行存款
def add_money():
    money = int(input("请输入您的存钱数："))
    global sum_money
    sum_money += money
# 进行取款
def get_money():
    money = int(input("请输入您的取钱数："))
    global sum_money
    sum_money -= money
# 进入主菜单
while flag:
    print(f"欢迎用户：{name},以下是主菜单:")
    print("查询余额请按：1")
    print("存钱请按：2")
    print("取钱请按：3")
    print("主菜单页面请按：0")
    choose = int(input("请输入您的操作（0-3）："))
    if choose == 1:
        query_balance()
    elif choose == 2:
        add_money()
    elif choose == 3:
        get_money()
    elif choose == 0:
        continue
    else:
        print("输入代码错误，系统退出")
        break