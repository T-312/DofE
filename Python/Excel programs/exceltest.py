import xlsxwriter, os

os.chdir('/Users/tim10')

wb = xlsxwriter.Workbook('test.xlsx')
ws = wb.add_worksheet('Expenses')

bold = wb.add_format({'bold' : True})

ws.set_column(0, 1, 10)

data = (
    ['10-12-2014', 'Rent', 1000],
    ['01-01-2015', 'Gas',   100],
    ['17-01-2015', 'Food',  300],
    ['11-02-2015', 'Gym',    50],
)

row, col = 0, 0
for date_num, item, price in data:
    ws.write(row, col, date_num)
    ws.write(row, col+1, item)
    ws.write(row, col+2, price)
    row+=1

ws.write(row, col, 'Total', bold)
ws.write(row, col+1, '=SUM(C1:C4)')

wb.close()
os.startfile('test.xlsx')