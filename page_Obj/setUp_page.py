from Common.commonlib import Commonshare
import time


class SETUP(Commonshare):
    def page(self):
        self.login()
        time.sleep(8)
        self.click('id', 'Member')
        time.sleep(5)
        self.click('id', 'setUp')

    def setup_zhsz(self):
        self.page()
        time.sleep(1)
        self.click('xpath', '//*[@id="topTab"]/a[1]')

    def setup_xtsz(self):
        self.page()
        time.sleep(1)
        self.click('xpath', '//*[@id="topTab"]/a[2]')

    def setup_fwyzc(self):
        self.page()
        time.sleep(1)
        self.click('xpath', '//*[@id="topTab"]/a[3]')



# if __name__ == '__main__':
#     # A = SETUP()


