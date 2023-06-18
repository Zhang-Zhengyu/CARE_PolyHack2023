import re
import openpyxl

# 打开Excel文件
workbook = openpyxl.load_workbook('zhihu_answers.xlsx')

# 获取第一个工作表
worksheet = workbook.active

# 遍历每个单元格
for row in worksheet.iter_rows():
    for cell in row:
        # 使用正则表达式删除<>包围的内容
        cell.value = re.sub('<[^>]+>', '', str(cell.value))

# 保存修改后的Excel文件
workbook.save('example_modified.xlsx')