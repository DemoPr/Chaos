name = 'chaos'
stock_price = 18.88
stock_code = '0032'
days = 500
# 使用%进行格式化
print("公司：%s " "股价：%.3f " "股票代码：%s " "成立天数：%d " %(name,stock_price,stock_code,days))
# 使用f{}进行格式化
print(f"公司：{name} " f"股价：{stock_price} " f"股票代码：{stock_code} " f"成立天数：{days} ")
print(f"公司：{name} 股价：{stock_price} 股票代码：{stock_code} 成立天数：{days}")
print("input name:")
name = input()
age = input()
age = int(age)
print(name,age)
print(type(age))
