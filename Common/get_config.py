from configparser import RawConfigParser
import os

from Common.handle_path import config_dir


class GetConfig(RawConfigParser):  # 当配置文件中有报告输出格式内容是使用RawConfigParser

    def __init__(self):
        super().__init__()

        config_path = os.path.join(config_dir, "config.ini")
        self.read(config_path, encoding='utf-8')


conf = GetConfig()




