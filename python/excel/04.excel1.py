import openpyxl

# 하나의 엑셀
wb = openpyxl.Workbook()
# sheet 생성
sh1 = wb.active
# 디폴트 sheet 타이틀 제목 Sheet
sh1.title = 'sheet1'
# sheet2 생성
sh2 = wb.create_sheet('sheet2')
# 셀에 데이터 넣기
sh1['A1'] = 10
sh1['A2'] = 20
sh1['B1'] = 'python'
sh1['A3'] = '=sum(A1:A2)'

sh2['A1'] = 'hello'
wb.save('my.xlsx')
