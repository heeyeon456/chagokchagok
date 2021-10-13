import openpyxl

wb = openpyxl.load_workbook('my.xlsx')
sh1 = wb['sheet1']
sh2 = wb['sheet2']

print(sh1['A1'].value)
print(sh2['A1'].value)
# 수정
sh1['C1'] = 'aaa'
wb.save('my.xlsx')

