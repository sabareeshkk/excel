from xlrd import open_workbook
import pprint

wb = open_workbook('sample-data.xls')

excel = {}

for s in wb.sheets():
    excel[str(wb.sheets().index(s))] = []
    for row in xrange(s.nrows):
        for col in xrange(s.ncols):
            value = (s.cell(row, col).value)
            excel[str(wb.sheets().index(s))].append(value)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(excel)
