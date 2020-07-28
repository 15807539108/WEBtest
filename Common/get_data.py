"""
获取excel表格的case数据
"""
from openpyxl import load_workbook
import os

from Common.handle_path import datas_dir


# 读取excel表格中的数据，并把它转换成ddt可识别的格式
class GetExcelData:

    def __init__(self, excel_name, sheet_name):
        file_path = os.path.join(datas_dir, excel_name)  # 获取文件路径
        self.wb = load_workbook(file_path)  # 读取文件内容
        self.sh = self.wb[sheet_name]  # 获取表格内的对应页面

    def get_all_data(self):
        data_keys = []
        for title in list(self.sh.rows)[0]:  # 先取出标题, 遍历sh的第一行数去循环取出标题
            data_keys.append(title.value)

        case_data = []  # 定义一个最后装数据的列表
        for data in list(self.sh.rows)[1:]:  # 获取测试用例的数据,sh.rows是逐行读取,从二行开始遍历到最后一行
            data_values = []
            for val in data:  # 遍历第一行内容，得到每个单元格的数据红并且写入到data_values
                data_values.append(val.value) # val指的是单元格的信息，需要调用出val的value值才是想要获取的信息
            res = dict(zip(data_keys, data_values))  # 使用zip函数将key和value打包成键值对格式然后转换为字典类型
            case_data.append(res)  # 添加到数据列表
        return case_data

    def close_excel(self):
        self.wb.close()


if __name__ == '__main__':
    exc = GetExcelData("ApiTest.xlsx", "registered")
    datas = exc.get_all_data()
    exc.close_excel()
    for item in datas:
        print(item)
        # print(json.dumps(item, ensure_ascii=False))  # 将json转换为字典格式 ensure_ascii=False设置中文编码格式