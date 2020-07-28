from Common.commonlib import Commonshare
import time


class DISCOVER(Commonshare):
    def page(self):
        self.login()
        time.sleep(8)
        self.click('id', 'discover')

    def doscover_wdyy(self):
        self.page()
        time.sleep(1)
        self.click('xpath', '//*[@id="divTabMenus"]/a[1]')

    def doscover_yyzx(self):
        self.page()
        time.sleep(1)
        self.click('xpath', '//*[@id="divTabMenus"]/a[2]')

if __name__ == '__main__':
    A = DISCOVER()
    A.doscover_wdyy()
    time.sleep(10)
    A.driver.quit()
