from xlrd import open_workbook
import pprint

wb = open_workbook('sample-data.xls')

excel = {}

for s in wb.sheets():
    excel['sheet' + str(wb.sheets().index(s))] = {}
    for col in xrange(s.ncols):
        excel['sheet' + str(wb.sheets().index(s))]['col' + str(col)] = []
        for row in xrange(s.nrows):
            value = (s.cell(row, col).value)
            excel['sheet' + str(wb.sheets().index(s))]['col' + str(col)].append(value)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(excel)
