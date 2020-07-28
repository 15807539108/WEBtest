from Common.commonlib import Commonshare
import time


class FINANCIAL(Commonshare):
    def page(self):
        self.login()
        time.sleep(8)
        self.click('id', 'financialManagement')

    def financial_djgl(self):
        self.page()
        time.sleep(1)
        self.click('xpath', '//*[@id="divTabMenus"]/a[1]')

    def financial_zjls(self):
        self.page()
        time.sleep(1)
        self.click('xpath', '//*[@id="divTabMenus"]/a[2]')

    def financial_kskcls(self):
        self.page()
        time.sleep(1)
        self.click('xpath', '//*[@id="divTabMenus"]/a[3]')

    def financial_jfls(self):
        self.page()
        time.sleep(1)
        self.click('xpath', '//*[@id="divTabMenus"]/a[4]')

# if __name__ == '__main__':
#       pass