import time
import os
from config import *
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AutoConnect:
    def __init__(self, id, pwd):
        self.url = URL
        self.student_id = id
        self.student_pwd = pwd
        self.driver_path = DRIVER_PATH
        self.service = Service(executable_path=self.driver_path)
        self.options = webdriver.EdgeOptions()
        self.driver = webdriver.Edge(service=self.service, options=self.options)
        # if browser == 'Chrome':
        #     self.driver_path = r'D:\py\AutoTest\ChromeDriver\chromedriver.exe'
        #     self.service = Service(executable_path=self.driver_path)
        #     self.options = webdriver.ChromeOptions()
        #     self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def connect(self):
        if not USE_WLAN:
            os.system(r'C:\Drcom\DrUpdateClient\DrMain.exe')
            time.sleep(5)
            return
        self.driver.get(self.url)
        student_id_input = self.driver.find_element(By.XPATH,
                                                    '//div[@class="edit_loginBox normal_box  random loginuse loginuse_pc ui-resizable-autohide"]/form//input[@name="DDDDD"]')
        select = Select(self.driver.find_element(By.XPATH,
                                                 '//div[@class="edit_loginBox normal_box  random loginuse loginuse_pc ui-resizable-autohide"]//select[@name="ISP_select"]'))
        password_input = self.driver.find_element(By.XPATH,
                                                  '//div[@class="edit_loginBox normal_box  random loginuse loginuse_pc ui-resizable-autohide"]/form//input[@name="upass"]')
        submit_button = self.driver.find_element(By.XPATH,
                                                 '//div[@class="edit_loginBox normal_box  random loginuse loginuse_pc ui-resizable-autohide"]/form//input[@name="0MKKey"]')

        student_id_input.send_keys(self.student_id)
        select.select_by_index(1)
        password_input.send_keys(self.student_pwd)
        submit_button.click()
        time.sleep(5)
        self.driver.close()


if __name__ == '__main__':
    AutoConnect(STUDENT_ID, STUDENT_PASSWORD).connect()
