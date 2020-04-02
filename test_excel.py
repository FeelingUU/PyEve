import xlrd,xlwt
import os
from xlutils.copy import copy
def red_e():
    cur_path = os.getcwd()+'/'
    file_list = os.listdir(cur_path)
    row_index = 0

    work_book = xlwt.Workbook(encoding='utf-8')
    work_book.add_sheet('sheet1')
    work_book.save(cur_path+'couts.xls')

    for x in file_list:
        print('复制'+x)
        ex = xlrd.open_workbook(cur_path + x)
        she = ex.sheet_by_index(0)
        # print(she.row(0))
        # print(she.nrows)

        list = []
        for i in range(she.nrows):
            list.append(she.row(i))


        for x in range(len(list)):

            for i in range(len(list[x])):
                list[x][i] =str(list[x][i].value)
        # print(list)

        # 写入原excel
        old_work_book = xlrd.open_workbook(cur_path + 'couts.xls', formatting_info=True)
        new_work_book = copy(old_work_book)

        new_she = new_work_book.get_sheet(0)

        for x in range(she.nrows):
            for i in range(she.ncols):
                new_she.write(x + row_index, i,list[x][i] )
        new_work_book.save(cur_path + 'couts.xls')
        row_index = row_index + she.nrows+1


    pass


if __name__ == '__main__':
    red_e()
    pass