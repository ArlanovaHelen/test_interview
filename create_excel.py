from openpyxl import Workbook
import sqlite_db
def create_statistic_file():
    sqlite_db.db_connect()
    data = sqlite_db.get_table_info()

    wb = Workbook()
    ws = wb.active
    mylist = ['datetime_info', 'vacancy_count',  'change']
    ws.append(mylist)

    for i in data:
        k = list(i)
        ws.append(k[1:])

    wb.save('report.xlsx')
    wb.close()
