from os import remove
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title('Base de datos de tickets')

remove("balances.xlsx")
wb.save('balances.xlsx')

