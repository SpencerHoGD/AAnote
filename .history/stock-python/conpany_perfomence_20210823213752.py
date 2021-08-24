# 导入 efinance 如果没有安装则需要通过执行命令: pip install efinance 来安装
# 获取最新季报
import efinance as ef
# 股票名称
filenane = 'base_info'
df = ef.stock.get_base_info()
# df = ef.stock.get_all_company_performance()
# df = ef.stock.get_quote_history(stock_code, klt=freq)
# 将数据存储到 csv 文件中
df.to_csv(f'{filenane}.csv', encoding='utf-8-sig', index=None)
print(f'股票: {filenane} 的行情数据已存储到文件: {filenane}.csv 中！')