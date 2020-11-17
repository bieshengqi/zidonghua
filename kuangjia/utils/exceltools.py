"""
    读取excel
"""
import xlrd

def read_excel(excel_path, sheet_name, skip_first=True):
    """
        方法：python读取excel
        参数：
            - excel_path：excel的路径
            - sheet_name：表格名字
            - skip_first: 是否跳过首行，True：跳过；False：不跳过，默认值是跳过
        返回值：[[1, "xxx接口成功", "/login"...], []]
    """
    results = [] 
    datas = xlrd.open_workbook(excel_path)
    table = datas.sheet_by_name(sheet_name)
    if skip_first == True:
        start_row = 1
    else:
        start_row = 0

    # 循环读取每一行数据
    for row in range(start_row, table.nrows):
        results.append(table.row_values(row))

    return results


if __name__ == "__main__":
    a = read_excel("./data/测谈网接口.xlsx", "首页")
    print(a)
