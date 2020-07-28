from page_Obj.teaching_page import TEACHING
import unittest
import time

class AddMember(unittest.TestCase):
    def test001(self):
        cmn = TEACHING()
        cmn.teaching_hd()
        cmn.move_to_element('xpath', '//*[@id="btnOpList_center"]')
        time.sleep(1)
        cmn.click('link_text', '添加活动')

        ele1 = cmn.locateElement('xpath', '//*[@id="dialogBox0"]/div/div/div[2]/iframe')
        cmn.driver.switch_to.frame(ele1)

        cmn.click('xpath', '//*[@id="activeStartTime"]/div/button')



        time.sleep(5)
        cmn.driver.quit()

if __name__ == '__main__':
    unittest.main()