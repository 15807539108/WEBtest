from Common.commonlib import Commonshare
import time


class TEACHING(Commonshare):
    def page(self):
        self.login()
        time.sleep(8)
        self.click('id', 'Teaching')

    def teaching_kcb(self):
        self.page()
        time.sleep(1)
        self.click('xpath', '//*[@id="divTabMenus"]/a[1]')

    def teaching_kqqd(self):
        self.page()
        time.sleep(1)
        self.click('xpath', '//*[@id="divTabMenus"]/a[2]')

    def teaching_bjgl(self):
        self.page()
        time.sleep(1)
        self.click('xpath', '//*[@id="divTabMenus"]/a[3]')

    def teaching_zykp(self):
        self.page()
        time.sleep(1)
        self.click('xpath', '//*[@id="divTabMenus"]/a[4]')

    def teaching_kckcb(self):
        self.page()
        time.sleep(1)
        self.click('xpath', '//*[@id="divTabMenus"]/a[5]')

    def teaching_hd(self):
        self.page()
        time.sleep(1)
        self.click('xpath', '//*[@id="divTabMenus"]/a[6]')



# if __name__ == '__main__':
#     A = TEACHING()

