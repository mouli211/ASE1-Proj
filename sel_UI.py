from selenium import webdriver
import unittest
import HtmlTestRunner

class ProjectAuto(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("C:\\selenium drivers\\chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_auto_signup_page(self):
        self.driver.get("http://127.0.0.1:8000/")
        elem = self.driver.find_element_by_link_text('accounts/signup')

    def test_auto_signup_user(self):
        self.driver.get("http://127.0.0.1:8000/accounts/login/")
        self.driver.find_element_by_name('username').send_keys('Mouli')
        self.driver.find_element_by_name('password').send_keys('asdf')
        self.driver.find_element_by_class_name('btn').click()

    def test_auto_login_page(self):
        self.driver.get("http://127.0.0.1:8000/accounts/login/")
        elem = self.driver.find_element_by_link_text('accounts/login')


    def test_auto_login_usr(self):
        self.driver.get("http://127.0.0.1:8000/accounts/login/")
        self.driver.find_element_by_name('username').send_keys('Mouli')
        self.driver.find_element_by_name('password').send_keys('asdf')
        self.driver.find_element_by_class_name('btn').click()

    def test_auto_login_pwd(self):
        self.driver.get("http://127.0.0.1:8000/accounts/login/")
        self.driver.find_element_by_name('username').send_keys('afsd')
        self.driver.find_element_by_name('password').send_keys('Mouli211')
        self.driver.find_element_by_class_name('bt').click()

    def test_auto_login_pwd_usr(self):
        self.driver.get("http://127.0.0.1:8000/accounts/login/")
        self.driver.find_element_by_name('username').send_keys('Mouli')
        self.driver.find_element_by_name('password').send_keys('Mouli211')
        self.driver.find_element_by_class_name('bt').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('test completed')

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\mouli\\Desktop\\Generated"))