import re
from page_Obj.setUp_page import SETUP
import time

cmn = SETUP()
cmn.page()
time.sleep(2)
cmn.move_to_element('xpath', '//*[@id="btnOpList_center"]')
time.sleep(2)
cmn.click('xpath', '//*[@id="addUser"]/a')
ele = cmn.driver.find_element_by_xpath('//*[@id="dialogBox0"]/div/div/div[2]/iframe')
cmn.driver.switch_to.frame(ele)
cmn.click('xpath', '//*[@id="schoolId"]/div/div/div[2]/a/i')
time.sleep(2)
source = cmn.driver.page_source
data = '天河测试'
zz = r"<li>.*?</i>(" + data + ")</span>"
a = re.findall(zz, source, re.DOTALL)  # re.DOTALL 解决多行匹配时换行的问题
print(a)
if len(a) > 0:
    if a[0] == data:
        print("成功")
    else:
        print('定位错误')
else:
    raise Warning("不存在")

cmn.driver.quit()







