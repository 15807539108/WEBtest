"""
获取项目中其他模块会用到的path
"""
import os

# 项目路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试用例路径
cases_dir = os.path.join(project_path, "Test_cases")

# 测试数据路径
datas_dir = os.path.join(project_path, "Test_datas")

# 配置文件路径
config_dir = os.path.join(project_path, "Config")

# 报告输出路径
# log
log_dir = os.path.join(project_path, "Result\\logs")
# report
report_dir = os.path.join(project_path, "Result\\report")

print("1111")
