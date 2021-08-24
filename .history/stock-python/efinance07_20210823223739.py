# 获取多只基金基本信息
import efinance as ef
# 股票名称
filenane = 'fund_base'
df = ef.fund.get_base_info(['161725', '005827'])
# 将数据存储到 csv 文件中
df.to_csv(f'{filenane}.csv', encoding='utf-8-sig', index=None)
print(f'股票: {filenane} 的行情数据已存储到文件: {filenane}.csv 中！')