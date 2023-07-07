import xlrd

def get_data(file_name, sheet_name):
    wb = xlrd.open_workbook(file_name)
    sheet = wb.sheet_by_name(sheet_name)
    data = []
    for i in range(1,sheet.nrows):
        temp = []
        for j in range(sheet.ncols):
            temp.append(sheet.cell_value(i,j))
        data.append(temp)
    return data

