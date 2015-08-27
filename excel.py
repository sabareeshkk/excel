from xlrd import open_workbook
import pprint


def excelreaderxls(filename):
    wb = open_workbook(filename)
    excel = []
    for s in wb.sheets():
        for row in xrange(s.nrows):
            data = []
            for col in xrange(s.ncols):
                value = (s.cell(row, col).value)
                data.append(value)
            excel.append(data)

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(excel)

if __name__ == "__main__":
    excelreaderxls('sample-data.xls')
