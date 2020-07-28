import logging
import time
import os

from Common.get_config import conf
from Common.handle_path import log_dir


class MyLogger(logging.Logger):

    def __init__(self, name, level=logging.INFO, file=None):
        # 重写默认的Logger方法，设置输出级别、输出渠道、输出日志格式
        super().__init__(name, level)

        # 日志格式
        formatter = logging.Formatter(conf.get("log", "formatter"))

        # 输出到控制台
        s_handle = logging.StreamHandler()  # 输出渠道控制台
        s_handle.setFormatter(formatter)  # 关联渠道的日志格式
        self.addHandler(s_handle)  # 将设置到的渠道添加到日志收集器中

        # 输出到文件
        if conf.getboolean("log", "file_is"):  # 判断配置中file_is项决定是否打印日志文件
            # 定义文件生成路径与文件名
            now_time = time.strftime("%m%d%H%M")
            log_path = log_dir
            new_file = os.path.join(log_path, now_time + file)
            # 输出到文件
            f_handle = logging.FileHandler(new_file, encoding="utf-8")
            f_handle.setFormatter(formatter)
            self.addHandler(f_handle)


logger = MyLogger(conf.get("log", "log_name"), level=conf.get("log", "level"), file=conf.get("log", "file_name"))
