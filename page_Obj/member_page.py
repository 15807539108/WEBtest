from Common.commonlib import Commonshare
import time


class MEMBER(Commonshare):
    def page(self):
        self.login()
        time.sleep(8)
        self.click('id', 'Member')

    def member_qzxy(self):
        self.page()
        time.sleep(1)
        self.click('xpath', '//*[@id="topTab"]/a[1]')

    def member_zsxy(self):
        self.page()
        time.sleep(1)
        self.click('xpath', '//*[@id="topTab"]/a[2]')

    def member_lxxy(self):
        self.page()
        time.sleep(1)
        self.click('xpath', '//*[@id="topTab"]/a[3]')

    def member_ghxy(self):
        self.page()
        time.sleep(1)
        self.click('xpath', '//*[@id="topTab"]/a[4]')


# if __name__ == '__main__':
#     pass
