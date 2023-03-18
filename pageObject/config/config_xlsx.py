import xlrd
import os
dir = os.path.dirname(os.path.realpath('__file__'))
# print(dir)
filename = os.path.join(dir, 'excel/sample.xlsx')

#install xlrd

class ConfigXlsxData:
    #open_woekbook will oopen the entire excel file
    book = xlrd.open_workbook(filename)
    #sheet_by_name() it take one argument (str) the sheet name which we need to read
    sheet1 = book.sheet_by_name('Sheet1')
    # nrows is function which is not callable it will return number of rows
    row_count = sheet1.nrows
    # ncols is function which is not callable it will return number of columns
    col_count = sheet1.ncols




obj = ConfigXlsxData()
