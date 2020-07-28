from Common.commonlib import Commonshare
import time

def AddCourse():
    cmn = Commonshare()
    cmn.login()
    time.sleep(5)
    cmn.click('id', 'Teaching')
    time.sleep(1)
    cmn.move_to_element('id', 'btnOpList_center')
    time.sleep(1)
    cmn.click('xpath', '//*[@id="opList"]/li[1]/a')

    ele = cmn.locateElement('xpath', '//*[@id="dialogBox0"]/div/div/div[2]/iframe')
    cmn.driver.switch_to.frame(ele)

    cmn.input_data('xpath', '//*[@id="topic"]', '音乐主题')
    cmn.click('xpath', '//*[@id="dyarrange"]/div[1]/div[1]/div[5]/div')
    time.sleep(1)

    #使指定的页面向下滚动50个像素
    cmn.page_sliding(50)
    time.sleep(1)

    #选择课程系列
    cmn.click('xpath', '//*[@id="courseList"]/div[1]/li[8]/a')
    time.sleep(30)

AddCourse()








