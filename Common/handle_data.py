"""
Envdata用于存放全局变量
replace_mark_with_data方法将测试用例中占位的mark替换为相应的数据
replace_case_regular 使用正则抓取用例中需要替换的信息并直接替换，相比使用mark替换来说更方便些
"""
import re
import json
from Common.get_config import conf


class Envdata:
    """
    用来存放全局变量
    """
    pass


def replace_case_regular(case):
    """
    case
    """
    case_str = json.dumps(case)
    new_case = replace_by_regular(case_str)
    case_dict = json.loads(new_case)
    return case_dict


def replace_by_regular(data):
    """
    data：需要替换的数据（字符串）
    """
    res = re.findall("#(.*?)#", data)  # 如果没有找到返回值是空
    if res:
        # 现在配置中找，如果找不到再去环境变量中找
        for item in res:
            try:
                value = conf.get("data", item)
            except:
                # 当环境变量中也找不到对应的对象时不做替换
                try:
                    value = getattr(Envdata, item)
                except AttributeError:
                    # value = "#{}#".format(item)
                    continue
            data = data.replace("#{}#".format(item), str(value))
    return data


def replace_mark_with_data(case, mark, new_data):
    """
    :param case:一条完整的用例
    :param mark: 数据中的占位符
    :param new_data: 需要替换mark的真实数据
    """
    for key, value in case.items():
        if value is not None and isinstance(value, str):
            case[key] = value.replace(mark, new_data)
    return case



