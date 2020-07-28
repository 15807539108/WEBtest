"""
该类主要是存放一些公共方法，比如：元素查找、截屏
、操作Excel、鼠标点击、键盘输入、登录系统等等
"""
from selenium import webdriver
# 导入Pillow包，PIL在python2.7已弃用，python3以上需要导入Pillow包
from PIL import ImageGrab
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from Common.get_config import conf


# filePath当前路径
filePath = os.path.split(os.path.dirname(__file__))[0]
# 获取url、账号、密码
url = conf.get("server", "url")
name = conf.get("default_user", "phone")
pwd = conf.get("default_user", "pwd")


class Commonshare(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def __del__(self):
        pass
        # self.driver.quit()

    # 打开指定网页
    def open_url(self):
        driver = self.driver
        driver.get(url)
        time.sleep(1)

    '''
    元素定位方法
    locate_type：定位元素的方法
    value：元素对应的值
    '''
    def locateElement(self, locate_type, value):
        # 判断定位方式并调用相关方法
        driver = self.driver
        el = None
        if locate_type == 'id':
            try:
                driver.find_element_by_id(value).is_displayed()
            except Exception:
                driver.quit()
                raise Warning("元素定位失败%s")
            else:
                el = driver.find_element_by_id(value)
            return el

        elif locate_type == 'name':
            el = driver.find_element_by_name(value)

        elif locate_type == 'class':
            el = driver.find_element_by_class_name(value)

        elif locate_type == 'xpath':
            try:
                driver.find_element_by_xpath(value).is_displayed()
            except Exception:
                driver.quit()
                raise Warning("元素定位失败%s")
            else:
                el = driver.find_element_by_xpath(value)
            return el

        elif locate_type == 'link_text':
            try:
                driver.find_element_by_link_text(value).is_displayed()
            except Exception:
                driver.quit()
                raise Warning("元素定位失败%s")
            else:
                el = driver.find_element_by_link_text(value)
            return el

        elif locate_type == 'partial_link_text':
            el = driver.find_element_by_partial_link_text(value)

        elif locate_type == 'css_selector':
            el = driver.find_element_by_css_selector(value)

        if el is not None:
            return el

    # 鼠标点击
    def click(self, locate_type, value):
        # 调用定位方法进行元素定位
        el = self.locateElement(locate_type, value)
        # 执行点击操作
        el.click()

    # 鼠标悬停
    def move_to_element(self, locate_type, value):
        ele = self.locateElement(locate_type, value)
        ActionChains(self.driver).move_to_element(ele).perform()

    # 键盘输入
    def input_data(self, locate_type, value, data):
        el = self.locateElement(locate_type, value)
        el.clear()
        el.send_keys(data)

    # 登录系统
    def login(self):
        self.open_url()
        self.input_data('id', 'userName', name)
        self.input_data('id', 'pwInput', pwd)
        self.click('id', 'btnLogin')

    # 选择日期
    def select_date(self, date):
        value = '[hmdate="' + date + '"]'
        self.click('css_selector', value)

    '''
    屏幕截图功能
    imPath:图片保存路径
    imType:图片类型
    '''

    def Screenshot(self, imPath, imType):
        im = ImageGrab.grab()
        im.save(imPath, imType)

    def Screenshot1(self):
        currentTime = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
        # log文件的存放路径
        imPath = filePath + '/Result/Picture/' + currentTime + '.png'
        im = ImageGrab.grab()
        im.save(imPath)

    def Screenshot2(self, imPath):
        im = ImageGrab.grab()
        im.save(imPath)

    '''
    使用 JS操作页面滚动条
    '''
    # 当前页面移动至某个元素位置
    def page_move(self, locate_type, value):
        wei_zhi = self.locateElement(locate_type, value)  # 先定位到一个元素
        self.driver.execute_script("arguments[0].scrollIntoView();", wei_zhi)

    # 使用ID指定特定的页面滑动指定像素 （num：滑动的像素）
    def page_sliding(self, id, num):
        num = str(num)
        js = 'document.getElementById("' + id + '").scrollTop=' + num
        self.driver.execute_script(js)

    # 判断元素是否存在
    def isElementPresent(self, by, value):
        try:
            element = self.locateElement(by, value)
        except NoSuchElementException as e:
            return False
        else:
            return True

    # 获取明天日期
    def tomorrowDate(self):
        # 获取当前时间戳
        today_timestamp = time.time()
        # 转化时间格式
        tomorrow_date = time.strftime('%Y-%m-%d', time.localtime(today_timestamp + 86400))
        return tomorrow_date

    # 获取昨天日期
    def yesterdayDate(self):
        # 获取当前时间戳
        today_timestamp = time.time()
        # 转化时间格式
        yesterday_date = time.strftime('%Y-%m-%d', time.localtime(today_timestamp - 86400))
        return yesterday_date